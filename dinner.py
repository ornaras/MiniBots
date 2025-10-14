import requests
import json
import dotenv
import os

dotenv.load_dotenv()

vk_header = {
        "Authorization": f"Bearer {os.getenv('VK_TOKEN')}"
}
vk_url = "https://api.vk.ru/method/wall.get?domain=vremya_obedat18&count=1&v=5.199"
vk_post = requests.get(vk_url, headers=vk_header)
vk_json = json.loads(vk_post.content)
attachments = vk_json["response"]["items"][0]["attachments"]

tg_body = {
    "chat_id": os.getenv("TELEGRAM_DINNER_GROUPID"),
    "photo": ""
}
for attach in attachments:
  if attach["type"] == "photo":
    tg_body["photo"] = attach["photo"]["orig_photo"]["url"]
    break
tg_url = f"https://api.telegram.org/bot{os.getenv('TELEGRAM_TOKEN')}/sendPhoto"
requests.post(tg_url, json=tg_body)
