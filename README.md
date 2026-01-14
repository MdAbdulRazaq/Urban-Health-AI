# 🌍 Urban Health AI  
**AI-powered Urban Pollution & Health Risk Intelligence System**

🔗 **Live Dashboard:** https://urban-health-ai-6c99xodfe3gofwcac5btzh.streamlit.app/  
📂 **Tech Stack:** Python, Pandas, Scikit-learn, APIs, Streamlit, Git, Cloud  

---

## 📌 Problem Statement
Urban air pollution is a growing public health concern in Indian cities.  
While pollution data exists, **decision-makers lack actionable insights** that connect pollution levels with **health risk outcomes**.

Most datasets remain:
- Fragmented (weather ≠ pollution ≠ health)
- Static (CSV-level analysis)
- Non-interactive (no real-time interpretation)

---

## 🎯 Objective
Build an **end-to-end system** that:
- Collects live pollution & weather data
- Converts raw data into health risk signals
- Predicts health risk using Machine Learning
- Presents insights through an interactive dashboard
- Is deployable and publicly accessible

---

## 🏗️ System Architecture
APIs (Pollution + Weather)
↓
Data Cleaning & Feature Engineering
↓
AQI Computation
↓
ML Health Risk Model
↓
Interactive Dashboard (Streamlit)
↓
Cloud Deployment

---

## 📊 Data Sources
- **Air Pollution:** OpenAQ API  
- **Weather:** OpenWeather API  
- **Cities Covered:** Delhi, Noida, Ghaziabad, Gurgaon, Kanpur  

Features include:
- PM2.5, PM10, NO₂, SO₂, CO
- Temperature, Humidity, Pressure, Wind Speed
- Latitude & Longitude (for spatial analysis)

---

## ⚙️ Feature Engineering
- Computed **AQI** using PM2.5 & PM10 breakpoints
- Standardized feature names to avoid model drift
- Handled missing values & inconsistent API responses
- Created time-indexed records for trend analysis

---

## 🤖 Machine Learning Model
- **Model:** Random Forest Classifier
- **Target:** Health Risk (LOW / MODERATE / HIGH)
- **Input Features:** Pollution + Weather + AQI
- **Reason:** Robust to non-linearity and noisy environmental data

---

## 📈 Key Metrics & KPIs
| Metric | Insight |
|------|--------|
| Avg PM2.5 | Consistently above WHO safe limits |
| Avg AQI | Majority cities fall in HIGH category |
| High-Risk Cities | 100% of monitored cities |
| Dominant Factor | PM2.5 strongest contributor |
| Trend | Pollution spikes during low wind |

---

## 🧠 Insights Generated
- PM2.5 is the **primary driver** of health risk
- Low wind speed increases pollution retention
- Tier-2 cities show risk levels close to metros
- Weather conditions amplify pollution impact

---

## 🗺️ Dashboard Capabilities
- City-wise AQI & pollution monitoring
- Time slider to observe pollution trends
- Interactive India map with AQI heat points
- AI-based health risk prediction
- Manual input for any city (what-if analysis)

---

## 🚀 Deployment
- Hosted on **Streamlit Cloud**
- CI-ready repository
- Secure environment variables
- Public access for recruiters & stakeholders

---

## 🧩 Challenges Solved
- API version deprecations (OpenAQ v1 → v3)
- Feature mismatch between training & inference
- Real-time deployment bugs
- Cloud dependency resolution

---

## 👤 Author
**MD ABDUL RAZAQ**  
B.Tech (CSE – Data Science)  
4th Year - 8th Semester
Noida International University
