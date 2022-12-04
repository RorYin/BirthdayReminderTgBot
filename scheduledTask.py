import time
import datetime
import requests
import json
from app import *
from logger import logger
from scheduledTask import *
from setup import *
import pytz

# token = os.environ.get('token')  #production
bot=logger(token)

# To fetch the current date
dt_today = datetime.datetime.today()
currentdate = dt_India = dt_today.astimezone(pytz.timezone('Asia/Kolkata')).strftime("%d-%m")
# print(currentdate)

requrl = f"https://api.airtable.com/v0/{BaseId}/{TableName}/?api_key={airtablekey}"
headers = {'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"}


def gettoday():
    return(dt_today.astimezone(pytz.timezone('Asia/Kolkata')))

def checkforbirthdays(gid):
    requrl = f"https://api.airtable.com/v0/{BaseId}/{TableName}/?api_key={airtablekey}"
    headers = {'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"}
    dt_today = datetime.datetime.today()
    currentdate = dt_India = dt_today.astimezone(pytz.timezone('Asia/Kolkata')).strftime("%d-%m")
    response = requests.get(requrl,headers).json()
    count=0
    for i in response['records']:

        fetcday = i['fields']['Birthday']
        fetcday = fetcday.split("-")
        fetcday = fetcday[2]+"-"+fetcday[1]

        fetchgid = str(i['fields']['gid'])
        #Check if birthday of anyone is today
        if currentdate == fetcday and fetchgid==str(gid):
            # Generate wishes and send a POST request to TG
            # print(fetcday)
            messageToSend = f"""Happy Birthday [{i['fields']['Name']}](tg://user?id={i['fields']['id']})
Have a great day and year ahead
            """
            messageToSend2 = f"""Happy Birthday *{i['fields']['Name']}*
Have a great day and year ahead
            """

            imgurl="https://i.ibb.co/SBZKVkt/Wish2.png"
            resp = bot.sendPhoto(imgurl,messageToSend,i['fields']['gid'],000,"Markdown")
            if(i['fields']['gid'] != i['fields']['id']):
                resp = bot.sendPhoto(imgurl,messageToSend2,i['fields']['id'],000,"Markdown")
            count = count+1
    if(count <1):
        bot.sendMsgTo(gid,"Unfortunately no one's birthday today.....",000,"Markdown")
    return

def testing():
    headers = {
        'Authorization': f'Bearer {airtablekey}',
        # Already added when you pass json= but not when you pass data=

    }
    Response = requests.get(f"https://api.airtable.com/v0/{BaseId}/{TableId}?fields%5B%5D=id",headers=headers).json()
    print(Response)
    flag = 0
    for i in Response['records'] :
        # print(i)
        if 235666 == i['fields']['id']:
            print(i['fields']['id'])
            flag = 1
            break
    if(flag == 0):
        return

def dodaily():
    headers = {
        'Authorization': f'Bearer {airtablekey}',
        # Already added when you pass json= but not when you pass data=

    }
    Response = requests.get(f"https://api.airtable.com/v0/{BaseId}/{TableId}?fields%5B%5D=gid",headers=headers).json()
    list = [ ]
    for i in Response['records'] :
        # print(i)

        if (i['fields']['gid'] not in list):
            list.append(i['fields']['gid'])
            checkforbirthdays(i['fields']['gid'])

    return

if __name__ == '__main__':
    dodaily()
    