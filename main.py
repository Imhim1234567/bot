import discord
from dotenv import load_dotenv
from discord.ext import commands
import os

load_dotenv()

TOKEN = os.getenv("TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="$", intents=intents)



class SimpleView(discord.ui.View):

    @discord.ui.button(label="Hello")
    async def hello(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("Hello World")

        @discord.ui.button(label = "Cancel", style=discord.ButtonStyle.red)
        async def cancel(self, interaction: discord.Interaction, button: discord.ui.Button):
            await interaction.response.send_message("Cancelling")
    


def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

@bot.command()
async def calculate(ctx, num1, operation, num2):
    a = int(num1)
    b = int(num2)

    if operation == "+":
        output = add(a, b)
    elif operation == "-":
        output = subtract(a, b)
    elif operation == "*":
        output = multiply(a, b)
    elif operation == "/":
        output = divide(a, b)
    else:
        await ctx.send("Invalid operation")
        return
    
    await ctx.send(output)


@bot.command
async def button(ctx):
     #a = int(num1)
     #b = int(num2)

     view = SimpleView()
  
     await ctx.send(view=view)

    
     



#testibng

     

    






bot.run(TOKEN)

