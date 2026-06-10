import os
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = os.environ.get("BOT_TOKEN")
if not TOKEN:
    raise ValueError("BOT_TOKEN not found!")

logging.basicConfig(level=logging.INFO)

responses = {
    "привет": "вассап, мабой",
    "как дела": "нормас",
    "пока": "гудбай",
    "спасибо": "всегда пожалуйста",
    "как тебя зовут": "я собака, братан",
    "ты тупой": "прям как твой жирный отец"
}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Я бот!")

async def handle(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()
    for word, answer in responses.items():
        if word in text:
            await update.message.reply_text(answer)
            return
    await update.message.reply_text("Не понял. Напиши 'привет'")

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle))
    app.run_polling()

if __name__ == "__main__":
    main()
