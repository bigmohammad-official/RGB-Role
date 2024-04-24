#Code by bigmohammad
#---------------------
#Youtube: bigmohammad
#---------------------
#Instagram: bigmohammad.official

import discord
import random
import asyncio

# Replace with your bot token
TOKEN = 'Token_Bot_Here'

# Guild ID and role ID
GUILD_ID = 1111111111111111 
ROLE_ID = 22222222222222222  # Your role ID here

# Create an instance of the Discord client
intents = discord.Intents.default()
intents.guilds = True  # Enable guild-related events
intents.messages = False  # We don't need message-related events for this example

# Create an instance of the Discord client with intents
client = discord.Client(intents=intents)

# Task to change the role color randomly every 3 seconds
async def change_role_color():
    guild = client.get_guild(GUILD_ID)
    role = guild.get_role(ROLE_ID)
    while True:
        # Generate a random color
        color = discord.Color(random.randint(0, 0xFFFFFF))

        # Edit the role color
        await role.edit(color=color)

        # Wait for 3 seconds
        await asyncio.sleep(3)

# When the bot is ready to work
@client.event
async def on_ready():
    print(f'Bot {client.user} has connected.')

    # Start changing the role color randomly
    client.loop.create_task(change_role_color())

# Run the bot with the provided token
client.run(TOKEN)
