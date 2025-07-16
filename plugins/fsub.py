from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

CHANNEL_USERNAME = '@yourchannelusername'  # Replace with your channel

def start(update: Update, context: CallbackContext):
    user_id = update.effective_user.id
    member = context.bot.get_chat_member(chat_id=CHANNEL_USERNAME, user_id=user_id)
    if member.status in ['member', 'administrator', 'creator']:
        update.message.reply_text("Welcome! You have access.")
        # Proceed with your main bot logic
    else:
        update.message.reply_text(
            f"Please join our channel first: https://t.me/{CHANNEL_USERNAME.lstrip('@')}"
        )

updater = Updater('YOUR_BOT_TOKEN')
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.start_polling()
updater.idle()
