from bs4 import BeautifulSoup
import requests
import time
import os
import json
import math
from colorama import Fore, Back, Style

class kd:
    r = Fore.RESET
    s = Fore.LIGHTGREEN_EX
    u = Fore.BLUE
    e = Fore.RED

tumblrUser = input(f"What user would you like to monitor? {kd.u}")
tumblerUrl = f"https://{tumblrUser}.tumblr.com/rss"

print(f"{kd.r}Attempting to monitor: {kd.s+tumblerUrl+kd.r}")

#
# Use the old tumblrUser track logs. If the file doesn't exist,
# then you use a new file. If no, override the old tracking logs.
#
while True:
    useOldTrack = input(f"\nDo you wish to use old data in {kd.s+tumblrUser}.txt{kd.r}? (y/n) {kd.u}")
    if((useOldTrack != "y") and (useOldTrack != "n")):
        print(f"{kd.e}Please say y or n.{kd.r}")
    if((useOldTrack == "y") or (useOldTrack == "n")):
        break

dataFile = f"{tumblrUser}.txt"
data = open(dataFile, "a")
data.close()
if(useOldTrack != "y"):
    data = open(dataFile, "w")
    data.write("")
    data.close()
data = open(dataFile, "r").read()

#
# Ping everyone area
#
while True:
    usePing = input(f"\n{kd.r}Do you want to ping everyone? (y/n) {kd.u}")
    if((usePing != "y") and (usePing != "n")):
        print(f"{kd.e}Please say y or n.{kd.r}")
    if((usePing == "y") or (usePing == "n")):
        break

#
# Discord Webhook Integration
#
while True:
    useWebhook = input(f"\n{kd.r}Do you wish to log these to a Discord webhook? (y/n) {kd.u}")
    if((useWebhook != "y") and (useWebhook != "n")):
        print(f"{kd.e}Please say y or n.{kd.r}")
    if((useWebhook == "y") or (useWebhook == "n")):
        break
if(useWebhook == "y"):
    webhookUrl = input(f"{kd.r}What is the webhook URL? {kd.u}")
    print(f"{kd.r}Using webhook: {kd.s+webhookUrl+kd.r}.\n\n")

def postToDiscord(uid, title, desc):
    username = f"{tumblrUser} ({uid})"
    ping = ""
    if(usePing == "y"):
        ping = "-# ||@everyone||"
    if(title != desc):
        message = f"## {title}\n{desc}\n{ping}"
    else:
        message = f"{desc}\n{ping}"
    data = {"content": message, "username": username}
    try:
        response = requests.post(webhookUrl, data=json.dumps(data), headers={"Content-Type": "application/json"})
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error sending message: {e}")
        time.sleep(5)
        postToDiscord(uid, title, desc)


#
# Main area
#
previous_listings = {}
pt = open(f"{tumblrUser}.txt", "r")
previous_track = pt.read()

while True:
    r = requests.get(tumblerUrl)
    soup = BeautifulSoup(r.text, 'xml')
    
    listings = soup.find_all('item')[::-1]
    terminal_size = os.get_terminal_size()
    text_width = terminal_size.columns
    new_listings = 0
    for listing in listings:
        
        title = str(listing.find('title').text)
        desc = str(listing.find('description').text)
        uid = str(listing.find('guid').text).replace(f"https://www.tumblr.com/{tumblrUser}/", "")
        
        title = title \
            .replace("&hellip;", "...") \
            .replace("</p><p>", "\n\t") \
            .replace("<p>", "") \
            .replace("</p>", "") \
            .replace("&ldquo;", "\"") \
            .replace("&rdquo;", "\"")
        desc = desc \
            .replace("</p><p>", "\n\t") \
            .replace("<p>", "") \
            .replace("</p>", "") \
            .replace("&ldquo;", "\"") \
            .replace("&rdquo;", "\"")
        
        if(uid in data):
            continue
        else:
            previous_listings.update({uid: {
                "guid":uid, 
                "title":title, 
                "description":desc
            }})
            f = open(f"{tumblrUser}.txt", "a")
            f.write(uid+"\n")
            f.close()

            print("Title: "+title)
            print("Description: "+desc)
            print("UID: "+uid)
            print("="*text_width)
            
            new_listings = new_listings + 1
            # DISCORD
            try:
                postToDiscord(uid, title, desc)
            except Exception as e:
                print(f"Error sending message: {e}")
                time.sleep(5)
                postToDiscord(uid, title, desc)
    
    tick_msg = f" [Tick] {new_listings} new posts [Tick] "
    tick_width_left = math.ceil((text_width - len(tick_msg)) / 2)
    tick_width_right = math.floor((text_width - len(tick_msg)) / 2)
    print(("-"*tick_width_left)+tick_msg+("-"*tick_width_right))
    
    time.sleep(30)