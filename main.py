import discord
import time
import os
import requests
import json
from replit import db
import random as r
from discord.ext.commands import Bot
from random import uniform
from keep_alive import keep_alive
client=discord.Client()
my_secret = os.environ['!F!J']
shop = [["soldier", 100],["gun",50]]
def example():
  response = requests.get("https://www.boredbutton.com/random")
  json_data=json.loads(response)
  return(json_data)
class UpdateBCur():
  if "BlueMoney" in db.keys():
    BlueCurrency = db["BlueMoney"]
    def blueMin(amountB):
      BlueCurrency-=amountB
      db["BlueMoney"] = BlueCurrency
    def blueAdd(amountBPlus):
      BlueCurrency+=amountBPlus
      db["BlueMoney"]=BlueCurrency
  else:
    db["BlueMoney"]=1000
    BlueCurrency=db["BlueMoney"]
@client.event
async def shop_input(message2,ident):
  if message2.author.name != ident:
    await shop_person(message2,ident)
  if message2.content.lower() == "y":
    await message2.channel.send('Purchase Complete!')
  elif message2.content.lower() == "n":
    await message2.channel.send('Purchase Canceled!')
  else:
    await message2.channel.send("I don't understand your wording! START OVER!")

bot = Bot(command_prefix='!', description='Hi')
@bot.event
async def bot_status():
  activity = discord.Game(name="!war", type=3)
  await Bot.change_presence(self=client,activity=activity)

class UpdateRCur():
  if "RedMoney" in db.keys():
    RedCurrency = db["RedMoney"]
    def redMin(amountRed):
      RedCurrency-=amountRed
      db["RedMoney"] = RedCurrency
    def redAdd(amountRPlus):
      RedCurrency+=amountRPlus
      RedCurrency+=amountRPlus
      db["RedMoney"]=RedCurrency
  else:
    db["RedMoney"]=1000
@client.event
async def shop_person(message,ident):
  userinput = await client.wait_for("message")
  await shop_input(userinput,ident)

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))
simulate=db["simulate"]
@client.event
async def on_message(message):
  global simulate
  if message.author == client.user:
    return
  if message.content.startswith('!simulateai'):
    simulate = db["simulate"]
    bool1 = message.content.split('simulateai ',1)[1]
    if bool1.lower() == 'false': 
      db["simulate"] = False
      simulate = db["simulate"]
    if bool1.lower() == 'true':
      db["simulate"] = True
      simulate = db["simulate"]
    await message.channel.send('simulateai is now')
    await message.channel.send(simulate)
    return
  if simulate:
    if message.content.startswith('!start'):
      await message.channel.send('!hi')
      db[simulate] = False
  msg = message.content
  if message.content.startswith('!threaten'):
    await message.channel.send('You have succesefuly threatened nobody!')
  if message.content.startswith('!war') or message.content.startswith('!War'):
    await message.channel.send('War has already started, dummy!')
  if message.content.startswith('!hi'):
    time.sleep(0.5)
    await message.channel.send('!how are you?')
  if message.content.startswith("!I'm"):
    time.sleep(0.5)
    ran1 = round(uniform(0,1))
    if ran1 == 0:
      await message.channel.send("!I'm alright, but my boss fired me.")
    elif ran1 == 1:
      await message.channel.send("!I'm great, I recently got a new house!")
  if message.content.startswith('!Oh'):
    time.sleep(1)
    await message.channel.send('*sigh*')
    time.sleep(2)
    await message.channel.send('Bye, I guess')
    time.sleep(0.5)
    await message.channel.send(':(')
    time.sleep(1)
    await message.channel.send('Why are you so casual about this?')
    db["simulate"] = True
  if message.content.startswith('!Thats'):
    time.sleep(0.5)
    await message.channel.send('Ok, bye!')
  if message.content.startswith('!shop'):
    if message.content.endswith == message.content.startswith:
      i = 0
    else:
      i = 1
    item = msg.split('!shop',i)[i]
    if item == '':
      await message.channel.send(shop)
      return
    if item == ' soldier' or item == " gun":
      await message.channel.send('do you REALLY wanna buy that? think about it. Type [y] for yes, [n] for no.')
      ident = message.author.name
      await shop_person(message,ident)
    else:
      await message.channel.send('we actually dont have that')
  if message.content.startswith('!invade'):
    invasion=round(r.uniform(0,1))
    if invasion == 1:
      await message.channel.send("Success! +1 trench!")
      #trenchs += 1
    else:
      await message.channel.send("Failure! -1 soldier!")
      #soldiers -= 1
  if message.content.startswith('!build'):
    buildwhat = msg.split('!build ',1)[1]
    if buildwhat == 'Trench' or buildwhat == 'trench':
      await message.channel.send('%alarm #war 30 Trench Complete!')
    else:
      await message.channel.send('I dunno what your talking about')
  if message.content.startswith('!message'):
    await message.channel.send('this is the pure message:')
    await message.channel.send(message)
    await message.channel.send('this is the traslated message:')
    await message.channel.send(message.content)
  await bot_status()
keep_alive()
client.run(my_secret)