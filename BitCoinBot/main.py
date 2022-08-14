import requests
from bs4 import BeautifulSoup
from telebot import types
import telebot

url = 'https://www.coindesk.com/price/bitcoin/'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
}

TOKEN = ''  # Put your token here!
bot = telebot.TeleBot(TOKEN)


def price():
    req = requests.get(url, headers=headers)
    soup = BeautifulSoup(req.text, 'lxml')
    return soup.find(class_='typography__StyledTypography-owin6q-0 jvRAOp').text


@bot.message_handler(commands=['start'])
def start(message):
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button = types.KeyboardButton(text="Show Price🔥")
    kb.add(button)
    bot.send_message(
        message.chat.id,
        'This bot shows you price of 🔥Bitcoin🔥! '
        '\n Click on the button down bellow or write "price"'
        , reply_markup=kb
    )


@bot.message_handler(content_types=['text'])
def bot_message(message):
    if message.chat.type == 'private':
        if message.text == 'Show Price🔥':
            bot.send_message(message.chat.id, f"{price()}$")

        elif message.text.lower() == 'price':
            bot.send_message(message.chat.id, f"{price()}$")


if __name__ == '__main__':
    bot.polling()
