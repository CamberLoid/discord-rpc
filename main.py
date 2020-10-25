## Discord-RPC/Studying.py [Camber's Fork]

## Todo 
## 1. 监听终端输入
## 2. Become Asynchronous
## 3. Build a GUI

import rpc
import time
from time import mktime
import json

time.sleep(5)
start_time = mktime(time.localtime())
activity = {
    "state": "睡觉",         # anything you like
    "details": "Sleeping",  # anything you like
    "timestamps": {
        "start": start_time
    },
    "assets": {
        "small_text": "Camber is Studying",  # anything you like
        "small_image": "nozomi_studying"  # must match the image key
        #"large_text": "Illustrator",  # anything you like
        #"large_image": "illustrator"  # must match the image key
    }
}

def main():
    print("Starting Camber's fork of Discord-RPC | Python")
    with open('./identities.json','r') as f:
        client_id = json.load(f).get('client_id')  # Your application's client ID as a string. (This isn't a real client ID)
    rpc_obj = rpc.DiscordIpcClient.for_platform(client_id)  # Send the client ID to the rpc module
    print("RPC connection successful.")
    print("Setting Status \nState = " + activity['state'] + '\nDetails='+activity.get('details'))
    try:
        while True:
            rpc_obj.set_activity(activity)
            time.sleep(30)
    except KeyboardInterrupt:
        print("Goodbye.")
        return
main()