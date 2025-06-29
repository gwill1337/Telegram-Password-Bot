import telebot
from telebot import types
import secrets

bot = telebot.TeleBot("bot's API")

@bot.message_handler(commands=['start'])
def password(message):
    markup = types.InlineKeyboardMarkup()

    btn1 = types.InlineKeyboardButton("8", callback_data="8")
    btn2 = types.InlineKeyboardButton("16", callback_data="16")
    btn3 = types.InlineKeyboardButton("32", callback_data="32")
    btn4 = types.InlineKeyboardButton("My GitHub", url="https://github.com/gwill1337")
    btn5 = types.InlineKeyboardButton("other", callback_data="other")
    markup.row(btn1, btn2, btn3)
    markup.row(btn4, btn5)
    user = message.chat.first_name or "user"
    bot.send_message(message.chat.id, f'Welcome {user}, you can generate password below with 8/16/32 symbols, or follow my GitHub.', reply_markup=markup)

@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    bot.answer_callback_query(callback.id)
    if callback.data == "8":
        bot.send_message(callback.message.chat.id, gen_password(8))

    elif callback.data == "16":
        bot.send_message(callback.message.chat.id, gen_password(16))

    elif callback.data == "32":
        bot.send_message(callback.message.chat.id, gen_password(32))

    elif callback.data == "8on":
        bot.send_message(callback.message.chat.id, only_numbers(8))

    elif callback.data == "16on":
        bot.send_message(callback.message.chat.id, only_numbers(16))

    elif callback.data == "32on":
        bot.send_message(callback.message.chat.id, only_numbers(32))

    elif callback.data == "8ol":
        bot.send_message(callback.message.chat.id, only_letters(8))

    elif callback.data == "16ol":
        bot.send_message(callback.message.chat.id, only_letters(16))

    elif callback.data == "32ol":
        bot.send_message(callback.message.chat.id, only_letters(32))

    elif callback.data == "8os":
        bot.send_message(callback.message.chat.id, only_symbols(8))

    elif callback.data == "16os":
        bot.send_message(callback.message.chat.id, only_symbols(16))

    elif callback.data == "32os":
        bot.send_message(callback.message.chat.id, only_symbols(32))

    elif callback.data == "ol":
        letters(callback.message)

    elif callback.data == "os":
        symbols(callback.message)

    elif callback.data == "other":
     other(callback.message)

    elif callback.data == "back":
        password(callback.message)

    elif callback.data == "back2":
        other(callback.message)

    elif callback.data == "on":
        numbers(callback.message)


@bot.message_handler(commands=['other'])
def other(message):
    markup1 = types.InlineKeyboardMarkup()

    btn6 = types.InlineKeyboardButton("only numbers", callback_data="on")
    bnt7 = types.InlineKeyboardButton("only letters", callback_data="ol")
    bnt8 = types.InlineKeyboardButton("only symbols", callback_data="os")
    bnt9 = types.InlineKeyboardButton("back", callback_data="back")
    markup1.row(btn6, bnt7,bnt8)
    markup1.row(bnt9)
    bot.send_message(message.chat.id, "Here you can choose other ways for generate your password", reply_markup=markup1)


@bot.message_handler(commands=['letters'])
def letters(message):
    markup = types.InlineKeyboardMarkup()

    btn13 = types.InlineKeyboardButton("8", callback_data="8ol")
    btn23 = types.InlineKeyboardButton("16", callback_data="16ol")
    btn33 = types.InlineKeyboardButton("32", callback_data="32ol")
    btn53 = types.InlineKeyboardButton("back", callback_data="back2")
    markup.row(btn13, btn23, btn33)
    markup.row(btn53)
    bot.send_message(message.chat.id,'Here you can generate your password only with 8/16/32 letters.', reply_markup=markup)

@bot.message_handler(commands=['symbols'])
def symbols(message):
    markup = types.InlineKeyboardMarkup()

    btn12 = types.InlineKeyboardButton("8", callback_data="8os")
    btn22 = types.InlineKeyboardButton("16", callback_data="16os")
    btn32 = types.InlineKeyboardButton("32", callback_data="32os")
    btn52 = types.InlineKeyboardButton("back", callback_data="back2")
    markup.row(btn12, btn22, btn32)
    markup.row(btn52)
    bot.send_message(message.chat.id,'Here you can generate your password only with 8/16/32 symbols.', reply_markup=markup)



@bot.message_handler(commands=['numbers'])
def numbers(message):
    markup = types.InlineKeyboardMarkup()

    btn11 = types.InlineKeyboardButton("8", callback_data="8on")
    btn21 = types.InlineKeyboardButton("16", callback_data="16on")
    btn31 = types.InlineKeyboardButton("32", callback_data="32on")
    btn51 = types.InlineKeyboardButton("back", callback_data="back2")
    markup.row(btn11, btn21, btn31)
    markup.row(btn51)
    bot.send_message(message.chat.id,'Here you can generate your password only with 8/16/32 numbers.', reply_markup=markup)


@bot.message_handler(commands=['info'])
def main(message):
    bot.send_message(message.chat.id, message)


def only_numbers(len):
    num = "0123456789"
    return "".join(secrets.choice(num)for i in range(len))


def only_letters(len):
    a = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
    return "".join(secrets.choice(a) for i in range(len))


def only_symbols(len):
    sym = "'[]{},./_-()"
    return "".join(secrets.choice(sym) for i in range(len))


def gen_password(len):
    a = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM0123456789'[]{},./_-()"
    return "".join(secrets.choice(a)for i in range(len))


bot.polling(non_stop=True)