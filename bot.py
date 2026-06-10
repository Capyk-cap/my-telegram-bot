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
    "ты тупой": "прям как твой жирный отец",
    "пошел нахуй": "кусай захуй",
    "какая сейчас погода": "хз",
    "ты человек": "нет, я собака",
    "что ты любишь": "отвечать таким ебланам как ты",
    "ты собака": "подумай"
}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
