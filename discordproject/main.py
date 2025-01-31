import discord
from discord.ext import commands
from model import modelCalistir

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
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

bot.run("import discord")
from discord.ext import commands

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
async def kontrol(ctx):
    if ctx.message.attachments:
        for attachments in ctx.message.attachments:
            file_name = attachments.filename
            url_name = attachments.url 
            await attachments.save(file_name)
            await ctx.send(f'Fotoğrafınız başarıyla kaydedildi. Fotoğrafın adı:{file_name}')
            await ctx.send(modelCalistir(file_name))
    else:
        
        await ctx.send('Bir fotoğraf eklemelisiniz!')
    

bot.run("TOKEN")
