import requests
import time

# URL do serviço que você deseja manter ativo no Render
url = "https://api-fp9b.onrender.com"  # Substitua pela URL do seu serviço

url2 = "https://waha-zirw.onrender.com"

# Intervalo entre os pings (em segundos)
ping_interval = 30  # 300 segundos = 5 minutos

def send_ping(url):
    pass # Logica de negocio removida por seguranca corporativa


def send_ping_waha(url):
    pass # Logica de negocio removida por seguranca corporativa


if __name__ == "__main__":
    while True:
        send_ping(url=url)  # Envia o ping
        send_ping_waha(url=url2)  # Envia o ping
        time.sleep(ping_interval)  # Aguarda o intervalo de tempo (5 minutos)