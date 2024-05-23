import telebot
import time

# Токен бота, полученный от BotFather
TOKEN = 'YOUR_BOT_TOKEN'

# Создаем бота
bot = telebot.TeleBot(TOKEN)

# Функция для отправки сообщения
def send_message(chat_id, message):
    bot.send_message(chat_id, message)

# Функция для спама
def spam(chat_id, message, interval):
    while True:
        send_message(chat_id, message)
        time.sleep(interval)

# Получаем чат-ид из сообщения
@bot.message_handler(content_types=['text'])
def get_chat_id(message):
    chat_id = message.chat.id
    # Сообщение для спама
    spam_message = 'Спам-сообщение!'
    # Интервал спама в секундах
    spam_interval = 60  # 1 минута
    spam(chat_id, spam_message, spam_interval)

# Запуск бота
bot.infinity_polling()
