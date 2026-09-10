from telegram import Update 
from telegram.ext import Application, CommandHandler, ContextTypes,MessageHandler,filters
import env

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(update.effective_user)

    first_name = update.effective_user.first_name
    last_name = update.effective_user.last_name

    if last_name == None:
        last_name = ""

    reply_text = update.message.reply_text(f"Assalomu alaykum, {first_name} {last_name}")
    await reply_text

async def about(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Biz ipeschool o'qituvchilarimiz!")

async def get_help(update: Update, context: ContextTypes.DEFAULT_TYPE):

    help_text = f"""
Botimizda 3 ta buyruq mavjud:
1. /start - Botni ishga tushuradi
2. /about - Biz haqimizda malumot beradi
3. /help - Yordam

Meneger bilan bog'lanish uchun: +998500104307
telegram: https://t.me/Akmal1985_And_Feruzbek2013
"""
    await update.message.reply_text(help_text)

async def get_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    print(text)
    await update.message.reply_text(f"Siz yozgan matn \n\n {text}")

async def get_photo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    photo = update.message.photo[-1]  
    photo_id = photo.file_id
    file = await context.bot.get_file(photo_id)
    file_path = f"photos/{photo_id}.jpg"
    await file.download_to_drive(file_path)
    await update.message.reply_photo(photo_id)

app = Application.builder().token(env.BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("about", about))
app.add_handler(CommandHandler("help", get_help))
app.add_handler(MessageHandler(filters.TEXT, get_text))
app.add_handler(MessageHandler(filters.PHOTO, get_photo))

print("Bot ish tushdi...")
app.run_polling()
