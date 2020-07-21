import requests
import time
import yaml
import json
from slack import WebClient
import os


TOKEN = os.environ['SLACKTOKEN']
web_client = WebClient(TOKEN)

with open('subscriptions.yml', 'r') as f:
    userconfigs = yaml.safe_load(f)

tags = {}
for i in userconfigs:
    for j in i['tags']:
        if tags.get(j):
            tags[j].append(i['slackuserid'])
        else:
            tags[j] = [i['slackuserid']]

BASE_URL = 'https://www.ozbargain.com.au'
API_URL = '/api/live'

ts = int(time.time())
params = {
    'last': ts,
    'disable': 'comments,votes,wiki',
    'types': 'Comp,Forum'
}


def sendSlack(title, link, userid):
    for user in userid:
        try:
            response = web_client.chat_postMessage(channel=user, text=f"Item: {title}\n\nLink: {BASE_URL+link}")
        except:
            with open('error.log', 'w') as f:
                f.write(f"Error: {title}, {link}, {user}")
        if response.status_code != 200:
            with open('error.log', 'w') as f:
                f.write(str(response.data))


print("Ozb monitoring starting...")
while True:
    d = requests.get(BASE_URL+API_URL, params=params)
    try:
        p = d.json()
    except:
        with open('error.log', 'w') as f:
            f.write(d.text)
    if p['records']:
        for i in p['records']:
            title = i['title'].lower()
            matches = list({x for x in tags.keys() if x in title})
            if matches:
                sendaddrs = tags[matches[0]]
                sendSlack(i['title'], i['link'], sendaddrs)
            print(i['title'])
            params['last'] = max(i['timestamp'], params['last'])
        with open('log.log', 'a') as f:
            f.write(json.dumps(p)+'\n')
    time.sleep(60)
