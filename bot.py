import os

# ВРЕМЕННАЯ ПРОВЕРКА (потом удалите эти строки)
bot_token = os.environ.get("BOT_TOKEN")
print(f"1. Токен, который видит программа: [{bot_token}]")
print(f"2. Длина токена: {len(bot_token) if bot_token else 0} символов")
print(f"3. Тип переменной: {type(bot_token)}")
# КОНЕЦ ВРЕМЕННОЙ ПРОВЕРКИ

# Дальше идет ваш основной код с Application и т.д.
