from telegram import Update
from telegram.ext import (
    ApplicationBuilder, CommandHandler,MessageHandler, ContextTypes,
    filters
)

from translate import Translator
import os
os.system("cls")

def tarjimon(text):
    try:
        to = text.split()[0].lower()
        translator = Translator(to_lang=to)
        res =  translator.translate(text[len(to):])
        print("Tarjima qilindi:", res)
    except:
        res = "Tarjima qilishda xatolik"
        print(res)
    return res


async def translate(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    enterence = f"{update.message.from_user.first_name}'dan matn kiritildi: {update.message.text}\n"
    with open("kiritishlar.log", "a") as file:
        file.write(enterence)
    res = tarjimon(update.message.text)
    await update.message.reply_text(f"Tarjimasi: {res}")

TOKEN = "8993779439:AAGrtw-BNH9Jbnz9o5KAi8ZQLg7UVyRkWRI"
app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(MessageHandler(filters.Text(), translate))

print("Bot ishga tushdi...")
app.run_polling()