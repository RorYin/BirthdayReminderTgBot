import time
import datetime
import requests
import json
from app import *
from logger import logger
from scheduledTask import *
from setup import *

# token = os.environ.get('token')  #production
bot=logger(token)

# To fetch the current date
currentdate = datetime.datetime.now().strftime("%d-%m")
# print(currentdate)

requrl = f"https://api.airtable.com/v0/appHXjkKNtDVs9aVm/Data/?api_key={airtablekey}"
headers = {'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"}


def gettoday():
    return (datetime.datetime.now())

def checkforbirthdays(gid):
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

            imgurl="https://pixabay.com/get/g0844b30093d900eea8021b5969c30f4c1d64af32dc20eefa813245698a95a17e5922238468ef8de4073e390aaa7ea2ba_640.jpg"
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
    Response = requests.get("https://api.airtable.com/v0/appHXjkKNtDVs9aVm/tblnRCTgqOA0n6qEB?fields%5B%5D=id",headers=headers).json()
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
    Response = requests.get("https://api.airtable.com/v0/appHXjkKNtDVs9aVm/tblnRCTgqOA0n6qEB?fields%5B%5D=gid",headers=headers).json()
    list = [ ]
    for i in Response['records'] :
        # print(i)

        if (i['fields']['gid'] not in list):
            list.append(i['fields']['gid'])
            checkforbirthdays(i['fields']['gid'])

    return

if __name__ == '__main__':
    dodaily()
    # testing()