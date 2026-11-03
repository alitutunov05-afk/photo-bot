import os
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

TOKEN = os.getenv("BOT_TOKEN")

def start(update: Update, context: CallbackContext):
    keyboard = [
        ["📸 Заказать фото"],
        ["💰 Цены", "🖼 Примеры работ"],
        ["👨‍💻 Оператор"]
    ]
    update.message.reply_text(
        "Привет! Добро пожаловать в онлайн-фотоателье.\nВыбери нужный пункт:",
        reply_markup=ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    )

def order(update: Update, context: CallbackContext):
    update.message.reply_text("📸 Отправь фотографию и напиши, какую форму или одежду нужно добавить.")

def prices(update: Update, context: CallbackContext):
    update.message.reply_text("💰 Стоимость обработки фотографии — от 300 ₽.")

def examples(update: Update, context: CallbackContext):
    update.message.reply_text("🖼 Примеры работ скоро появятся здесь.")

def operator(update: Update, context: CallbackContext):
    update.message.reply_text("👨‍💻 Напиши свой вопрос. Оператор скоро ответит.")

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.regex("^📸 Заказать фото$"), order))
    dp.add_handler(MessageHandler(Filters.regex("^💰 Цены$"), prices))
    dp.add_handler(MessageHandler(Filters.regex("^🖼 Примеры работ$"), examples))
    dp.add_handler(MessageHandler(Filters.regex("^👨‍💻 Оператор$"), operator))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
