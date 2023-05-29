import telebot
import json
from config import token


bot = telebot.TeleBot(token)
dict = {}
filename = ('data.json')

#открыть .json с данными
try:
    with open(filename, "r") as f:
        dict = json.load(f)
except FileNotFoundError:
    pass

#распаковка списка
def unpack(s):
    return " ".join(map(str, s))

#добавление в список
@bot.message_handler(commands=['join'])
def join_ping_list(message):
    command = message.text.split()
    if len(command) < 2:
        bot.send_message(message.chat.id, "Название списка введи, плз. Например: `/join list1`")
        dict["id"].append(message.chat.id)
        return

    list_name = command[1]
    if list_name not in dict:
        bot.send_message(message.chat.id, f"Списка `{list_name}` не существует, @AeksErr может его добавить")
        return

    username = (f"@{message.from_user.username}")
    user_id = message.from_user.id
    if username not in dict[list_name]:
        dict[list_name].append(username)
        bot.send_message(user_id, f"Ура, ты теперь в списке `{list_name}`")
        with open(filename, "w") as f:
            json.dump(dict, f)
    else:
        bot.send_message(user_id, f"Ты уже есть в списке `{list_name}`")

@bot.message_handler(commands=list(dict.keys()))
def handle_command(message):
    commands = message.text.split("@")
    command = commands[0]("/", "")
    if command == 'all':
        bot.reply_to(message, f"Тегаю всех в этом чятике: {unpack(dict[command])}")
    elif command == 'other':
        bot.reply_to(message, f"Please add following block for your commands {unpack(dict[command])}")




bot.polling(none_stop=True, interval=0) #обязательная для работы бота часть

