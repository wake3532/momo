import discord
from discord.ext import commands
import os
import asyncio
import random
import urllib
from bs4 import BeautifulSoup
from urllib.request import Request
from urllib import parse
import bs4
import time


client = discord.Client()

owner = ['724769557759393837']
@client.event
async def on_ready():
    print('봇이 로그인 하였습니다.')
    print(' ')
    print('닉네임 : {}'.format(client.user.name))
    print('아이디 : {}'.format(client.user.id))

@client.event
async def on_ready():
    print('봇이 로그인 하였습니다.')
    print(' ')
    print('닉네임 : {}'.format(client.user.name))
    print('아이디 : {}'.format(client.user.id))
    while True:
        user = len(client.users)
        server = len(client.guilds)
        messages = ["BOT HOSTING : FINE ", " ERROR : 없음 " , " 이 봇은 개인적인 봇 입니다. 가져가실 수 없습니다. " , str(user) + "분이 우리 서버에 가입중! .", str(server) + "부스트!"]
        for (m) in range(5):
            await client.change_presence(status=discord.Status.dnd, activity=discord.Activity(name=messages[(m)], type=discord.ActivityType.watching))
            await asyncio.sleep(4)


@client.event
async def on_member_join(member):
    syschannel = member.guild.system_channel.id 
    try:
        embed=discord.Embed(
            title=f'진심으로 환영해요.',
            description=f'{member}님  {member.guild} 환영합니다  !   \n 현재 서버 인원수: {str(len(member.guild.members))}명 나가지 마세요 ㅠㅠ;;ㅠㅠ',
            colour=0x00ff00
        )
        embed.set_thumbnail(url=member.avatar_url)
        await client.get_channel(syschannel).send(embed=embed)
    except:
        return None
@client.event
async def on_member_remove(member):
    syschannel = member.guild.system_channel.id 
    try:
        embed=discord.Embed(
            title=f'멤버가 어어어ㅓ어엄청 아쉽게 퇴장하셨습니다. ',
            description=f'{member}님이{member.guild}에 퇴장 했습니다. :( 아쉬워요  더 놀고 가지..ㅠㅠ \n 현재 서버 인원수: {str(len(member.guild.members))}명',
            colour=discord.Colour.red()
        )
        embed.set_thumbnail(url=member.avatar_url)
        await client.get_channel(syschannel).send(embed=embed)
    except:
        return None

@client.event
async def on_message(message):
    if (message.content.split(" ")[0] == "momo!ban"):
        if (message.author.guild_permissions.ban_members):
            try:
                user = message.guild.get_member(int(message.content.split(' ')[1][3:21]))
                reason = message.content[22:]
                if (len(message.content.split(" ")) == 2):
                    reason = "None"
                await user.send(embed=discord.Embed(title=" 으아... 더 같이 놀고 싶었는데 관리자가 거부하네요 !ㅠㅠㅠㅠㅠㅠ [ 당신은 서버에서 밴 되셨습니다 ] ", description=f'당신은 **{message.guild.name}** 서버에서 차단되었습니다. 사유는 다음과 같습니다. ```{reason}```', color=0xff0000))
                await user.ban(reason=reason)
                await message.channel.send(embed=discord.Embed(title="Ban Success", description=f"{message.author.mention} 님, 성공적으로 차단시켰습니다. 사유:```{reason}```", color=0x00ff00))
            except Exception as e:
                await message.channel.send(embed=discord.Embed(title="❌ 에러 발생", description=str(e), color=0xff0000))
                return
        else:
            await message.channel.send(embed=discord.Embed(title="⚠ 권한 부족", description=message.author.mention + "님은 유저를 차단할 수 있는 권한이 없습니다.", color=0xff0000))
            return
            

access_token = os.environ["BOT_TOKEN"]
client.run(access_token)           
