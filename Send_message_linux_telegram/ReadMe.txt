To send message from Linux machine to Telegram chennal with python:
1) Need to create Bot, and get its "TOKEN" like "6397487705:AAGun0CNt2MCwrHoFc7MHOtWPdolz9j4nlM"
2) Create channel and add your Bot as a admin to the chennel (bot will write message behalf of the Linux machine)
3) Get Channal ID
3.1) Change  <YourBOTToken> https://api.telegram.org/bot<YourBOTToken>/getUpdates
3.2) But https://api.telegram.org/bot<YourBOTToken>/getUpdates  to Browser
3.3) Send message into the chennel from your phone APP and you can get chennel ID there
This is useful link:
https://bogomolov.tech/Telegram-notification-on-SSH-login/
https://linuxtech.in/how-to-send-alerts-and-notifications-with-telegram/




Code example with python
######################################################################################################################################################
import os
import requests

IPs = os.popen("cat dev.zalo.ai.access.log | egrep `date '+%H:[0-59]'` | awk '{print $1}'").read()
#IPs = os.popen("egrep \"$(date '+%d/%b/%Y:%H')\" /data/log/dev.zalo.ai.access.log | awk '{print $1}'").read()
IPs = IPs.split()
#print(IPs)
occurrence = {IP: IPs.count(IP) for IP in IPs}
print(occurrence)
for key, value in occurrence.items():
    if (value > 10):
        msg = "DoS WARNING: Suspicious requests from {}, sending {} requests over the last 1 hour".format(key,value)
        ######################################################################################################################################################
        url = 'https://api.telegram.org/bot6397487705:AAGun0CNt2MCwrHoFc7MHOtWPdolz9j4nlM/sendMessage' # This is bot token
        headers = {'Content-type': 'application/json'}
        #data = {"chat_id": "6972452293", "text": msg}
        data = {"chat_id": "-1002073547571", "text": msg} # -1002073547571 this is Chat or Channel ID
        request = requests.post(url, headers= headers, json = data)
        print(msg)

######################################################################################################################################################
