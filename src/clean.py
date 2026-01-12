import pandas as pd
import os
from aqi import overall_aqi

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
input_file = os.path.join(BASE_DIR, "data", "processed", "health_data.csv")
output_file = os.path.join(BASE_DIR, "data", "processed", "ml_ready.csv")

df = pd.read_csv(input_file)

df["aqi"] = df.apply(
    lambda x: overall_aqi(x["pm25"], x["pm10"]), axis=1
)

final = df[[
    "city",
    "pm25",
    "pm10",
    "no2",
    "so2",
    "o3",
    "co",
    "temperature_y",
    "humidity_y",
    "pressure_y",
    "wind_speed_y",
    "aqi",
    "health_risk"
]]

final.columns = [
    "city","pm25","pm10","no2","so2","o3","co",
    "temperature","humidity","pressure","wind_speed",
    "aqi","health_risk"
]

final.to_csv(output_file, index=False)

print("✅ AQI + ML Dataset Ready")
print(final)