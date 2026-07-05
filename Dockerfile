FROM python:3.11-slim

WORKDIR /app

# Installer les dépendances système
RUN apt-get update && apt-get install -y --no-install-recommends \
    git \
    && rm -rf /var/lib/apt/lists/*

# Copier les fichiers de dépendances
COPY requirements.txt .

# Installer les dépendances Python
RUN pip install --no-cache-dir -r requirements.txt

# Copier les fichiers des bots
COPY zeeplin_bot.py .
COPY belugang_bot.py .
COPY honeypot_bot.py .

# Créer un script de démarrage
RUN echo '#!/bin/bash\n\
echo "Démarrage des bots Discord..."\n\
python3 zeeplin_bot.py &\n\
ZEEPLIN_PID=$!\n\
python3 belugang_bot.py &\n\
BELUGANG_PID=$!\n\
python3 honeypot_bot.py &\n\
HONEYPOT_PID=$!\n\
\n\
echo "Tous les bots sont en cours d'\''exécution..."\n\
wait $ZEEPLIN_PID $BELUGANG_PID $HONEYPOT_PID' > start.sh && chmod +x start.sh

# Commande de démarrage
CMD ["./start.sh"]
