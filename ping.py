ADDRESSES = [('8.8.8.8', 53, "Google DNS")]

from tcppinglib import tcpping
import requests
import os
import python_dotenv

python_dotenv.load_dotenv()

for addr in ADDRESSES:
  host = tcpping(addr[0], addr[1], 2, 4, 1)
  if host.is_alive:
    continue

  tg_body = {
      "chat_id": os.getenv("TELEGRAM_USERID"),
      "text": f"Сервис \"{addr[2]}\" не отвечает"
  }
  tg_url = f"https://api.telegram.org/bot{os.getenv('TELEGRAM_TOKEN')}/sendMessage"
  requests.post(tg_url, json=tg_body)
