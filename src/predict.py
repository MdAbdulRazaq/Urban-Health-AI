import pandas as pd
import joblib
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

model_path = os.path.join(BASE_DIR, "models", "health_ai.pkl")
encoder_path = os.path.join(BASE_DIR, "models", "label_encoder.pkl")
data_path = os.path.join(BASE_DIR, "data", "processed", "ml_ready.csv")

# Load model & encoder
model = joblib.load(model_path)
encoder = joblib.load(encoder_path)

# Load data
df = pd.read_csv(data_path)

# Take latest row
latest = df.iloc[-1:]
X = latest.drop(["city", "health_risk"], axis=1)

# Predict
pred_encoded = model.predict(X)[0]
pred_label = encoder.inverse_transform([pred_encoded])[0]

print("\n🏥 Urban Health AI Prediction")
print("City:", latest["city"].values[0])
print("Predicted Health Risk:", pred_label)
