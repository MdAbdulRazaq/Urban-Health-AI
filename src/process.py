import pandas as pd
import os

# ---------- PATH SETUP ----------
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW = os.path.join(BASE_DIR, "data", "raw")
PROCESSED = os.path.join(BASE_DIR, "data", "processed")

pollution_path = os.path.join(RAW, "pollution.csv")
weather_path = os.path.join(RAW, "weather.csv")

# ---------- LOAD DATA ----------
pollution = pd.read_csv(pollution_path)
weather = pd.read_csv(weather_path)

print("Pollution rows:", len(pollution))
print("Weather rows:", len(weather))

# ---------- CLEAN ----------
pollution["city"] = pollution["city"].str.lower().str.strip()
weather["city"] = weather["city"].str.lower().str.strip()

# Convert pollution to numeric
for col in ["pm25","pm10","no2","so2","o3","co"]:
    pollution[col] = pd.to_numeric(pollution[col], errors="coerce")

# ---------- MERGE ----------
data = pd.merge(pollution, weather, on="city", how="inner")

print("Merged rows:", len(data))

# ---------- HEALTH RISK ENGINE ----------
def health_risk(row):
    score = 0
    
    if row["pm25"] > 60: score += 3
    elif row["pm25"] > 30: score += 2
    
    if row["pm10"] > 100: score += 3
    elif row["pm10"] > 50: score += 2
    
    if row["no2"] > 40: score += 1
    if row["so2"] > 20: score += 1
    if row["o3"] > 100: score += 1
    
    if score >= 7:
        return "EXTREME"
    elif score >= 5:
        return "HIGH"
    elif score >= 3:
        return "MODERATE"
    else:
        return "LOW"

data["health_risk"] = data.apply(health_risk, axis=1)

# ---------- SAVE ----------
os.makedirs(PROCESSED, exist_ok=True)
output = os.path.join(PROCESSED, "health_data.csv")
data.to_csv(output, index=False)

print("✅ Health dataset created successfully")
print("📁", output)
print("\n📊 Preview:")
print(data)
