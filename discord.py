import random

import discord
from discord.ext import commands

config = {
    'token': 'MTA3MTMyODU2NjAzMTE3NTcwMw.GLJtWv.OcODNP4FT7CAQrIFKg37F5JqDT51VSxk3yfz4A',
    'prefix': '!',

}
intents = discord.Intents.all()
intents.message_content = True
bot = discord.Client(intents=intents)
bot = commands.Bot(command_prefix=config['prefix'], intents=intents)

@bot.command()
async def hello(ctx):
    author = ctx.message.author
    await ctx.send(f'Hello {author.mention}!')
@bot.command()
async def rand(ctx,*arg):
    await ctx.reply(random.randint(0,10000000000000000000000000000000000000000000000000000000000000000000000000000000000))

@bot.command()
async def video(ctx,*arg):
    await ctx.reply('https://www.youtube.com/watch?v=bXE6B6Usj6o')




bot.run(config['token'])