import requests
from bs4 import BeautifulSoup
import datetime

def szombathely_data_structure():
    # This is the data we will send to the SQL database
    sample_data = {
        "date": datetime.date.today(),
        "city": "Szombathely",
        "district": "Olad",
        "price_huf": 42000000,
        "size_m2": 55,
        "rooms": 2,
        "property_type": "brick apartment"
    }
    
    # Calculated field for the portfolio:
    price_per_m2 = sample_data["price_huf"] / sample_data["size_m2"]
    
    print(f"New property listing: {sample_data['district']} - {sample_data['price_huf']} HUF")
    print(f"Calculated price per m2: {round(price_per_m2)} HUF/m2")

szombathely_data_structure()