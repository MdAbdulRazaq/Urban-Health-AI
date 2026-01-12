import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import classification_report
import joblib
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
data_file = os.path.join(BASE_DIR, "data", "processed", "ml_ready.csv")
model_file = os.path.join(BASE_DIR, "models", "health_ai.pkl")
encoder_file = os.path.join(BASE_DIR, "models", "label_encoder.pkl")

df = pd.read_csv(data_file)

# Encode target properly
encoder = LabelEncoder()
df["health_risk_encoded"] = encoder.fit_transform(df["health_risk"])

X = df.drop(["city", "health_risk", "health_risk_encoded"], axis=1)
y = df["health_risk_encoded"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

pred = model.predict(X_test)
print("\n📊 Model Report")
print(classification_report(y_test, pred))

os.makedirs(os.path.join(BASE_DIR, "models"), exist_ok=True)

joblib.dump(model, model_file)
joblib.dump(encoder, encoder_file)

print("\n✅ Model and encoder saved")
