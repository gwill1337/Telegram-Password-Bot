# Telegram Password Bot

![PyPI](https://img.shields.io/pypi/v/pyTelegramBotAPI)
![PyPI](https://img.shields.io/pypi/pyversions/pyTelegramBotAPI?color=red)

**Telegram Password Bot** - this telegram bot for generating passwords with 8/16/32 symbols and which uses pyTelegramBotAPI 4.27.0

**API Documentation** - [https://pytba.readthedocs.io/en/latest/index.html](https://pytba.readthedocs.io/en/latest/index.html)

## Requirements
Install the current version [PyPI](https://pypi.org/project/pyTelegramBotAPI/):
```python
pip install pyTelegramBotAPI
```
or with Git:

```python
pip install git+https://github.com/eternnoir/pyTelegramBotAPI.git
```

## Usage
1. Create Virtualenv environment (Venv).
2. Create Telegram Bot in ```@BotFather```, take API token, then paste it instead **"bot's API"**
```python
bot = telebot.TeleBot("bot's API")
```
3. Also if you want you can write **/setcommands** in ```@BotFather```, choose your bot and set comand **"start - start"**, in order to when you enter bot at first, in the left corner was shown menu with command "/start".

## Generation

This Bot uses module **secrets** to generate passwords.

```python
def gen_password(len):
    a = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM0123456789'[]{},./_-()"
    return "".join(secrets.choice(a)for i in range(len))
```

It also has generation with only letters, numbers and symbols.

```python
def only_numbers(len):
    num = "0123456789"
    return "".join(secrets.choice(num)for i in range(len))


def only_letters(len):
    a = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
    return "".join(secrets.choice(a) for i in range(len))


def only_symbols(len):
    sym = "'[]{},./_-()"
    return "".join(secrets.choice(sym) for i in range(len))
```
