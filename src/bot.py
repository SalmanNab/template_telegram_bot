import os

import emoji
import telebot
from loguru import logger

from src.constants import create_keyboard, keyboards
# from src.utils.io import write_json


class Bot:
    """
    Template for telegram not
    """
    def __init__(self):
        self.bot = telebot.TeleBot(os.environ['NASHENAS_BOT_TOKEN'])
        self.echo_all = self.bot.message_handler(
            func=lambda message:True
        )(self.echo_all)

    def run(self):
        logger.info('Bot running...')
        self.bot.infinity_polling()

    def echo_all(self, message):
        # print(message.text)
        # write_json(message.json, 'message.json')
        # self.bot.reply_to(message, message.text)
        # self.bot.send_message(message.chat.id, message.text)
        self.bot.send_message(
            message.chat.id, message.text,
            reply_markup=keyboards.main,
            # reply_markup=create_keyboard(message.chat.first_name),
        )

if __name__ == '__main__':
    logger.info('Bot started')
    bot = Bot()
    bot.run()




# bot = telebot.TeleBot(os.environ['NASHENAS_BOT_TOKEN'])

# @bot.message_handler(commands=['start', 'help'])
# def send_welcome(message):
# 	bot.reply_to(message, "I love you talkhoon!")
#     # bot.reply_to(message, "Howdy, how are you doing?")

# @bot.message_handler(func=lambda m: True)
# def echo_all(message):
# 	# bot.reply_to(message, message.text)
#     # bot.reply_to(message, str(;enmessage.text)))
#     bot.reply_to(message, str(eval(message.text)))

# logger.info('Bot started')
# bot.infinity_polling()
# logger.info('Done')

