import time
import requests

# List of Render app URLs to keep alive
URLS = [
    "https://character-prototyping.onrender.com",
    "https://character-prototyping-1.onrender.com",
    "https://character-prototyping-2.onrender.com",
    "https://pm-tutorial-3.onrender.com",
     "https://pm-tutorial-2.onrender.com"
]

def keep_alive():
    while True:
        for url in URLS:
            try:
                response = requests.get(url)
                print(f"Pinged {url}, Status Code: {response.status_code}")
            except Exception as e:
                print(f"Error pinging {url}: {e}")
        time.sleep(600)  # Sleep for 10 minutes (600 seconds)

if __name__ == "__main__":
    keep_alive()
