from discord.ext import tasks, commands
import requests
import discord
from os import environ
import time
import os
import random

class auto(commands.Cog, name='auto'):
    def __init__(self, bot):
        self.index = 0
        self.bot = bot
        self.auto.start()

    def cog_unload(self):
        self.printer.cancel()

    @tasks.loop(minutes=1.0)
    async def auto(self):
        city = 'Delhi'
        key = '{Your Open Wheather API Key}'
        url = "https://api.openweathermap.org/data/2.5/weather?"+"q="+city+"&appid="+key
        a = requests.get(url)
        data = a.json()
        if a.status_code==200:
            main = data['main']
            temprature = main['temp']
            humidity = main['humidity']
            pressure = main['pressure']
            report = data['weather']
            cit = f"{city:-^30}\nTemperature: {temprature}\nHumidity: {humidity}\nPressure: {pressure}\nWeather Report: {report[0]['description']}"
            temp=discord.Embed(title=f"Weather report for {city}", description=cit, color=random.randint(0, 0xffffff))
            channel = self.bot.get_channel(Your channel ID)
            msg = await channel.send(embed=temp)

    @auto.before_loop
    async def before_auto(self):
        print('waiting...')
        await self.bot.wait_until_ready()

def setup(bot):
    bot.add_cog(auto(bot))
