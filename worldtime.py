import discord
from discord.ext.commands import Bot
import datetime

TOKEN = ''

intents = discord.Intents.default()

# !로 시작하면 명령어로 인식
bot = Bot(command_prefix='worldt', intents=intents)

# !hello 명령어 처리
@bot.command()
async def ime(ctx, country):
  

  if country in
  await ctx.reply('{0}의 시간은 현재 {1} 입니다.'.format(country, worldtime)

# !bye 명령어 처리
@bot.command()
async def bye(ctx):
  await ctx.reply('See you later!')

bot.run(TOKEN)
