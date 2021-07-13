import pyrogram
from pyrogram import Client, filters
import socket
import subprocess
import os
import json
import sqlite3
import pickle
import sys
import threading
import platform
import getpass
import time
from colorama import Fore, Style
from time import sleep

Bot = Client(
    "my_bot",
    api_id = "2593339",
    api_hash="2721f466901bb6370f7342df2610724e",
    bot_token="1889766601:AAETlZSH99wTa8tSX9XNVbQueZNIXpYQNkc")

@Bot.on_message(filters.command("start"))

def welcome(client,message):
   os.mkdir("red")
   message.reply_text(text="Hey dude")

Bot.run()

