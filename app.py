import os
from flask.templating import render_template_string,render_template
from flask import Flask,jsonify,request,Response,redirect
from logger import logger
# from flask_ngrok import run_with_ngrok
from airtablehandler import *
from scheduledTask import *

#Setting the flask app
app = Flask(__name__)
# app.url_map.strict_slashes=False
# run_with_ngrok(app)

token = "5002606701:AAFt2QcHWaEgqW0T63dXmTIQYglYX2Dw1bM" #testing

# token = os.environ.get('token')  #production
bot=logger(token)


#ForTGBot
def handletgbotquery(text,chat_id,msg_id,query):
    headers = {'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"}
    url="http://roryin-newsapi.herokuapp.com/?q="

def handlecommands(text,chat_id,msg_id):
    headers = {'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"}
    if(text[:6]=="/about"):
        imgurl="https://telegra.ph/file/28d63ceb53d4ab684aa1e.jpg"
        text1="""*Hello, I'm Birthday Reminder Bot,*
I can remind birthday of your favourite ones,
Just share the bot with the one you need to remember their birthday of,
Bot will collect their birthday info and remind in group on their birthday,

To know more about bot usage 
[API Source Code](https://github.com/RorYin/BirthdayReminderTgBot)
[Bot Developped By RorYin](https://github.com/RorYin)

*Made with ❤️ In India*"""
        bot.sendPhoto(imgurl,text1,chat_id,msg_id,"Markdown")
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
        bot.sendPhoto(imgurl,txt1,chat_id,msg_id,"Markdown")
        return
    elif(text[:5]=="/join"):
        # Sending a link to collect his birthday
        url = f"https://roryin.pythonanywhere.com/newuser?id={chat_id}"
        bot.sendMsgTo(chat_id,url,msg_id,"Markdown")

    elif(text[:9]=="/checknow"):
        checkforbirthdays()

    else:
        bot.sendMsgTo(chat_id,"Please wait....",msg_id,"Markdown")
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
            bot.sendMsgTo(887572477,"Something went wrong in bot while getting updates",55,"Markdown")
            print("Something went wrong while getting updates")
            return Response("Ok",status=200)
            
        try:
            #get all normal text messages
            chat_id=msg['message']['chat']['id']
            text=msg['message']['text']
            message_id=msg['message']['message_id']
        except:
            # bot.sendMsgTo(887572477,"Something went wrong in bot while parsing json data",55,"Markdown")
            print("Something went wrong while parsing json data")
            return Response("Ok",status=200)
            

        if (text[0]=="/"):
                handlecommands(text,chat_id,message_id)
                return Response("Ok",status=200)
        else:
            handlecommands("/help",chat_id,message_id)
            return Response("Ok",status=200)

@app.route('/newuser',methods=['POST','GET'])
def newuser():
    query=request.args.get('id')
    return render_template("index.html",chatid=query)

@app.route('/register',methods=['POST','GET'])
def register():
    id = request.args.get('id')
    name = request.args.get('name')
    bday = request.args.get('bday')
    
    if(name == "" or bday == ""):
        return redirect("./registered?q=500")
    respcode = updatedata(name,bday,id)
    if(respcode == 200):
        return redirect("./registered?q=200")
    else:
        return redirect("./registered?q=500")

@app.route('/registered',methods=['POST','GET'])
def openpage():
    # if(request.args.get('q')==200):
    #     return render_template("registered.html",imgurl="Sucessfully Registered")
    # else:
    #     return render_template("registered.html",igmurl="Check all fields and try again")
    if(request.args.get('q')=='200'):
        
        return render_template("registered.html",imgurl="https://i.ibb.co/G9xrRHt/Registered.jpg")
    else:
        return render_template("notregistered.html",igmurl="https://i.ibb.co/XC6NKh0/Not-Registered.jpg")

if __name__ == '__main__':
    app.debug=True
    app.run()    