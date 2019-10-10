#!python3.7.4

import discord

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    # 「おはよう」で始まるか調べる
    if message.content.startswith("古戦場"):
        # 送り主がBotだった場合反応したくないので
        if client.user != message.author:
            # メッセージを書きます

            m = "http://game.granbluefantasy.jp/#top" + message.author.name + "さん！"
            # メッセージが送られてきたチャンネルへメッセージを送ります
            await message.channel.send(m)


            # token にDiscordのデベロッパサイトで取得したトークンを入れてください
client.run("TOKEN")
