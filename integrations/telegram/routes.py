from flask import Blueprint, request, jsonify
import os
from telegram import Bot, Update
from telegram.ext import Dispatcher, CommandHandler, MessageHandler, filters

telegram_bp = Blueprint('telegram', __name__)
TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
bot = Bot(token=TELEGRAM_BOT_TOKEN)
dispatcher = Dispatcher(bot=bot, update_queue=None, workers=0, use_context=True)

# Example command handler
def start(update, context):
    update.message.reply_text('Welcome to Nubi Telegram Integration!')

dispatcher.add_handler(CommandHandler('start', start))

@telegram_bp.route('/telegram/webhook', methods=['POST'])
def telegram_webhook():
    if request.method == 'POST':
        update = Update.de_json(request.get_json(force=True), bot)
        dispatcher.process_update(update)
        return 'ok'

@telegram_bp.route('/telegram/send', methods=['POST'])
def send_message():
    data = request.json
    chat_id = data['chat_id']
    text = data['text']
    bot.send_message(chat_id=chat_id, text=text)
    return jsonify({'status': 'sent'})
