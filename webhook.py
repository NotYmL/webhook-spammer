import time as sleep #import sleep
import requests      #import sleep

poruka = 'Kys Faggots'  #Set spam message

web_hooks = [
    "URL"       #List of webhooks
]

while 1:  #while 1 = 1
    for webhook in web_hooks: #for webhhok url in webhhoks list
        print(requests.post(webhook, json={'content': poruka})) #send message
        sleep(1)  #sleep 1s
