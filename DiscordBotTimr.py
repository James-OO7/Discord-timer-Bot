import time
import os
import discord

from discord.ext import commands

Sec = 0
Min = 0
MinReq = 0
SeqReq = 0

TOKEN = "NzAyMTYzNTg3Mjk2Mzk1MzY2.XqcbDg.MfOcE_Pqt7_frK8H5eYfb_4oRaU"
GUILD = "Galloway Coding Class"

bot = commands.Bot(command_prefix = '!')

#bot setup lmao
@bot.event
async def on_ready ():
    guild = discord.utils.get(bot.guilds, name = GUILD)
    print(f'{bot.user.name} has connected to the following server:\n\t{guild.name} (id: {guild.id})')

@bot.command(name = 'timer', help = 'Type # of minutes then # of seconds to set your timer')
async def timer(ctx, MinReq, SecReq):
    response = 'Your timer is set for ' + str(MinReq) + ' minutes and ' + str(SecReq) + ' seconds. We will send a meesage to this channel when your timer is done!'
    countdown = True
    await ctx.send(response)
    while countdown:
        if countdown == False:
            response = 'Your timers has been canceled. Have a nice day!'
            await ctx.send(response)
            break
        if int(SecReq) == 0:
            SecReq = int(60)
            MinReq = int(MinReq) - 1
            if MinReq < 0:
                mention_string = '<@!' + str(ctx.message.author.id) + '>'
                await ctx.send(mention_string + ', your timer is finished!')
                break
        SecReq = int(SecReq) - 1
        time.sleep(1)

@bot.command(name = 'timerCancel', help = 'Command used to cancel all set timers.')
async def timerCancel(ctx):
    countdown = False
    
        

bot.run(TOKEN)
