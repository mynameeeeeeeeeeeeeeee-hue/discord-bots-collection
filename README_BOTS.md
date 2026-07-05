# Guide des 3 Bots Discord

## Prérequis

Avant de lancer les bots, installe la bibliothèque `discord.py` :

```bash
pip install discord.py
```

---

## 1. Bot Zeeplin

**Fichier :** `zeeplin_bot.py`  
**Préfixe :** `!`

### Commandes disponibles

| Commande | Description |
|----------|-------------|
| `!ping` | Répond avec "Pong!" |
| `!hello` | Dit bonjour à l'utilisateur |

### Lancer le bot

```bash
DISCORD_TOKEN=TON_TOKEN python3 zeeplin_bot.py
```

---

## 2. Bot BeluGANG Events

**Fichier :** `belugang_bot.py`  
**Préfixe :** `b!`

Ce bot gère un système d'XP et de Belubucks. Les membres gagnent de l'XP en chattant, et montent de niveau automatiquement.

### Commandes disponibles

| Commande | Description | Permission |
|----------|-------------|------------|
| `b!rank` | Affiche ton niveau et ton XP | Tout le monde |
| `b!belubucks` | Affiche ton solde de Belubucks | Tout le monde |
| `b!give_belubucks @user montant` | Donne des Belubucks à un membre | Admin seulement |

### Lancer le bot

```bash
DISCORD_TOKEN=TON_TOKEN python3 belugang_bot.py
```

---

## 3. Bot Honeypot

**Fichier :** `honeypot_bot.py`  
**Préfixe :** `h!`

Ce bot surveille un channel `#honeypot`. Tout utilisateur qui y envoie un message est automatiquement **banni** du serveur.

### Commandes disponibles

| Commande | Description | Permission |
|----------|-------------|------------|
| `h!setup_honeypot` | Crée le channel #honeypot | Admin seulement |

### Permissions requises
- Ban Members
- Manage Channels
- Read Messages
- Send Messages

### Lancer le bot

```bash
DISCORD_TOKEN=TON_TOKEN python3 honeypot_bot.py
```

---

## Comment obtenir un Token Discord

1. Va sur [Discord Developer Portal](https://discord.com/developers/applications)
2. Clique sur **New Application**
3. Donne un nom à ton bot (ex: Zeeplin, BeluGANG Events, Honeypot)
4. Va dans **Bot** > **Reset Token** pour obtenir ton token
5. Active les **Privileged Gateway Intents** : `SERVER MEMBERS INTENT` et `MESSAGE CONTENT INTENT`
6. Pour inviter le bot : va dans **OAuth2 > URL Generator**, coche `bot`, puis les permissions nécessaires

> **Important :** Ne partage jamais ton token Discord publiquement. Si un token est exposé, régénère-le immédiatement.
