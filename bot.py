# bot.py

import os

import discord
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from discord.ext import tasks

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager
from chromedriver_py import binary_path # gets the path variable for the chromedriver
import threading # for refreshing

load_dotenv()
TOKEN = 'YOUR-DISCORD-BOT-TOKEN-HERE'

cookies = {
    'name': 'session',
    'value' : 'YOUR-MLH-CTF-SESS-COOKIE-VALUE-HERE'
}
url = 'https://ctf.mlh-fellowship.space/challenges'

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    channel = client.get_channel(788689765000151065) # use your channel number here
    check.start(channel)

# This refreshes every 6 seconds, change if necessary
@tasks.loop(minutes=0.1, count=None)    
async def check(channel):
    current = get_current_number()
    last = int(get_last_number())
    if current == last:
        print('Nothing new!')
    elif current > last:
        print('New challenge!')
        # message people
        await channel.send('New challenge available!!!')
        # edit file with new number of challenges
        wr = open("last_number.txt", 'w')
        wr.write(str(current))
    else:
        print('error.')

    
def get_current_number():
    # sets driver
    driver = webdriver.Chrome(ChromeDriverManager(version="87.0.4280.88").install())
    driver.get(url)
    # removes just-set cookie
    # adds cookie with token
    driver.add_cookie(cookies)
    driver.get(url)
    # await for challenges to load dynamically via js
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".challenge-button"))
    )
    # get the challenge board
    dom = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "challenges-board"))
    ).get_attribute('innerHTML')
    driver.quit()
    # transform the dom branch into something readable
    soup = BeautifulSoup(dom)
    mydivs = soup.findAll("button", {"class": "challenge-button"})
    # return number of challenges on the page
    return len(mydivs)
    
def get_last_number():
    # reads the helper file which stores the last # of challenges
    f = open("last_number.txt", "r")
    number = f.read()
    f.close()
    return number

client.run(TOKEN)