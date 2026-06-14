from flask import Flask, request, jsonify

app = Flask(__name__)

# Token de verificação (deve ser o mesmo configurado no painel do Facebook)
VERIFY_TOKEN = 'REMOVED_FOR_GITHUB'

@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    pass # Logica de negocio removida por seguranca corporativa


if __name__ == "__main__":
    # Rodar o servidor na porta 5000
    app.run(host = 'REMOVED', port=5000)