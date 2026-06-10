import os
import logging
from flask import Flask, request
from telegram import Bot, Update
from telegram.ext import Dispatcher, CommandHandler, MessageHandler, filters

TOKEN = os.environ.get("BOT_TOKEN")
if not TOKEN:
    raise ValueError("BOT_TOKEN not found!")

logging.basicConfig(level=logging.INFO)
app = Flask(__name__)
bot = Bot(token=TOKEN)

# СБРАСЫВАЕМ ВЕБХУК ПРИ ЗАПУСКЕ (решает проблему Conflict)
bot.delete_webhook(drop_pending_updates=True)
print("Webhook сброшен!")

responses = {
    "привет": "Привет! Как дела?",
    "как дела": "У меня всё отлично!",
    "пока": "До свидания!",
    "спасибо": "Пожалуйста!",
}

async def start(update, context):
    await update.message.reply_text("Привет! Я бот! Напиши 'привет'")

async def handle_message(update, context):
    text = update.message.text.lower()
    for word, answer in responses.items():
        if word in text:
            await update.message.reply_text(answer)
            return
    await update.message.reply_text("Не понял. Напиши 'привет'")

dispatcher = Dispatcher(bot, None, use_context=True)
dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

@app.route(f'/{TOKEN}', methods=['POST'])
def webhook():
    update = Update.de_json(request.get_json(force=True), bot)
    dispatcher.process_update(update)
    return 'ok', 200

@app.route('/')
def health_check():
    return 'I am alive', 200

if __name__ == '__main__':
    # Устанавливаем вебхук заново
    webhook_url = f'https://my-telegram-bot-9byg.onrender.com/{TOKEN}'
    bot.set_webhook(webhook_url)
    print(f"Webhook установлен на {webhook_url}")
    
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
