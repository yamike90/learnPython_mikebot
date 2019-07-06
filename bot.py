import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, RegexHandler, Filters

from handlers import greet_user, send_cat_picture, change_avatar, get_contact, get_location, talk_to_me
import settings

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level = logging.INFO,
                    filename = 'bot.log'
                    )

def main():
    mikebot = Updater(settings.TG_API_KEY, request_kwargs = settings.PROXY)

    logging.info('Bot is starting')

    dp = mikebot.dispatcher

    dp.add_handler(CommandHandler('start', greet_user, pass_user_data=True))
    dp.add_handler(CommandHandler('cat', send_cat_picture, pass_user_data=True))

    dp.add_handler(RegexHandler('^(Прислать котика)$', send_cat_picture, pass_user_data=True))
    dp.add_handler(RegexHandler('^(Сменить аватарку)$', change_avatar, pass_user_data=True))

    dp.add_handler(MessageHandler(Filters.contact, get_contact, pass_user_data=True))
    dp.add_handler(MessageHandler(Filters.location, get_location, pass_user_data=True))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me, pass_user_data=True))

    mikebot.start_polling()
    mikebot.idle()

if __name__ == "__main__":
    main()
