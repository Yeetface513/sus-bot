from keep_alive import keep_alive
import discord.ext
import os
import discord
import requests
import json
from discord.ext import commands

client = commands.Bot()
my_secretx = os.environ['NINJA_API']


@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))
  await client.change_presence(status=discord.Status.online,
                               activity=discord.Game(name="your dad"))


@client.slash_command(name="hi", description="say hi to sus bot")
async def hi(ctx):
  await ctx.respond(content='good morning, meatbag')


@client.slash_command(name='joke', description="tell a joke")
async def joke(ctx):
  limit = 1
  api_url = 'https://api.api-ninjas.com/v1/jokes?limit={}'.format(limit)
  response = requests.get(api_url, headers={'X-Api-Key': my_secretx})

  cheese = json.loads(response.text)
  beans = str(cheese)
  chips = beans.replace("[{'joke': ", "")
  eat = chips.replace("}]", "")
  await ctx.respond(eat)


@client.slash_command(name='plane_facts',
                      description="tells you facts about a plane")
async def plane_facts(ctx, manufacturer_of_plane, plane_model):
  manufacturer = manufacturer_of_plane
  model = plane_model
  api_url = 'https://api.api-ninjas.com/v1/aircraft?manufacturer={}&model={}'.format(
    manufacturer, model)
  response = requests.get(api_url, headers={'X-Api-Key': my_secretx})
  await ctx.respond(response.text)


@client.slash_command(name="currency_conversion",
                      description="convert your currency!")
async def currency_conversion(ctx, starting_currency, amount, end_currency):
  api_url = f'https://api.api-ninjas.com/v1/convertcurrency?want={end_currency}&have={starting_currency}&amount={amount}'
  amogus = requests.get(api_url, headers={'X-Api-Key': my_secretx})
  await ctx.respond(f"the amount is {amogus.text}")

@client.slash_command(name="shrek",description="testing embeds")
async def embed(ctx):
  shrek=discord.Embed(title="SHREK", url="https://i0.wp.com/cambridge105.co.uk/wp-content/uploads/2022/07/Shrek-the-Musical.jpg?resize=900%2C506&ssl=1", description="your mum", color=0xFF5733)
  await ctx.send(embed=shrek)



keep_alive()

my_secret = os.environ['DISCORD_TOKEN']
client.run(my_secret)
