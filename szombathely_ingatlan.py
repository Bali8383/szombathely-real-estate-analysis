import requests
from bs4 import BeautifulSoup

def fetch_szombathely_real_estate():
    # Example URL (important: check the site's robots.txt in reality!)
    url = "https://www.ingatlan.com/szombathely" 
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    print(f"Fetching data from: {url}...")
    
    # Sending the request to the website here
    # Note: This is an example, in a real scenario you need to adjust selectors to the site's HTML structure.
    try:
        # response = requests.get(url, headers=headers)
        # soup = BeautifulSoup(response.text, 'html.parser')
        
        print("\n--- Szombathely Real Estate Portfolio Project ---")
        print("Status: Connection successful (Simulation)")
        
        # Example data structure to be loaded into SQL later:
        properties = [
            {"location": "City Center area", "price": "45.000.000 HUF", "size": "62 m2"},
            {"location": "Olad residential area", "price": "38.500.000 HUF", "size": "54 m2"},
            {"location": "Kámon district", "price": "82.000.000 HUF", "size": "120 m2"}
        ]
        
        for prop in properties:
            print(f"Location: {prop['location']} | Price: {prop['price']} | Size: {prop['size']}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    fetch_szombathely_real_estate()