TELEGRAM_CHATID = 0
TELEGRAM_TOKEN = ""

import requests
from bs4 import BeautifulSoup
from datetime import datetime


def send_message(text: str):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    data = {
        "chat_id": TELEGRAM_CHATID,
        "text": text
    }
    requests.post(url, json=data)
    

cbr_resp = requests.get("https://www.cbr.ru/hd_base/keyrate/")
if(cbr_resp.status_code != 200):
    send_message(f"Не удалось получить ключевую ставку ЦБ РФ (Статус код: {cbr_resp.status_code})")
cbr_bs = BeautifulSoup(cbr_resp.content, 'lxml')
curr_procent = cbr_bs.find_all("td")[1].text
send_message(f"Ключевая ставка ЦБ РФ (на {datetime.now().strftime('%d-%m-%Y')}): {curr_procent}%")
