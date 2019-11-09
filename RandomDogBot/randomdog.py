from telegram.ext import Updater, CommandHandler
import requests
import re
contents = requests.get('https://random.dog/woof.json').json()
print(contents)
