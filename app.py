import os
from flask.templating import render_template_string,render_template
from flask import Flask,jsonify,request,Response,redirect
from logger import logger
# from flask_ngrok import run_with_ngrok
from airtablehandler import *
from scheduledTask import *
from cryptography.fernet import Fernet
from setup import *
#For Encryption


crypter = Fernet(key)

# Method for encrypt
def encrypt(mess):
    mid = bytes(f"{mess}", 'utf-8')
    #encryption with the present key
    q = crypter.encrypt(mid)
    q = str(q,'utf8')
    return q

def decrypt(mess):
    enc = bytes(mess,'utf-8')
    print(enc)
    decdata =str(crypter.decrypt(enc),'utf8')
    return decdata


#Setting the flask app
app = Flask(__name__)
# app.url_map.strict_slashes=False
# run_with_ngrok(app)



# token = os.environ.get('token')  #production
bot=logger(token)


#ForTGBot


def handlecommands(text,chat_id,msg_id,gid):
    headers = {'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"}
    if(text[:6]=="/start"):
        imgurl="https://telegra.ph/file/28d63ceb53d4ab684aa1e.jpg"
        text1="""*Hello, I'm Birthday Reminder Bot,*
I can remind birthday of your favourite ones,
Just share the bot with the one you need to remember their birthday of,
Bot will collect their birthday info and remind in group on their birthday,

To know more about bot usage
[API Source Code](https://github.com/RorYin/BirthdayReminderTgBot)
[Bot Developped By RorYin](https://github.com/RorYin)

*Made with ❤️ In India*"""
        bot.sendPhoto(imgurl,text1,gid,msg_id,"Markdown")
        return

    elif(text[:5]=="/help"):
        imgurl="https://telegra.ph/file/28d63ceb53d4ab684aa1e.jpg"
        txt1="""*Hello, I'm Birthday Reminder Bot*,
I can remind birthday of your favourite ones,
Just share the bot with the one you need to remember their birthday of,
Bot will collect their birthday info and remind in group on their birthday,

To know more about bot usage
[API Source Code](https://github.com/RorYin/BirthdayReminderTgBot)
[Bot Developped By RorYin](https://github.com/RorYin)

*Made with ❤️ In India*"""
        bot.sendPhoto(imgurl,txt1,gid,msg_id,"Markdown")
        return
    elif(text[:5]=="/join"):
        # Sending a link to collect his birthday

        q = encrypt(chat_id)
        q2 = encrypt(gid)
        url = f"./newuser?id={q}&gid={q2}"

        msg = f"""[Click here to open link and register..!]({url})"""
        bot.sendMsgTo(gid,msg,msg_id,"Markdown")
        return

    elif(text[:9]=="/checknow"):
        if(chat_id == devTGid):
            bot.sendMsgTo(gid,f"Checking for birthdays....",msg_id,"Markdown")
            checkforbirthdays(gid)
            return
        else:
            bot.sendMsgTo(gid,"*You are not authorised to use this command*",msg_id,"Markdown")
            return


    elif(text[:8]=="/dodaily"):
        if(chat_id == devTGid):
            dodaily()
            return
        else:
            bot.sendMsgTo(gid,"*You are not authorised to use this command*",msg_id,"Markdown")
            return

    elif(text[:6]=="/today"):
        msg = gettoday()
        bot.sendMsgTo(gid,msg,msg_id,"Markdown")
        return
    elif(text[:3]=="/id"):
        bot.sendMsgTo(gid,f"gid = {gid} & chatid = {chat_id}",msg_id,"Markdown")
        return
        # if(chat_id == devTGid):
        #     bot.sendMsgTo(gid,f"gid = {gid} & chatid = {chat_id}",msg_id,"Markdown")
        #     return
        # else:
        #     bot.sendMsgTo(gid,"*You are not authorised to use this command*",msg_id,"Markdown")
        #     return

    else:
        bot.sendMsgTo(gid,"Please wait....",msg_id,"Markdown")
        handletgbotquery(text,chat_id,msg_id,text[1:])
        return



@app.route('/',methods=['POST','GET'])
def home():
    # Do something
    query=request.args.get('q')
    if query == None:
        return render_template("index.html")
    else:
        print(query)



@app.route('/botupdates',methods=['POST','GET'])
def handlebot():
    if request.method == "POST":

        try:
            msg=request.get_json()
        except:
            bot.sendMsgTo(devTGid,"Something went wrong in bot while getting updates",55,"Markdown")
            print("Something went wrong while getting updates")
            return Response("Ok",status=200)

        try:
            #get all normal text messages
            gid=msg['message']['chat']['id']
            text=msg['message']['text']
            message_id=msg['message']['message_id']
        except:
            # bot.sendMsgTo(devTGid,"Something went wrong in bot while parsing json data",55,"Markdown")
            print("Something went wrong while parsing json data")
            return Response("Ok",status=200)

        # TO get chat_id if exists
        try:
            chat_id = msg['message']['from']['id']  #here chat_id is nothing but the from id and gid is chat_id as in json
        except:
            chat_id = devTGid
            #Do nothing

        if (text[0]=="/"):
                handlecommands(text,chat_id,message_id,gid)
                return Response("Ok",status=200)
        else:
            handlecommands("/help",chat_id,message_id,gid)
            return Response("Ok",status=200)

@app.route('/newuser',methods=['POST','GET'])
def newuser():
    id=request.args.get('id')

    gid = request.args.get('gid')

    return render_template("index.html",chatid=id,gid=gid)

@app.route('/register',methods=['POST','GET'])
def register():
    id = request.args.get('id')
    gid = request.args.get('gid')
    gid = str(gid)
    try:
        decid = decrypt(id)
        decgid = decrypt(gid)
    except:
        return redirect(f"./registered?q=404")
    name = request.args.get('name')
    bday = request.args.get('bday')

    if(name == "" or bday == ""):
        return redirect("./registered?q=500")
    print(decid,decgid)
    respcode = updatedata(name,bday,decid,decgid)

    return redirect(f"./registered?q={respcode}")


@app.route('/registered',methods=['POST','GET'])
def openpage():
    # if(request.args.get('q')==200):
    #     return render_template("registered.html",imgurl="Sucessfully Registered")
    # else:
    #     return render_template("registered.html",igmurl="Check all fields and try again")
    if(request.args.get('q')=='200'):

        return render_template("registered.html",msg="Sucessfully Registered")
    elif(request.args.get('q')=='501'):
        return render_template("registered.html",msg="""You have already registered, if required you can degister by sending "/deregister" to the bot, and try registering again""")
    elif(request.args.get('q')=='404'):
        return render_template("registered.html",msg="Something went wrong")
    else:
        return render_template("registered.html",msg="Check all fields and try again")

if __name__ == '__main__':
    app.debug=True
    app.run()