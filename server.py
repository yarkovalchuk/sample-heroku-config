from time import sleep

while True:
    print("Tick!")
    sleep(10)
    print("Tack!")
    sleep(10)

import requests
from handler import handle_message

while True:
    res =requests.get("https://api.telegram.org/bot344998733:AAF0R901Ilq43PH-MSYAnoDHMYrh5yaK3eg/getUpdates")
    d = res.json()
    for elem in d["result"]:
        text = elem["message"]
        ans =  handle_message(text)
        chat_id = elem["message"]["chat"]["id"]
        requests.post("URL", params={"chat_id": chat_id, "text": text} )
