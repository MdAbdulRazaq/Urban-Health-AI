import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

INPUT_FILE = os.path.join(BASE_DIR, "data", "processed", "health_data.csv")
OUTPUT_FILE = os.path.join(BASE_DIR, "data", "processed", "ml_ready.csv")

# ---------------- LOAD DATA ----------------
df = pd.read_csv(INPUT_FILE)
print("Loaded rows:", len(df))

# ---------------- AQI CALCULATION ----------------
def aqi_pm25(pm25):
    if pm25 <= 30: return 50
    elif pm25 <= 60: return 100
    elif pm25 <= 90: return 200
    elif pm25 <= 120: return 300
    elif pm25 <= 250: return 400
    else: return 500

def aqi_pm10(pm10):
    if pm10 <= 50: return 50
    elif pm10 <= 100: return 100
    elif pm10 <= 250: return 200
    elif pm10 <= 350: return 300
    elif pm10 <= 430: return 400
    else: return 500

def overall_aqi(row):
    return max(
        aqi_pm25(row["pm25"]),
        aqi_pm10(row["pm10"])
    )

df["aqi"] = df.apply(overall_aqi, axis=1)

# ---------------- MODEL FEATURES ----------------
MODEL_FEATURES = [
    "pm25",
    "pm10",
    "no2",
    "o3",
    "so2",
    "co",
    "temperature_x",
    "humidity_x",
    "pressure_x",
    "wind_speed_x"
]

FINAL_COLUMNS = (
    ["city"] +
    MODEL_FEATURES +
    ["latitude", "longitude", "aqi", "health_risk"]
)

# ---------------- VALIDATION ----------------
missing = set(FINAL_COLUMNS) - set(df.columns)
if missing:
    raise ValueError(f"Missing required columns: {missing}")

# ---------------- BUILD ML DATASET ----------------
ml_df = df[FINAL_COLUMNS].copy()

# ---------------- SAVE ----------------
ml_df.to_csv(OUTPUT_FILE, index=False)

print("✅ ml_ready.csv rebuilt successfully")
print("📁 Saved at:", OUTPUT_FILE)
print("\nPreview:")
print(ml_df.head())