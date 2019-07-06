from glob import glob
import logging
from random import choice

from utils import get_keyboard, get_user_emo

def greet_user(bot, update, user_data):
    emo = get_user_emo(user_data)
    #user_data['emo'] = emo уже не нужно
    text = 'Привет {}'.format(emo)
    update.message.reply_text(text, reply_markup=get_keyboard())

def send_cat_picture(bot, update, user_data):
    cats_list = glob('cats_images/*cat*.jp*g')
    cat_pic = choice(cats_list)
    bot.send_photo(chat_id=update.message.chat_id, photo = open(cat_pic, 'rb'), reply_markup=get_keyboard())

def talk_to_me(bot, update, user_data):
    emo = get_user_emo(user_data)
    user_text = "Hello {} {}! You wrote: '{}'.".format(update.message.chat.first_name, emo, update.message.text)
    logging.info("User: %s, chat id: %s, Message: %s",
                update.message.chat.username,
                update.message.chat.id,
                update.message.text
                )
    update.message.reply_text(user_text, reply_markup=get_keyboard())

def change_avatar(bot, update, user_data):
    if 'emo' in user_data:
        del user_data['emo']
    emo = get_user_emo(user_data)
    update.message.reply_text('Готово {}'.format(emo), reply_markup=get_keyboard())

def get_contact(bot, update, user_data):
    print(update.message.contact)
    update.message.reply_text('Готово {}'.format(get_user_emo(user_data), reply_markup=get_keyboard()))

def get_location(bot, update, user_data):
    print(update.message.location)
    update.message.reply_text('Готово {}'.format(get_user_emo(user_data), reply_markup=get_keyboard()))