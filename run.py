from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from dotenv import load_dotenv
import os

load_dotenv()
TOKEN=os.getenv('TOKEN')
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Ola kazveli!")

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler('start', start))

app.run_polling()