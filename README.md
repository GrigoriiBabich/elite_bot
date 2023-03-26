# elite_bot

Добавляем новую группу для вызова в три простых шага:
1. Придумайте имя списка
```
    list_name
```
2. В файл data.json нужно добавить новый список в следующем формате  
```json
    {
    ...
    "list_name": [],
    ...
    }
```
3. В файле main.py добавить команду 
```py
@bot.message_handler(commands=['list_name'])
def all(message):
    bot.reply_to(message, f"Не забудь описание {unpack(dict['list_name'])}")
```
