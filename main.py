import discord
from discord.ext import commands
import openai
import json
import os
import keep_alive

file = open('config.json', 'r')
config = json.load(file)

intents = discord.Intents.all()
bot = commands.Bot(config['prefix'], intents=intents)
openai.api_key = config['token_openai']


@bot.event
async def on_ready():
    print('Бот онлайн')


@bot.command(name='chat')
async def cont(ctx: commands.context, *, args):
    result = str(args)
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=result,
        temperature=0.9,
        max_tokens=1000,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.6,
        stop=[" Людина:", " ШІ:"]
    )
    await ctx.send(embed=discord.Embed(title=f'{result}', description=response['choices'][0]['text']))


@bot.command(name='gpt')
async def cont(ctx: commands.context, *, args):
    gpt = str(args)
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=gpt,
        temperature=0.9,
        max_tokens=1000,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.6,
        stop=[" Людина:", " ШІ:"]
    )
    await ctx.send(embed=discord.Embed(title=f'{gpt}', description=response['choices'][0]['text']))


@bot.command(name='translate')
async def cont(ctx: commands.context, *, args):
    translate = str(args)
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=translate,
        temperature=0.3,
        max_tokens=100,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )
    await ctx.send(embed=discord.Embed(title=f'{translate}', description=response['choices'][0]['text']))


@bot.command(name='рецепт')
async def cont(ctx: commands.context, *, args):
    recipe = str(args)
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=recipe,
        temperature=0.3,
        max_tokens=120,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )
    await ctx.send(embed=discord.Embed(title=f'{recipe}', description=response['choices'][0]['text']))

keep_alive.keep_alive()
bot.run(config['token'])
