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


class TimeoutView(discord.ui.View):

    foo = None

    async def disable_all_items(self):
        for item in self.children:
            item.disabled = True

        await self.message.edit(view=self)   
        




    async def on_timeout(self) -> None:
        await self.message.channel.send("Timeout")
        await self.disable_all_items()


    @discord.ui.button(label="Hello")
    async def hello(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("Hello World")
        self.foo = True
        self.stop()

    @discord.ui.button(label = "Cancel", style=discord.ButtonStyle.red)
    async def cancel(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("Cancelling")
        self.foo = False


 
 
          
        
    


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

     view = TimeoutView(timeout=5)

     message = await ctx.send(view=view)
     view.message = message
     await view.wait()
     await view.disable_all_items()


  
     await ctx.send(view=view)

     if view.foo is None:
         print("Timeout")
     elif view.foo == True:
         print("ok")
     else:
         print("cancel")        



    
     



#testibng

     

    






bot.run(TOKEN)

