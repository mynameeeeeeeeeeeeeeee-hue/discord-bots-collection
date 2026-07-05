import discord
from discord.ext import commands
import os
import json

# Configuration des intents
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

# Initialisation du bot
bot = commands.Bot(command_prefix="b!", intents=intents)

# Fichier pour stocker les données XP et Belubucks
DATA_FILE = "belugang_data.json"

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return {}

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

@bot.event
async def on_ready():
    print(f'Connecté en tant que {bot.user} (ID: {bot.user.id})')
    print('------')

@bot.event
async def on_message(message):
    if message.author.bot:
        return

    # Système d'XP
    data = load_data()
    user_id = str(message.author.id)
    
    if user_id not in data:
        data[user_id] = {"xp": 0, "level": 1, "belubucks": 0}
    
    # Ajouter de l'XP
    data[user_id]["xp"] += 5
    
    # Vérifier le passage de niveau
    current_level = data[user_id]["level"]
    xp_needed = current_level * 100
    
    if data[user_id]["xp"] >= xp_needed:
        data[user_id]["level"] += 1
        data[user_id]["xp"] -= xp_needed
        await message.channel.send(f'🎉 Bravo {message.author.mention}, tu as atteint le niveau {data[user_id]["level"]} !')
    
    save_data(data)
    await bot.process_commands(message)

@bot.command()
async def rank(ctx):
    """Affiche ton niveau et ton XP"""
    data = load_data()
    user_id = str(ctx.author.id)
    
    if user_id in data:
        xp = data[user_id]["xp"]
        level = data[user_id]["level"]
        await ctx.send(f'📊 {ctx.author.name}, tu es niveau {level} avec {xp} XP.')
    else:
        await ctx.send(f"Tu n'as pas encore d'XP.")

@bot.command()
async def belubucks(ctx):
    """Affiche ton solde de Belubucks"""
    data = load_data()
    user_id = str(ctx.author.id)
    
    if user_id in data:
        bucks = data[user_id]["belubucks"]
        await ctx.send(f'💸 {ctx.author.name}, tu as {bucks} Belubucks.')
    else:
        await ctx.send(f"Tu n'as pas de Belubucks.")

@bot.command()
@commands.has_permissions(administrator=True)
async def give_belubucks(ctx, member: discord.Member, amount: int):
    """Donne des Belubucks à un utilisateur (Admin seulement)"""
    data = load_data()
    user_id = str(member.id)
    
    if user_id not in data:
        data[user_id] = {"xp": 0, "level": 1, "belubucks": 0}
        
    data[user_id]["belubucks"] += amount
    save_data(data)
    
    await ctx.send(f'✅ {amount} Belubucks ont été ajoutés au compte de {member.name}.')

# Lancer le bot
if __name__ == "__main__":
    TOKEN = os.getenv("DISCORD_TOKEN", "TON_TOKEN_ICI")
    if TOKEN == "TON_TOKEN_ICI":
        print("Veuillez configurer votre token Discord.")
    else:
        bot.run(TOKEN)
