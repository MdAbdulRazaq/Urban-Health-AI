import requests
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENWEATHER_API_KEY")

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW_PATH = os.path.join(BASE_DIR, "data", "raw")

cities = [
    ("Delhi", 28.6139, 77.2090),
    ("Noida", 28.5355, 77.3910),
    ("Ghaziabad", 28.6692, 77.4538),
    ("kanpur", 26.4499, 80.3319),
    ("Gurgaon", 28.4595, 77.0266),
]

rows = []

for city, lat, lon in cities:
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&units=metric"
    res = requests.get(url).json()

    rows.append({
        "city": city,
        "latitude": lat,
        "longitude": lon,
        "temperature": res["main"]["temp"],
        "humidity": res["main"]["humidity"],
        "pressure": res["main"]["pressure"],
        "wind_speed": res["wind"]["speed"]
    })

df = pd.DataFrame(rows)
df.to_csv(os.path.join(RAW_PATH, "weather.csv"), index=False)

print("✅ Weather data saved with coordinates")
