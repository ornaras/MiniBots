> В данном репозитории собраны маленькие Telegram-скрипты, которыми я пользуюсь на постоянной основе

## Структура репозитория
- [`dinner.py`](https://github.com/ornaras/MiniBots/blob/main/dinner.py): выгружает дневное меню из ВК-страницы доставки обедов и отправляет в Telegram-группу
- [`percent_bank.py`](https://github.com/ornaras/MiniBots/blob/main/percent_bank.py): получает и отправляет текущую [ключевую ставку ЦБ РФ](https://www.cbr.ru/hd_base/keyrate/) в Telegram

## Настройка планировщика (/etc/crontab)
```
0 8 * * 1-5 root python3 dinner.py
0 15 * * 1-5 root python3 percent_bank.py
```
