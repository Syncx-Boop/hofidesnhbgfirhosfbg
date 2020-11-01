import discord
import asyncio
import random 

opt = ["schere","papier","stein"]

client = discord.Client()
@client.event
async def on_message(message):
    if message.content.lower() in opt:
        oopt = random.choice(opt)
        if oopt == message.content.lower():
            await message.channel.send("Gleichstand")
        elif oopt == "schere" and message.content.lower() == "papier":
            await message.channel.send ("Ich habe mit schere gewonnen")     
        elif oopt == "papier" and message.content.lower() == "stein":
            await message.channel.send ("Ich habe mit papier gewonnen")     
        elif oopt == "stein" and message.content.lower() == "schere":
            await message.channel.send ("Ich habe mit stein gewonnen")
        elif oopt == "schere" and message.content.lower() == "stein":
            await message.channel.send ("Ich habe mit schere verloren")     
        elif oopt == "papier" and message.content.lower() == "schere":
            await message.channel.send ("Ich habe mit papier verloren")     
        elif oopt == "stein" and message.content.lower() == "papier":
            await message.channel.send ("Ich habe mit stein verloren")     





with open("token.tk","r") as token_file:
    client.run(token_file.readline())