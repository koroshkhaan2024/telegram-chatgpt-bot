import os
import openai
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

# گرفتن توکن‌ها از محیط
TELEGRAM_TOKEN = os.getenv("7677443612:AAF8v5RlE-VYfqXZUxzKxBNYOOU_umgbWIQ")
OPENAI_API_KEY = os.getenv("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")

openai.api_key = OPENAI_API_KEY

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("سلام! من ربات ChatGPT هستم. پیام بده باهات حرف بزنم.")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # یا مدل دیگه مثل gpt-4
            messages=[{"role": "user", "content": user_message}]
        )
        bot_reply = response.choices[0].message.content.strip()
        await update.message.reply_text(bot_reply)
    except Exception as e:
        await update.message.reply_text("خطا در پاسخ‌دهی. لطفاً بعداً امتحان کن.")
        print(e)

if __name__ == "__main__":
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.run_polling()
