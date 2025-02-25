import time
import requests

# Replace with your actual Render app URL
URL = "https://character-prototyping.onrender.com"

def keep_alive():
    while True:
        try:
            response = requests.get(URL)
            print(f"Pinged {URL}, Status Code: {response.status_code}")
        except Exception as e:
            print(f"Error pinging {URL}: {e}")
        time.sleep(600)  # Sleep for 10 minutes (600 seconds)

if __name__ == "__main__":
    keep_alive()
