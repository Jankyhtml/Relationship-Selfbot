import discord, subprocess, sys, time, os, colorama, base64, codecs, datetime, io, random, numpy, datetime, smtplib, string, ctypes
import urllib.parse, urllib.request, re, json, requests, webbrowser, aiohttp, dns.name, asyncio, functools, logging

import discord
import time
from discord.ext import commands
from colorama import Fore, init 
import requests
import os 
import base64
import random
 
# Dont just skid it, gimme some credits, thank you - Janky 
 # Dont just skid it, gimme some credits, thank you - Janky
  # Dont just skid it, gimme some credits, thank you - Janky
   # Dont just skid it, gimme some credits, thank you - Janky
    # Dont just skid it, gimme some credits, thank you - Janky
     # Dont just skid it, gimme some credits, thank you - Janky 
      # Dont just skid it, gimme some credits, thank you - Janky
       # Dont just skid it, gimme some credits, thank you - Janky
        # Dont just skid it, gimme some credits, thank you - Janky
         # Dont just skid it, gimme some credits, thank you - Janky
          # Dont just skid it, gimme some credits, thank you - Janky
           # Dont just skid it, gimme some credits, thank you - Janky
            # Dont just skid it, gimme some credits, thank you - Janky

prefix = "."

JANKY = commands.Bot(command_prefix=prefix, self_bot=True)
JANKY.remove_command('help')

@JANKY.event
async def on_connect():
    print(f'''{Fore.RED}
 ▄▄▄██▀▀▀▄▄▄       ███▄    █  ██ ▄█▀▓██   ██▓
   ▒██  ▒████▄     ██ ▀█   █  ██▄█▒  ▒██  ██▒
   ░██  ▒██  ▀█▄  ▓██  ▀█ ██▒▓███▄░   ▒██ ██░
▓██▄██▓ ░██▄▄▄▄██ ▓██▒  ▐▌██▒▓██ █▄   ░ ▐██▓░
 ▓███▒   ▓█   ▓██▒▒██░   ▓██░▒██▒ █▄  ░ ██▒▓░
 ▒▓▒▒░   ▒▒   ▓▒█░░ ▒░   ▒ ▒ ▒ ▒▒ ▓▒   ██▒▒▒ 
 ▒ ░▒░    ▒   ▒▒ ░░ ░░   ░ ▒░░ ░▒ ▒░ ▓██ ░▒░ 
 ░ ░ ░    ░   ▒      ░   ░ ░ ░ ░░ ░  ▒ ▒ ░░  
 ░   ░        ░  ░         ░ ░  ░    ░ ░     
                                     ░ ░     
                                                                                           
                                                                                                                                     
                                                                       
            {Fore.WHITE}[+] MADE BY JANKY
              {Fore.WHITE}_________________    
                {Fore.WHITE}
                {Fore.WHITE}[-]    J
                  {Fore.WHITE}[-]   A
                    {Fore.WHITE}[-]  N
                     {Fore.WHITE}[-]  K
                       {Fore.WHITE}[-] Y
                                                                                               
                                                                               ''')
@JANKY.command()
async def help(ctx):
    embed = discord.Embed(title="𝙍𝙚𝙡𝙖𝙩𝙞𝙤𝙣𝙨𝙝𝙞𝙥 𝙎𝙚𝙡𝙛𝙗𝙤𝙩", color= discord.Color(random.randint(0xe360c3, 0xe360c3)))
    embed.add_field(name="`Love`", value="**SENDS LOVE PARAGRAPH.**\n", inline=False)
    embed.add_field(name="`Apoligize`", value="**SENDS APOLIGY PARAGRAPH.**\n", inline=False)  
    embed.add_field(name="`Cheating`", value="**SENDS CHEATING PARAGRAPH.**\n", inline=False)
    embed.add_field(name="`Birthday`", value="**SENDS BIRTHDAY PARAGRAPH.**\n", inline=False)
    embed.add_field(name="`Gay`", value="**SENDS GAY PARAGRAPH.**\n", inline=False)
    embed.add_field(name="`ESex`", value="**SENDS E-SEX PARAGRAPH.**\n", inline=False)
    embed.add_field(name="`Janky`", value="**I was bored okay :(.**\n", inline=False)
    embed.add_field(name='`MWAH`', value="**JANKY MADE THIS (SKIDS K)**", inline=False)
    embed.set_footer(text=f"Logged in as : {ctx.author}", icon_url=ctx.author.avatar_url)
    embed.set_image(url="https://cdn.discordapp.com/attachments/739948730777731192/742449338961362959/56.gif")
    await ctx.send(embed=embed)

@JANKY.command()
async def Love(ctx):
    await ctx.message.delete()
    await ctx.send('**You’re nice and funny and how I can talk to you about stuff and make jokes with you, we connect alot in text but I wanna be able to talk to you on call too, I care about you a lot and I love you. I like how we have late night conversations and how much you care about me and waited for me. I see us having a future but there is stuff that I need to work on in our relationship like communicating but I just dont want to put stuff on you when Im upset or bother you about it. its not your fault, and I don’t want to lose you, and you’re not boring im just dry sometimes because I just quick respond. Some stuff kinda bothers me like when you say i love you without capsulizing it, just seems like you don’t mean it, or like when you say “if you want me to” when I ask something, because it comes off like you dont want to and im forcing you to. Its just little stuff that bothers me that shouldn’t, I just over think stuff. I see a lot in you like how much of great boyfriend you are and you always show me a lot attention and make my day better:two_hearts:. But don’t say you’re boring because if anything im boring I barely respond most the time and I feel bad for it because you deserve better and ill try to talk to you more**')

@JANKY.command()
async def Apoligize(ctx):
    await ctx.message.delete()
    await ctx.send('**I cling on to the hope that the heart that Ive cherished and hurt, truly knows how sorry I am for the pain I caused. All I can say Im sorry to you, my love, my girlfriend and the best thing thats ever happened to me. All I can ask is humbly for forgiveness. Please forgive me.**')

@JANKY.command()
async def Cheating(ctx):
    await ctx.message.delete()
    await ctx.send('**I want to tell you I am sorry a thousand times but I know my apology cant undo what has been done or ease the pain in your heart Cheating on you is certainly an unforgivable mistake. I totally deserve all the anger and resentment from you for what I have put you through However, it also pains me to see you suffering as a result of my misbehavior. Guilt burns in my heart thinking of all the hurt that you must have felt because of my recklessness. Each time that I think of you, I get angry with myself because I can imagine all the bitter tears you must have shed when you learned of my indiscretion.**')

@JANKY.command()
async def Birthday(ctx):
    await ctx.message.delete()
    await ctx.send('**Baby I love you much more than you can ever imagine. My heart belongs to no one else but you. As you grow a year older today, I’ll grow older with you and our love will always stay young and strong. Happy birthday, my love and have a fun-filled day.**')

@JANKY.command()
async def Gay(ctx):
    await ctx.message.delete()
    await ctx.send('**Ive thought about it a million times and played all the scenarios in my head. You know sometimes when I am quiet and you ask me what I am thinking or what is wrong. Thats me playing out my options. I know that the easiest route to avoid all of this would be to keep my secret to myself so I dont rock our boat. I am Gay...**')

@JANKY.command()
async def ESEX(ctx):
    await ctx.message.delete()
    await ctx.send('**I want you to hold me so tight. I want you to lick me all over.I want to perform your art on me! I want to have every reason to moan and scream your name! I want you to kiss me so badly making me want you in sweet and reckless abandon! You are my sweet craving!**')

JANKY.run('YOUR TOKEN HERE', bot=False)
