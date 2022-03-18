import discord
from discord.ext import commands
import sqlite3

settings = {
    'token': 'OTUyNTA2MzIxNzcxNTgxNDUx.Yi3Aow.MeZjbiA0Uv8fUTpWgI_uUjREFkI',
    'bot': 'RoboShot',
    'id': 952506321771581451,
    'prefix': 's!'
}

bot = commands.Bot(command_prefix = settings['prefix'], intents=discord.Intents.all())

bot.run(settings['token'])

@bot.event
async def on_ready():
	print('Бот запущен!')

	global base, cur
	base = sqlite3.connect('bot.db')
	cur = base.cursor()
	if base:
		print('DataBase connected... OK')