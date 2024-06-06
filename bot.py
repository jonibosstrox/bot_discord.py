import discord
from discord.ext import commands
from modelo import *
import os
import random
import requests

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def IA(ctx):
    if ctx.message.attachments:
        for attach in ctx.message.attachements:
            file_name = attach.filename
            file_url = attach.url
            await attach.save( f"./{attach.filename}" )
            await ctx.send(get_class("./keras.model.h5", "labels.txt", f"./{attach.filename}" ) )
    else:
        await ctx.send("Olvidaste adjuntar una imagen :v")
            
@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

bot.run("TOKEN")
