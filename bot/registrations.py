from telebot import types

from extensions import bot
from bot.custom import my_next_step_handler


@bot.message_handler(commands=['registrations'])
def regs(message):
    bot.reply_to(
        message, "Kindly Select the registration you would like to perform from the ones below"
    )
    bot.send_message(
        chat_id=message.chat.id, text="/jamb_reg - Jamb Registration\n/de_reg - Direct Entry Registration")


@bot.message_handler(commands=['jamb_reg'])
def jamb_reg(message):
    bot.reply_to(message, "This is a placeholder Text that would be changed")


@bot.message_handler(commands=['de_reg'])
def de_reg(message):
    bot.reply_to(message, "The process for DE registration is as follows:\n\n \
        Provided that you have written the JUPEB exam and you already have your Statement of Result.\n\n \
        Below is a Voice recording explaining requirements and process of DE registration to University of Lagos ")

    audio = open('test.ogg', 'rb')
    bot.send_voice(chat_id=message.chat.id, voice=audio,
                   caption="Solomon Cares Welcome Message")
    msg = bot.send_message(chat_id=message.chat.id,
                           text=f"To Proceed with registrations, We would require a few things: \n\n \
                        1. Jupeb Statement of Result, \n \
                        2. O Level Result(WASSCE or SSCE), \n \
                        3. Jamb Direct Entry Acknowledgemnt Slip, \n \
                        4. Your personal details to be filled via a google form link that would be sent in subsequent steps \n\n \
                        Lastly a fee.Breakdown is as follows: \n \
                            ₦ 2000 --  Unilag Direct Entry Form \n \
                            ₦ 500  -- Remitta Charges \n \
                            ₦ 1000 - -Solomon Cares Service Charge \n\n \
                        We could also assist you with submitting these documents.\n The option would be displayed later if you so desire. \n\n \
                        To proceed with payment Please Click the button below ↓ ::: Or otherwise click ►►: /cancel", reply_markup=my_next_step_handler(txt=txt))
    # FIXME bot.register_next_step_handler(message=msg, callback=)
