from time import sleep



import requests
from handler import handle_message

while True:
    res = requests.get("https://api.telegram.org/bot468389348:AAFk47PMcPIsE_2B5eukGpFUC2CWCGWzdKc/getUpdates")
    d = res.json()
    print(d)
    
    for elem in d["result"]:
        text = elem["message"]
        print(text)
        ans = handle_message(text)
        print(">>>", ans)
        chat_id = elem["message"]["chat"]["id"]
        requests.post("https://api.telegram.org/bot468389348:AAFk47PMcPIsE_2B5eukGpFUC2CWCGWzdKc/sendMessage", params={"chat_id": chat_id, "text": ans} )
