import discord
import pytz
from datetime import datetime


TOKEN = ""
client = discord.Client()

timezones = {
    "한국": "Asia/Seoul",
    "미국 동부": "America/New_York",
    "미국 서부": "America/Los_Angeles",
    "일본": "Asia/Tokyo",
    "중국": "Asia/Shanghai",
    "러시아": "Europe/Moscow",
    "영국": "Europe/London",
    "독일": "Europe/Berlin",
    "네덜란드": "Europe/Berlin",
    "오스트레일리아": "Australia/Sydney",
    "뉴질랜드": "Pacific/Auckland"
}

@client.event
async def on_ready():
    print("세계시간 봇 작동 시작")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("!time"):
        timezone_str = message.content[6:].strip()

        if timezone_str not in timezones:
            await message.channel.send("시간대를 찾을 수 없습니다.")
            return

        timezone = pytz.timezone(timezones[timezone_str])
        now = datetime.now(timezone)
        time_str = now.strftime("%Y년 %m월 %d일 %H시 %M분 %S초")

        response = f"{timezone_str} 시간은 {time_str}입니다."
        await message.channel.send(response)

client.run(TOKEN)

