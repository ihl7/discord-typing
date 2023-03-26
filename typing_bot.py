import requests
import time

channel_id = "your_channel_id"
discord_token = "your_discord_token_here"
headers = {
    'authorization': f'{discord_token}'
}

while True:
    requests.post(f"https://discord.com/api/v9/channels/{channel_id}/typing", headers=headers)
    time.sleep(5)
