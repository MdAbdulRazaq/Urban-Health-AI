import requests
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("WAQI_TOKEN")

CITIES = ["Delhi", "Kanpur", "Noida", "Ghaziabad", "Gurgaon"]

rows = []

for city in CITIES:
    print("Fetching:", city)
    url = f"https://api.waqi.info/feed/{city}/?token={TOKEN}"
    r = requests.get(url).json()

    if r["status"] != "ok":
        print("❌ Failed for", city)
        continue

    d = r["data"]
    iaqi = d["iaqi"]

    rows.append({
        "city": city,
        "pm25": iaqi.get("pm25", {}).get("v"),
        "pm10": iaqi.get("pm10", {}).get("v"),
        "no2": iaqi.get("no2", {}).get("v"),
        "o3": iaqi.get("o3", {}).get("v"),
        "so2": iaqi.get("so2", {}).get("v"),
        "co": iaqi.get("co", {}).get("v"),
        "temperature": iaqi.get("t", {}).get("v"),
        "humidity": iaqi.get("h", {}).get("v"),
        "pressure": iaqi.get("p", {}).get("v"),
        "wind_speed": iaqi.get("w", {}).get("v")
    })

os.makedirs("data/raw", exist_ok=True)
df = pd.DataFrame(rows)
file_path = "data/raw/pollution.csv"

# If file exists, append new data
if os.path.exists(file_path):
    old_df = pd.read_csv(file_path)
    df = pd.concat([old_df, df], ignore_index=True)

df.to_csv(file_path, index=False)


print("\n✅ pollution.csv updated (data accumulated)")
print("Total rows:", len(df))
