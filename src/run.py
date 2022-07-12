# import os

import emoji
# import telebot
from loguru import logger

from src.constants import create_keyboard, keyboards
# from src.utils.io import write_json
from src.filters import IsAdmin
from src.bot import bot


class Bot:
    """
    Template for telegram not
    """
    def __init__(self, telebot):
        # self.bot = telebot.TeleBot(os.environ['NASHENAS_BOT_TOKEN'])
        self.bot = telebot
        # self.echo_all = self.bot.message_handler(
        #     func=lambda message:True
        # )(self.echo_all)

        # add mustom filter
        self.bot.add_custom_filter(IsAdmin())

        # register handler
        self.handlers()


    # def run(self):
    # run bot
        logger.info('Bot running...')
        self.bot.infinity_polling()

    def handlers(self):
        @self.bot.message_handler(is_admin=True)
        def admin_of_group(message):
            # self.bot.send_message(message.chat.id, 'You are admin of this group')
            # self.bot.send_message(message.chat.id, '<strong> You are admin of this group! </strong>')
            self.send_message(message.chat.id, '<strong> You are admin of this group! </strong>')

        @self.bot.message_handler(func=lambda _:True)
        def echo(message):
            # self.bot.send_message(
                self.send_message(
                message.chat.id, message.text,
                reply_markup=keyboards.main
            )

    def send_message(self, chat_id, text, reply_markup=None, emojize=True):
        """
        Send message to telegram bot.
        """
        if emojize:
            text = emoji.emojize(text, language='alias')
            # text = emoji.emojize(text, use_aliases=True)

        self.bot.send_message(chat_id, text, reply_markup=reply_markup)
    # def echo_all(self, message):
        # print(message.text)
        # write_json(message.json, 'message.json')
        # self.bot.reply_to(message, message.text)
        # self.bot.send_message(message.chat.id, message.text)
        # self.bot.send_message(
        #     message.chat.id, message.text,
        #     reply_markup=keyboards.main,
            # reply_markup=create_keyboard(message.chat.first_name),
        #)

if __name__ == '__main__':
    logger.info('Bot started')
    # bot = Bot()
    # bot.run()
    nashenas_bot = Bot(telebot=bot)
    nashenas_bot.run()




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

