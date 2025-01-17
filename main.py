import requests
import json
import os
import platform
import time

file_path = 'token.txt'
user_file_path = 'token.txt'

banner = """
  ____  _                       _   _____            _       _ _   
 |  _ \(_)___  ___ ___  _ __ __| | | ____|_  ___ __ | | ___ (_) |_ 
 | | | | / __|/ __/ _ \| '__/ _` | |  _| \ \/ / '_ \| |/ _ \| | __|
 | |_| | \__ \ (_| (_) | | | (_| | | |___ >  <| |_) | | (_) | | |_ 
 |____/|_|___/\___\___/|_|  \__,_| |_____/_/\_\ .__/|_|\___/|_|\__|
                                              |_|                  
"""

def clear():
    sistema = platform.system()
    
    if sistema == "Linux" or sistema == "Darwin":  
        os.system('clear')
    elif sistema == "Windows":
        os.system('cls')

clear()

print(f"\033[38;2;117;117;248m{banner}\033[0m")
print("          \033[91mExploit:\033[0m \033[38;2;1;251;1mView hidden channels\033[0m")
print()

def is_file_empty(file_path):
    return os.path.getsize(file_path) == 0


if is_file_empty(file_path):
    token = input(" \033[93m[Token-Authorization]\033[0m Insert Token Bot > ")
    with open(user_file_path, 'w') as user_file:
        user_file.write(token)

with open(user_file_path, 'r') as user_file:
    token = user_file.read().strip()


print(f" \033[92m[!]\033[0m TOKEN >>> {token}")


clear()

print(f"\033[38;2;117;117;248m{banner}\033[0m")
print("          \033[91mExploit:\033[0m \033[38;2;1;251;1mView hidden channels\033[0m")
print()

guild_id = input(" \033[93m[SERVER-ID]\033[0m > ")
print()

token = f"{token}" 


urlchannels = f"https://discord.com/api/v10/guilds/{guild_id}/channels"
headers = {
    "Authorization": f"Bot {token}",
    "Content-Type": "application/json"
}


responsechannels = requests.get(urlchannels, headers=headers)

if responsechannels.status_code == 200:
    
    channels = responsechannels.json()
    categories = {}
    text_channels = []
    voice_channels = []


    for channel in channels:
        if channel['type'] == 4: 
            categories[channel['id']] = {
                'name': channel['name'],
                'channels': {
                    'text': [],
                    'voice': []
                }
            }
        elif channel['type'] == 0:  
            if channel.get('parent_id') in categories:
                categories[channel['parent_id']]['channels']['text'].append(channel['name'])
            else:
                text_channels.append(channel['name'])
        elif channel['type'] == 2:  
            if channel.get('parent_id') in categories:
                categories[channel['parent_id']]['channels']['voice'].append(channel['name'])
            else:
                voice_channels.append(channel['name'])

    

    
    for category_id, category_data in categories.items():
        print(f" {category_data['name']} [CATEGORY]")
        for text_channel in category_data['channels']['text']:
            print(f"  #{text_channel}")
        for voice_channel in category_data['channels']['voice']:
            print(f"  {voice_channel} [VOICE]")

    
    if text_channels:
        print("")
        for channel in text_channels:
            print(f"  #{channel}")

    
    if voice_channels:
        print("")
        for channel in voice_channels:
            print(f"  {channel} [VOICE]")

else:
    print(f"Failed: {responsechannels.status_code}")
    print(responsechannels.text)

# Code by github.com/Eltotiz