import streamlit as st
import pandas as pd
import joblib
import pydeck as pdk

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Urban Health AI",
    layout="wide"
)

# ---------------- STYLE ----------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif;
    background-color: #0e1117;
    color: #ffffff;
}

.title {
    text-align:center;
    font-size:42px;
    font-weight:700;
}

.subtitle {
    text-align:center;
    color:#9ca3af;
    margin-bottom:25px;
}

.card {
    background:linear-gradient(135deg,#1f2933,#111827);
    padding:22px;
    border-radius:14px;
    box-shadow:0 0 25px rgba(0,255,255,0.15);
    margin-bottom:25px;
}

.badge {
    padding:8px 16px;
    border-radius:20px;
    font-weight:600;
}

.low {background:#16a34a;}
.moderate {background:#facc15;color:black;}
.high {background:#f97316;}
.severe {background:#dc2626;}

hr {
    border:1px solid #1f2933;
}
</style>
""", unsafe_allow_html=True)

# ---------------- LOAD DATA & MODELS ----------------
df = pd.read_csv("data/processed/ml_ready.csv")
model = joblib.load("models/health_ai.pkl")
encoder = joblib.load("models/label_encoder.pkl")

# Normalize column names (safety)
df = df.rename(columns={
    "temperature_x": "temperature",
    "humidity_x": "humidity",
    "pressure_x": "pressure",
    "wind_speed_x": "wind_speed",
})

# 🔒 Model feature truth
MODEL_FEATURES = list(model.feature_names_in_)

# ---------------- TIME AXIS ----------------
df["day"] = df.groupby("city").cumcount()

# ---------------- AQI HELPERS ----------------
def aqi_category(aqi):
    if aqi <= 50: return "LOW", "low"
    elif aqi <= 100: return "MODERATE", "moderate"
    elif aqi <= 200: return "HIGH", "high"
    else: return "SEVERE", "severe"

def aqi_color(aqi):
    if aqi <= 50: return [22,163,74,200]
    elif aqi <= 100: return [250,204,21,200]
    elif aqi <= 200: return [249,115,22,200]
    else: return [220,38,38,200]

# ---------------- HEADER ----------------
st.markdown('<div class="title">🌍 Urban Health AI</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Interactive AI health risk prediction system</div>', unsafe_allow_html=True)

# ==================================================
# 🔴 EXECUTIVE SUMMARY (INSIGHT FIRST)
# ==================================================
st.subheader("🧠 Executive Summary")

col1, col2, col3 = st.columns(3)

col1.metric(
    "🚨 High Risk Cities",
    df[df["health_risk"] == "HIGH"]["city"].nunique()
)

col2.metric(
    "🌫 Avg PM2.5",
    round(df["pm25"].mean(), 1)
)

col3.metric(
    "📊 Avg AQI",
    int(df["aqi"].mean())
)


# ==================================================
# 🔵 SECTION 1 — EXISTING CITY (LEVEL 4 CONTINUED)
# ==================================================
st.subheader("🏙️ Existing City Monitoring")

city = st.selectbox("Select City", sorted(df["city"].unique()))
city_df = df[df["city"] == city]

max_day = city_df["day"].max()
selected_day = st.slider("Time (Day Index)", 0, int(max_day), int(max_day))

row = city_df[city_df["day"] == selected_day].iloc[-1:]

aqi = row["aqi"].values[0]
pm25 = row["pm25"].values[0]
pm10 = row["pm10"].values[0]

aqi_label, aqi_class = aqi_category(aqi)

st.markdown(f"""
<div class="card">
<h3>📍 City: {city.title()}</h3>
<h4>🌫️ PM2.5: {pm25}</h4>
<h4>🌪️ PM10: {pm10}</h4>
<h4>📊 AQI: {aqi}</h4>
<br>
<span class="badge {aqi_class}">{aqi_label} AQI</span>
</div>
""", unsafe_allow_html=True)

X_existing = row[MODEL_FEATURES]
pred_existing = model.predict(X_existing)[0]
risk_existing = encoder.inverse_transform([pred_existing])[0]

st.subheader("🏥 AI Health Risk (Existing City)")
if risk_existing == "LOW":
    st.success("🟢 LOW Health Risk")
elif risk_existing == "MODERATE":
    st.warning("🟡 MODERATE Health Risk")
else:
    st.error("🔴 HIGH Health Risk")

# ---------------- MAP ----------------
st.subheader("🗺️ AQI Map")

map_df = df[df["day"] == selected_day].dropna(subset=["latitude", "longitude"]).copy()
map_df["color"] = map_df["aqi"].apply(aqi_color)

layer = pdk.Layer(
    "ScatterplotLayer",
    data=map_df,
    get_position='[longitude, latitude]',
    get_radius=45000,
    get_fill_color="color",
    pickable=True
)

view_state = pdk.ViewState(
    latitude=22.5937,
    longitude=78.9629,
    zoom=4.4
)

st.pydeck_chart(
    pdk.Deck(
        layers=[layer],
        initial_view_state=view_state,
        tooltip={
            "html": "<b>{city}</b><br>AQI: {aqi}<br>PM2.5: {pm25}<br>PM10: {pm10}",
            "style": {"color": "white"}
        }
    )
)

# ==================================================
# 💡 KEY INSIGHTS
# ==================================================
st.subheader("💡 Key Insights")

st.info("PM2.5 is the dominant contributor to HIGH health risk across all monitored cities.")
st.warning("Low wind speed and high humidity conditions intensify pollution exposure.")
st.success("Tier-2 cities show pollution levels approaching metro-city risk thresholds.")


# ==================================================
# 🔵 SECTION 2 — USER INPUT PREDICTION (LEVEL 5)
# ==================================================
st.markdown("<hr>", unsafe_allow_html=True)
st.subheader("🧠 Predict Health Risk for ANY City")

with st.form("manual_prediction"):
    user_city = st.text_input("City Name (any city)")
    
    inputs = {}
    for feature in MODEL_FEATURES:
        inputs[feature] = st.number_input(
            f"{feature}",
            value=float(df[feature].mean())
        )

    submitted = st.form_submit_button("🔮 Predict Health Risk")

if submitted:
    input_df = pd.DataFrame([inputs])
    pred = model.predict(input_df)[0]
    risk = encoder.inverse_transform([pred])[0]

    st.subheader(f"🏥 Prediction for {user_city or 'Custom City'}")

    if risk == "LOW":
        st.success("🟢 LOW Health Risk")
    elif risk == "MODERATE":
        st.warning("🟡 MODERATE Health Risk")
    else:
        st.error("🔴 HIGH Health Risk")

# ---------------- TREND ----------------
st.markdown("<hr>", unsafe_allow_html=True)
st.subheader("📈 Pollution Trend (Selected City)")
st.line_chart(city_df.set_index("day")[["pm25", "pm10"]])

# ==================================================
# 🧭 RECOMMENDED ACTIONS
# ==================================================
st.subheader("🧭 Recommended Actions")

st.markdown("""
- Prioritize PM2.5 emission controls in HIGH-risk cities  
- Deploy early-warning alerts during low-wind conditions  
- Expand continuous monitoring to Tier-2 urban regions  
- Support healthcare preparedness in pollution hotspots  
""")
