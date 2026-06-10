import os
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = os.environ.get("BOT_TOKEN")

logging.basicConfig(level=logging.INFO)

responses = {
    "ку": "вассап, че надо",
    "че надо": "нормас",
    "гудбай": "пока",
    "сяп": "не за что)",
}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("вассап, братишка")

async def handle(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()
    for word, answer in responses.items():
        if word in text:
            await update.message.reply_text(answer)
            return
    await update.message.reply_text("Не понял. Напиши 'помощь'")

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle))

if __name__ == "__main__":
    app.run_polling()
