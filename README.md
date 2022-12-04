


![](https://raw.githubusercontent.com/RorYin/BirthdayReminderTgBot/main/Design.png)
<p align="center" >
![Adobe Photoshop](https://img.shields.io/badge/adobe%20photoshop-%2331A8FF.svg?style=for-the-badge&logo=adobe%20photoshop&logoColor=white)

![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

![Airtable](https://img.shields.io/badge/Airtable-18BFFF?style=for-the-badge&logo=Airtable&logoColor=white)

![Telegram](https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white) </p>
<p align="center">
![](https://img.shields.io/github/stars/RorYin/BirthdayReminderTgBot.svg) ![](https://img.shields.io/github/forks/RorYin/BirthdayReminderTgBot.svg) ![](https://img.shields.io/github/tags/RorYin/BirthdayReminderTgBot.svg) ![](https://img.shields.io/github/release/RorYin/BirthdayReminderTgBot.svg) ![](https://img.shields.io/github/issues/RorYin/BirthdayReminderTgBot.svg) 
</p>



**Table of Contents**

[TOCM]

# Features
+ Can remind and wish on birthdays in a group and in personal
+ Fun to use
+ Can add to any of your personal group and start using the bot withouth deploying
+ If interested you can try deploying your own using the open source code
+ currently deployed on pythonanywhere and railway

#Tips
+ Deploy on pythonanywhere and set the task for ScheduledTask.py to whatever time u want the bot to check and send update, currently it is set to 12AM for my deployed bot.

#ToDo
👁️_ To add multiple register from one telegram user, so that one can add his/her friends list to get reminder to him personally rather than in group(if needed so).
👁️ To add deregister functionality.
👁️ To add list registered user functionality.
👁️ And more, as per discussion in the [group](https://telegram.me/+gK3cgGhXuwIzMDJl)._



#ReleaseNote

> Currently V1.0 bot is deployed on railway, which might soon stop, will deploy to other services, if bot stops workin anytime, you can report the same in [TG group](https://telegram.me/+gK3cgGhXuwIzMDJl).

#Setup

+ Fork the repo
+ Edit the Setup.py
	+ Create a new TG Bot using BotFather, and copy the bot token and paste it.
	+ Create a Airtable Base, and a table, with fields as "Name", "Birthday", "id", "gid".
	+ Copy and paste the airtable api key, Base Id, Tabe Id, Table Name, refer airtable docs to know how to get it or ping on [TG group](https://telegram.me/+gK3cgGhXuwIzMDJl).
+ Choose your fav platform to deploy, recommended is pythonanywhere as it has a option to create tasks. Else you can find a way to run the ScheduledTask.py at particular time.
+ Once deployed, copy pase the webapp url into setup.py "appurl", save it and redeploy.
+ Webhook has to be set for the bot, for that just go to this url "https://api.telegram.org/botYOURBOTTOKEN/setWebhook?url=YOURWEBAPPURL" by replacing bot token and web app url with yours.
+ Edit your bot description, commands, botpic using BotFather.
+ Done, bot is ready to use, check with "/start" command.

#Airtable Guide
> Here is how to your airtable base and table should look like, here "Birthday" is the base name, and "V1Data" is the table name.
> 
![AirtableBase Example](https://raw.githubusercontent.com/RorYin/BirthdayReminderTgBot/main/AirtableBase.png)

<br>

#Deployed Bot Link
> Here is the Bot link one can readliy use without deploying there own, just add the bot to your group and start using..!
https://telegram.me/BirthdayReminderV1_bot



<br><br>
_Star the repo incase if you liked it...! 😊_
