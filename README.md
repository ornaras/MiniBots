> В данном репозитории собраны маленькие Telegram-скрипты, которыми я пользуюсь на постоянной основе

## Структура репозитория
- [`dinner/`](https://github.com/ornaras/MiniBots/blob/main/dinner/main.py): выгружает дневное меню из ВК-страницы доставки обедов и отправляет в Telegram-группу
- [`keyrate_ru/`](https://github.com/ornaras/MiniBots/blob/main/keyrate_ru/main.py): получает и отправляет текущую [ключевую ставку ЦБ РФ](https://www.cbr.ru/hd_base/keyrate/) в Telegram

## Настройка планировщика (/etc/crontab)
```
0 8 * * 1-5 root python3 dinner/main.py
0 15 * * 1-5 root python3 keyrate_ru/main.py
```
