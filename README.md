> В данном репозитории собраны маленькие Telegram-скрипты, которыми я пользуюсь на постоянной основе

## Структура репозитория
- [`dinner.py`](https://github.com/ornaras/MiniBots/blob/main/dinner.py): выгружает дневное меню из ВК-страницы доставки обедов и отправляет в Telegram-группу
- [`keyrate_ru.py`](https://github.com/ornaras/MiniBots/blob/main/keyrate_ru.py): получает и отправляет текущую [ключевую ставку ЦБ РФ](https://www.cbr.ru/hd_base/keyrate/) в Telegram
- [`ping.py`](https://github.com/ornaras/MiniBots/blob/main/ping.py): отправляет сообщение в Telegram, при не доступности сервиса

## Настройка планировщика (/etc/crontab)
```
0 8 * * 1-5 root python3 dinner.py
0 15 * * 1-5 root python3 keyrate_ru.py
*/30 * * * * root python3 ping.py
```
