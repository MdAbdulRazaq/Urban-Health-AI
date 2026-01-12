# 🌍 Urban Health AI — Pollution-Based Health Risk Prediction

Urban Health AI is an end-to-end machine learning system that transforms air pollution and weather data into actionable public health insights for Indian cities.

---

## 🚀 Key Features

- Real-world air pollution and weather data ingestion
- AQI computation using PM2.5 and PM10 standards
- Machine learning–based health risk classification
- Interactive Streamlit dashboard with:
  - City-wise monitoring
  - Time-based pollution trends
  - India-wide AQI map visualization
  - Manual prediction for any city
- Cloud deployment with secure configuration

---

## 🧠 Technology Stack

**Programming:** Python  
**Data Processing:** Pandas, NumPy  
**Machine Learning:** Scikit-learn (Random Forest)  
**Visualization:** Streamlit, PyDeck  
**APIs:** OpenAQ, OpenWeather  
**Deployment:** GitHub, Streamlit Cloud  

---

## 📊 Use Cases

- Urban public health monitoring  
- Air pollution impact analysis  
- Healthcare preparedness planning  
- Environmental policy support  

---

## 🌐 Live Application

🔗 **Live Demo:**  
https://urban-health-ai-6c99xodfe3gofwcac5btzh.streamlit.app/

---

## 🧩 Project Architecture

Urban Health AI/
├── app.py # Streamlit dashboard
├── data/
│ ├── raw/ # Raw pollution & weather data
│ └── processed/ # ML-ready datasets
├── models/
│ ├── health_ai.pkl # Trained ML model
│ └── label_encoder.pkl
├── src/
│ ├── pollution.py # Pollution data ingestion
│ ├── weather.py # Weather data ingestion
│ ├── process.py # Data merging & labeling
│ ├── prepare_ml_data.py # Feature preparation
│ ├── train.py # Model training
│ └── aqi.py # AQI calculation logic
├── requirements.txt
└── README.md


---

## ⚠️ Important Note

This project is **insight-driven**, not dataset-driven.  
The focus is on converting environmental data into **decision-ready health intelligence**, similar to real-world data science systems.

---

## 👤 Author

**Md Abdul Razaq**  
B.Tech CSE (Data Science)  
Urban Health AI — 2026
