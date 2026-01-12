import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
data_path = os.path.join(BASE_DIR, "data", "processed", "health_data.csv")

df = pd.read_csv(data_path)

print("\nTop 5 rows:")
print(df.head())

# 1️⃣ Air pollution vs health risk
plt.figure(figsize=(10,6))
sns.boxplot(x="health_risk", y="pm25", data=df)
plt.title("PM2.5 vs Health Risk")
plt.savefig(os.path.join(BASE_DIR, "pm25_vs_health.png"))
plt.close()

# 2️⃣ Temperature vs health risk
plt.figure(figsize=(10,6))
sns.boxplot(x="health_risk", y="temperature_y", data=df)
plt.title("Temperature vs Health Risk")
plt.savefig(os.path.join(BASE_DIR, "temp_vs_health.png"))
plt.close()

# 3️⃣ Wind speed vs pollution
plt.figure(figsize=(10,6))
sns.scatterplot(x="wind_speed_y", y="pm25", hue="health_risk", data=df)
plt.title("Wind Speed vs PM2.5")
plt.savefig(os.path.join(BASE_DIR, "wind_vs_pm25.png"))
plt.close()

print("\n📊 Charts created:")
print("pm25_vs_health.png")
print("temp_vs_health.png")
print("wind_vs_pm25.png")
