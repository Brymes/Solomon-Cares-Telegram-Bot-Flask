#!/usr/bin/env python3

# FIXME Detailed Example userStep[cid] = 1

from telebot import types

from extensions import bot
from bot.custom import (
    my_next_step_handler,
    process_name_entry,
    process_desc_entry,
    process_suggestion_entry
)

token = "1751532233:AAFBGtBcj51uHuS3DpwAdZxGZ6hjzll6rtM"
# bot = TeleBot(token=token)

markup = types.ReplyKeyboardMarkup(row_width=3)

registration_button = types.KeyboardButton('/registrations')
bot_tutorial_button = types.KeyboardButton('/bot_tut')
appointment_button = types.KeyboardButton('/appointment')
direct_entry_button = types.KeyboardButton('/direct_entry')

markup.add(registration_button)

# inline_keys = types.InlineKeyboardMarkup(row_width=2)


hideBoard = types.ReplyKeyboardRemove()

# FIXME random vars
txt = "Please Click this Button. After which you then Enter your name"


@bot.message_handler()
def payment_validation(message):
    pass


@bot.message_handler(commands=['start', 'help', 'cancel'])
def welcome(message):
    users_name = message.from_user.username
    bot.reply_to(
        message, f"Hi There, {users_name} Welcome to Solomon Cares.\n \
                Here is a list of commands you can give me to get started.\n\n \
                If you haven't used a telegram bot before, Please click this ►►: /bot_tut")
    bot.reply_to(
        message, "/start - start me up\n\
        /help - to get this menu\n \
        /registrations - To perform registrations, \n \
        /appointment - To Book an Appointment with Solomon Cares, \n \
        /others - Other miscellanous services e.g Submission of forms e.t.c.\n \
        If you need more explanations concerning our services please listen to the voice note below")

    audio = open('test.ogg', 'rb')
    bot.send_voice(chat_id=message.chat.id, voice=audio,
                   caption="Solomon Cares Welcome Message")

    bot.send_message(
        chat_id=message.chat.id, text="What do you want to do today 😁")
    # reply_markup=markup)
    del audio


@bot.message_handler(commands=['others'])
def others(message):
    bot.reply_to(
        message, "Kindly select from the list below the service you would like to use")
    bot.send_message(chat_id=message.chat.id,
                     text="This is Dummy Placeholder text.\n \
        /service1 - service \n\n \
        If you would like to request a separate service Please click this ►►: /req_svc .")


@bot.message_handler(commands=['req_svc'])
def request_service(message):
    msg = bot.reply_to(
        message, "Kindly Send a Descriptive Text, or a Voice note (not longer than 2 minutes) requesting the service you would require. We would get back to you shortly")

    bot.register_next_step_handler(msg, process_suggestion_entry)


@bot.message_handler(commands=['bot_tut'])
def bot_tutorial(message):
    bot.reply_to(message, 'Welcome to Solomon Cares Bot tutorial.\n To communicate with the bot please click the commands preceeded by a forward slash "/" As shown in the gif below. \n\n Please avoid sending messages directly to the Bot Unless prompted to. \n\n\n Now please proceed to start the bot by clicking this ►► : /start')
    video = open('test1.mp4', 'rb')
    bot.send_video_note(chat_id=message.chat.id, data=video)

# FIXME make this a button


@bot.message_handler(commands=['appointment'])
def appointments(message):
    msg = bot.reply_to(message, 'To book an appointment we would require your fullname and a short description of your purpose at our office.\n\n To proceed with booking an appointment click the button displayed \n',
                       reply_markup=my_next_step_handler(txt=txt))
    bot.register_next_step_handler(message=msg, callback=process_name_entry)

# FIXME
# Base functions to send documents
# Pictures


@bot.message_handler(commands=['enter_documents'])
@bot.message_handler(content_types=['photo', 'document'])
def accept_image_document(message):
    pass


@bot.message_handler(func=lambda message: True)
def error_handler(message):
    bot.send_message(
        message, 'You have sent a message directly to the bot.\n Please click /cancel to proceed')


bot.polling()
print("Bot Started")
