import discord
from discord.ext import commands
import os

# Configuration des intents
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

# Initialisation du bot
bot = commands.Bot(command_prefix="h!", intents=intents)

# Nom du channel honeypot
HONEYPOT_CHANNEL_NAME = "honeypot"

@bot.event
async def on_ready():
    print(f'Connecté en tant que {bot.user} (ID: {bot.user.id})')
    print('------')

@bot.event
async def on_message(message):
    # Ignorer les messages du bot lui-même
    if message.author.bot:
        return

    # Vérifier si le message a été envoyé dans le channel honeypot
    if message.channel.name == HONEYPOT_CHANNEL_NAME:
        try:
            # Essayer de bannir l'utilisateur
            await message.author.ban(reason="A posté dans le channel Honeypot (Spam/Bot)")
            
            # Tenter de supprimer le message
            await message.delete()
            
            print(f"Banni : {message.author} pour avoir posté dans #{HONEYPOT_CHANNEL_NAME}")
        except discord.Forbidden:
            print(f"Erreur : Je n'ai pas les permissions pour bannir {message.author} ou supprimer son message.")
        except discord.HTTPException as e:
            print(f"Erreur HTTP lors du bannissement de {message.author}: {e}")
            
    await bot.process_commands(message)

@bot.command()
@commands.has_permissions(administrator=True)
async def setup_honeypot(ctx):
    """Crée le channel honeypot si ce n'est pas déjà fait"""
    existing_channel = discord.utils.get(ctx.guild.channels, name=HONEYPOT_CHANNEL_NAME)
    
    if existing_channel:
        await ctx.send(f"Le channel #{HONEYPOT_CHANNEL_NAME} existe déjà.")
        return
        
    # Créer le channel avec des permissions spécifiques
    # Les utilisateurs normaux peuvent le voir et écrire, mais pas lire l'historique
    overwrites = {
        ctx.guild.default_role: discord.PermissionOverwrite(read_messages=True, send_messages=True, read_message_history=False),
        ctx.guild.me: discord.PermissionOverwrite(read_messages=True, send_messages=True)
    }
    
    await ctx.guild.create_text_channel(HONEYPOT_CHANNEL_NAME, overwrites=overwrites, reason="Setup Honeypot")
    await ctx.send(f"Channel #{HONEYPOT_CHANNEL_NAME} créé avec succès ! Tout membre qui y poste sera banni.")

# Lancer le bot
if __name__ == "__main__":
    TOKEN = os.getenv("DISCORD_TOKEN", "TON_TOKEN_ICI")
    if TOKEN == "TON_TOKEN_ICI":
        print("Veuillez configurer votre token Discord.")
    else:
        bot.run(TOKEN)
