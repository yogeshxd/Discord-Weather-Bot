import discord
from discord.ext import commands
import time
import logging
import requests
import random
from discord.ext import tasks, commands

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix=['Wu '], intents=intents)

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
discord.utils.setup_logging(level=logging.DEBUG, handler=handler, root=False)

@bot.event
async def on_ready():
    print(f'\nLogged as: {bot.user.name} - {bot.user.id}\nConnected to:')
    for i in bot.guilds:
        print(
        f'{i}'
        )
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"Weather Updates."))
    print(f'Bot is ready to go!')
    await auto.start()

@bot.command(hidden=True)
async def reload(ctx, extension):
    bot.reload_extension(extension)

@bot.command(hidden=True)
async def activity(ctx, arg, arg2, arg3=None):
    author = ctx.message.author
    if author.id == 490749286930448384: #change this to you discord id
        if arg == 'playing':
            await bot.change_presence(activity=discord.Game(name=arg2))
        elif arg == 'streaming':
            await bot.change_presence(activity=discord.Streaming(name=arg2, url=arg3))
        elif arg == 'listening':
            await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=arg2))
        elif arg == 'watching':
            await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=arg2))
        await ctx.send('Status Updated')
        time.sleep(0.5)
        await ctx.channel.purge(limit=2)
    else:
        msg = await ctx.send('Fuck off. You are not authorized', delete_after=60)

@tasks.loop(minutes=5.0)
async def auto():
    channel = bot.get_channel(1013697327879421993)
    await channel.purge(limit=100)
    #city 1
    city = 'Delhi'
    key = ''
    url = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid="+key
    a = requests.get(url)
    data = a.json()
    if a.status_code==200:
        main = data['main']
        temp = int(main['temp'])-273
        temprature = str(temp)+'°C'
        humidity = main['humidity']
        pressure = main['pressure']
        report = data['weather']
        cit = f"{city:-^30}\nTemperature: {temprature}\nHumidity: {humidity}\nPressure: {pressure}\nWeather Report: {report[0]['description']}"
        temp=discord.Embed(title=f"Weather report for {city}", description=cit, color=random.randint(0, 0xffffff))
        channel = bot.get_channel(1013697327879421993)
        await channel.send(embed=temp)
    #city 2
    city = 'Lucknow'
    key = ''
    url = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid="+key
    a = requests.get(url)
    data = a.json()
    if a.status_code==200:
        main = data['main']
        temp = int(main['temp'])-273
        temprature = str(temp)+'°C'
        humidity = main['humidity']
        pressure = main['pressure']
        report = data['weather']
        cit = f"{city:-^30}\nTemperature: {temprature}\nHumidity: {humidity}\nPressure: {pressure}\nWeather Report: {report[0]['description']}"
        temp=discord.Embed(title=f"Weather report for {city}", description=cit, color=random.randint(0, 0xffffff))
        channel = bot.get_channel(1013697327879421993)
        await channel.send(embed=temp)

bot.run('', reconnect = True)
