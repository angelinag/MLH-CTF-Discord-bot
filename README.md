# MLH-CTF-Discord-bot
A Discord bot which pings users in a channel whenever a new CTF challenge is up.

![bot](preview.png)

# How to use
The bot is located in `bot.py`. 

### 1. Install the dependencies:

#### Dependencies
 - discord
 - discord.ext
 - bs4
 - requests
 - dotenv
 - selenium
 - webdriver_manager
 - chromedriver_py
 - threading
 
You'll need to have Chrome installed since its the browser used in this bot.  
You can change this yourself, just find the definition of the driver and change it to whatever
selenium driver suits your needs.
 
### 2. Edit the script with your tokens
You'll need:
 - *A discord app with a discord bot in it, and the token of that specific bot*. To obtain it, go to Discord.
 - *The MLH platform's session cookie value as a token.* You can find it in your cookies when you go to the platform.
 - *The discord channel ID where messages will get sent.* With developer mode enabled, rightclick on the channel > Copy ID.
 
### 3. Simply run the script without any arguments:
`python bot.py`
