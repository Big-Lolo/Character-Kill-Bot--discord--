# BOT CK (discord)
 The finality of this bot is to facilitate the work when you're going to make a Character Kill of a player on GTA Roleplay.
You can use this bot to delate information of a database with some discord commands.

# Configuration to make a Character Kill (CK):
1. Use the command  ```ruby !help``` to know all the commands that offers the bot.
2. Use command  ```ruby !start [ip] [username] [password] [database_name]``` to start the connection with you're database SQL.
- If database has not a password, you have to put the sign " - " when you insert the password
3. Use command  ```ruby !add [table_name] [column_name]``` to add tables and columns where you want to delate the identifier.
- You can use the command  ```ruby !add [table_name] [column_name]``` more than one time. and all tables and columns would be considered yo delate the indentifier.
4. Use the command  ```ruby !save``` to save the credentials of you're database and the tables/columns. Next time you wouldn't need to insert all the datas inserted before.
5. Use the command  ```ruby !CK [identifier (steam or rockstar)]``` to realize the Character Kill.
- you just could delate one identificator. If all columns selected has steam identificator, you have to insert the Steam identificator with the !CK command.

# Requests:
To excec this bot, you need to install / import next complements:
- Discord.py
- mysql-connection
- os

To install the complements, follow the instructions below:

1. Install Python.
2. discord.py: To install discord py on Windows, open cmd and pass next command:
```ruby py -3.6 -m pip install -U discord.py ```
To install it on linux, use the next command: ```ruby python3 -m pip install -U discord.py```

3. mysql-connection: To install mysql-connection on Windows, open and paass next command: 
- ```ruby pip install mysql-connector-python```.
- To install it on Linux, you have to insert next commands:
- ```ruby sudo apt-get install mysql-connector-python```
- ```ruby pip install mysql-connector-python```
