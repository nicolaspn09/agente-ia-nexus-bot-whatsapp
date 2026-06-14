from flask import Flask, request, jsonify
from services.waha import Waha
from bot.ai_bot import AIBot
import time
import random
import datetime

app = Flask(__name__)

@app.route("/chatbot/webhook/", methods=["POST"])

def webhook():
    pass # Logica de negocio removida por seguranca corporativa


if __name__ == "__main__":
     app.run(host = 'REMOVED', port=int(os.environ.get("PORT", 5000)), debug=True)
