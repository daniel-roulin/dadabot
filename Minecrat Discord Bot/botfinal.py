#!/usr/bin/env python3

import asyncio
import datetime
import discord
import json
from mcstatus import MinecraftServer
import requests
import random

server_url = "dadarou.tk"

client = discord.Client()
token = 'NzY0OTU1ODk5MzQ4Mzg1ODE1.X4Nysg.On025R8mZmcvvl23rtbzYjfziGQ'
bot_channels = []

json_ids = open('ids.json')
discord_ids = json.load(json_ids)
json_ids.close()


def get_gif_url(players):
    return "http://dadarou.tk:8080/gifs/" + "-".join(players) + ".gif"

def get_players():
    server = MinecraftServer.lookup(server_url)
    try:
        query = server.query()
        # print("The server has the following players online: {0}".format(", ".join(query.players.names)))
        return query.players.names
    except Exception as e:
        print('[MCStatus]: Error when querying the server:')
        print(str(e))
        return []

async def player2user(player):
    if player in discord_ids:
        user = await client.fetch_user(discord_ids[player])
        return user
    else:
        return None

async def make_message(connected_players, new_player=None):
    if new_player:
        embed = discord.Embed(title=f"{new_player} joined the server!", color=0xFF5733)
        new_user = await player2user(new_player)
        if new_user != None:
            embed.set_author(name=new_user.display_name, icon_url=new_user.avatar_url)
            embed.description= f"{new_user} joined {server_url} with IGN: {new_player}. Players connected to the server:"
        else:
            embed.set_author(name="unknown user")
            embed.description= f"An unknown user joined {server_url} with IGN: {new_player}. Players connected to the server:"
        skin_url = get_gif_url(connected_players)
        embed.set_thumbnail(url = skin_url)
    else:
        embed = discord.Embed(title=f"Players connected to {server_url}:", color=0xFF5733)

    if connected_players != []:    
        for player in connected_players:
            user = await player2user(player)
            if user != None:
                embed.add_field(name=player, value=user, inline=False)
            else:
                embed.add_field(name=player, value="unknown discord", inline=False)
    else:
        sad_responses = ["feels empty...", "you can still play alone ¯\_(ツ)_/¯", "better luck next time..", "nobody liked you anyways", "violence is never the answer", "wanna play Roblox with me instead?", "happens to the best of us", "but here is a banana instead 🍌", "go cry now.", "nobody's ever here for me anyways", "Roses are red\nLapis is blue\nFeed me some wheat\nI want to mate with you"]
        embed.add_field(name="Nobody", value=random.choice(sad_responses), inline=False)
        
    embed.set_footer(text='Made by Dada_Roulin#5870/Superbloc100. Thank you to Crafatar for providing avatars.', icon_url="https://cdn.discordapp.com/avatars/414733857460453377/c8eee80c268e0e928786eea0fd5b1850.webp?size=1024")
    return embed

@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")

    channel = client.get_channel(807285208130781224)
    print(f"Connected to: {channel.name} in {channel.guild}")
    bot_channels.append(channel)

    # for guild in client.guilds:
    #     for channel in guild.text_channels:
    #         if channel.name == "server_info":
    #             print(f"Connected to: {channel.name} in {channel.guild}")
    #             bot_channels.append(channel)

@client.event
async def on_message(message):
    if str(message.author) != "Dadabot#9151" and message.content.startswith("/list"):
        connected_players = get_players()
        embed = await make_message(connected_players)
        embed.set_author(name=message.author.display_name, icon_url=message.author.avatar_url)
        print(f"Responding to '{str(message.content)}' by {str(message.author)} in {str(message.channel.guild.name)} with {str(connected_players)} connected")
        await message.channel.send(embed=embed)

async def online_players_background_task():
    players_dates = {}
    await client.wait_until_ready()
    while not client.is_closed():
        connected_players = get_players()
        new_players = []
        now = datetime.datetime.now()
        threshold = datetime.timedelta(minutes = 5)
        # threshold = datetime.timedelta(seconds=10)
        for player in connected_players:
            if player in players_dates:
                delta = now - players_dates[player]
                # print(player, delta)
                if delta > threshold:
                    new_players.append(player)
            else:
                new_players.append(player)
            players_dates[player] = datetime.datetime.now()
        for new_player in new_players:
            embed = await make_message(connected_players, new_player)
            for channel in bot_channels: 
                print(f"Sending welcome message for {new_player} with {str(connected_players)} connected in {channel.guild.name}")
                await channel.send(embed=embed)
        
        await asyncio.sleep(2)

print("Starting server check background task")
client.loop.create_task(online_players_background_task())

print("Starting client")
client.run(token)