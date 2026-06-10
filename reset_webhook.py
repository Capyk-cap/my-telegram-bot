import os
import requests

TOKEN = "8654250066:AAHZ6LBm5qjkgVHYk415fM-LMP-FKX84psc"

url = f"https://api.telegram.org/bot{TOKEN}/deleteWebhook?drop_pending_updates=True"
response = requests.get(url)
print(response.json())
