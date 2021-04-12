from telebot import types

from extensions import bot


def my_next_step_handler(txt):
    name_entry = types.InlineKeyboardMarkup(row_width=2).add(
        types.InlineKeyboardButton(txt))

    return name_entry


def process_name_entry(message):
    try:
        # FIXME
        chat_id = message.chat.id
        name = message.text
        if name.isalpha() is False:
            msg = bot.reply_to(
                message, 'Name should contain only Alphabets')
            bot.register_next_step_handler(msg, process_name_entry)
            return
        # FIXME user = User(name)
        # FIXME user_dict[chat_id] = user

        msg = bot.reply_to(
            message, "Please enter a short Description of why you would like to meet us.")
        bot.register_next_step_handler(msg, process_desc_entry)
    except Exception as e:
        bot.reply_to(message, f'oooops This occured : {e}')


def process_desc_entry(message):
    try:
        chat_id = message.chat.id
        desc = message.text

        # FIXME user = user_dict[chat_id]
        # FIXME user.description = desc
        bot.reply_to(
            message, "Information Succesfully Recieved.\n\n \
                You would be contacted via this bot with a date and location of our office")

    except Exception as e:
        bot.reply_to(message, f'oooops This occured : {e}')


@bot.message_handler(content_types=['text', 'audio', 'voice', 'document'])
def process_suggestion_entry(message):
    try:
        chat_id = message.chat.id
        if message.content_type == "document":
            print(message.document)
            print(message.document.file_id)
            # FIXME suggestions[chat_id] = bot.get_file(message.document.file_id)

            # FIXME
            # file_info = bot.get_file(message.voice.file_id)
            # downloaded_file = bot.download_file(file_info.file_path)
        elif message.content_type == "voice":
            # FIXME
            # file_info = bot.get_file(message.voice.file_id)
            # downloaded_file = bot.download_file(file_info.file_path)

            # FIXME suggestions[chat_id] = bot.get_file(message.voice.file_id)
            print(message.voice.file_id)
        elif message.content_type == "text":
            pass
            # FIXME suggestions[chat_id] == message.text
        elif message.content_type == "audio":
            print(message.audio.file_id)
            # FIXME suggestions[chat_id] = bot.get_file(message.audio.file_id)
    except Exception as e:
        bot.reply_to(message, f'oooops This occured : {e}')
