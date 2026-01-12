# 🌍 Urban Health AI

Urban Health AI is an end-to-end machine learning system that predicts health risk levels in cities using air pollution and weather data.

The project combines real-world environmental data, AQI calculation, machine learning, and an interactive dashboard deployed on the cloud.

---

## 🚀 Key Features

- 📡 Pollution data ingestion (PM2.5, PM10, NO₂, SO₂, CO, O₃)
- 🌦️ Weather data integration
- 📊 AQI calculation using PM2.5 & PM10
- 🧠 Machine Learning health risk prediction
- 🗺️ Interactive India map with AQI-based coloring
- ⏱️ Time-based pollution trend analysis
- ✍️ Manual user input for predicting any city
- ☁️ Cloud deployment with Streamlit

---

## 🧠 Tech Stack

- **Language:** Python  
- **Data Processing:** Pandas, NumPy  
- **Machine Learning:** Scikit-learn  
- **Dashboard:** Streamlit  
- **Visualization:** PyDeck  
- **APIs:** OpenAQ, Weather APIs  

---

## 📊 Dashboard Capabilities

- Select a city and view pollution metrics
- See AQI classification and health risk
- Visualize pollution trends over time
- Explore AQI on an interactive India map
- Enter custom data to predict health risk for any city

---

## 🏥 Health Risk Categories

- 🟢 LOW  
- 🟡 MODERATE  
- 🔴 HIGH  

Predictions are generated using a trained machine learning model.

---

## ▶️ Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py


👤 Author

Abdul Razaq
Final Year B.Tech — Computer Science Engineering (Data Science)