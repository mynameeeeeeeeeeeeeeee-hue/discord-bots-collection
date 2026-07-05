import discord
from discord.ext import commands
import os

# Configuration des intents
intents = discord.Intents.default()
intents.message_content = True

# Initialisation du bot
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Connecté en tant que {bot.user} (ID: {bot.user.id})')
    print('------')

@bot.command()
async def ping(ctx):
    """Répond avec Pong!"""
    await ctx.send('Pong! 🏓')

@bot.command()
async def hello(ctx):
    """Dit bonjour à l'utilisateur"""
    await ctx.send(f'Bonjour {ctx.author.mention} ! Je suis Zeeplin.')

# Lancer le bot
if __name__ == "__main__":
    # Le token doit être défini dans les variables d'environnement ou remplacé ici
    TOKEN = os.getenv("DISCORD_TOKEN", "TON_TOKEN_ICI")
    if TOKEN == "TON_TOKEN_ICI":
        print("Veuillez configurer votre token Discord.")
    else:
        bot.run(TOKEN)
