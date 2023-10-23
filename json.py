import discord
from dotenv import load_dotenv
from discord.ext import commands
import os
import json; import random

load_dotenv()

TOKEN = os.getenv("TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

def load_num(num):
    with open("num.json", "r") as f:
        data = json.load(f)

        data["num"] = None


        with open("num.json", 'w') as f:
            json.dump(data,f, indent = 2)


load_num(None)            

with open("quotes.json", "r") as  json_file:
        quotes_data = json.load(json_file)


def get_random_quote():
    random_quote = random.choice(quotes_data)
    return f'"{random_quote["quote"]}" - {random_quote["author"]}'
     



@bot.command()
async def num_store(ctx,num):
    load_num(num)
    await ctx.send("Num saved as {num}!")


@bot.command()
async def print_num(ctx):
    with open("num.json", "r") as f:
        data = json.load(f)

    cool_num = data["num"] = None

    await ctx.send(f"The num is {cool_num}") 

@bot.command
async def quote(ctx):
     quote = get_random_quote()
     await ctx.send(quote)   
     
        
