
# Project Description

Simple bot for ping friends in your group chat 

# Usage

To use this bot, you will need to create your own bot and get a token. You can get a token by following the instructions on the official Telegram page for creating bots.

## Installation and Usage

1.  Prepare environment with following instruction https://habr.com/ru/articles/549962/ 
    
2.  Download the repository or clone it:
    `git  clone  https://github.com/GrigoriiBabich/elite_bot.git`
    
3.  Paste your bot token to `config.py`:
    `TOKEN =  'your_token'`

4. Add info about groups and chat members to file `data.json`
```json
    {
    "command_name_1": ["..."],
    "command_name_2": ["@group_member", "@other_group_member"],
    "command_name_3": ["..."]
    }
```
    
5. For every list you need add following code to `main.py`
```python
    elif command == 'other':
        bot.reply_to(message, f"Please add following block for your commands {unpack(dict[command])}")
```
    
6.  Run the bot:
    `sudo systemctl start`

