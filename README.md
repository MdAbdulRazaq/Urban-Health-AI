🏙️ Urban Health AI — A Production-Ready Data & AI Case Study

## 📌 Project Overview

Urban Health AI is an end-to-end data science and machine learning platform designed to translate urban air-pollution data into actionable public-health insights.

The system ingests pollution and weather data, computes Air Quality Index (AQI), predicts population health risk using machine learning, and presents insights through an interactive, cloud-deployed dashboard.

This project was intentionally built to simulate real-world production challenges, including unreliable APIs, evolving data schemas, feature inconsistencies, and cloud deployment constraints — not just ideal classroom conditions.

🔗 Live Application:
https://urban-health-ai-6c99xodfe3gofwcac5btzh.streamlit.app/

🔗 Source Code:
GitHub Repository

---

## 🎯 Business Problem

Urban populations are increasingly exposed to hazardous air quality, yet decision-makers often lack clear, city-level health risk intelligence that connects pollution metrics to real health outcomes.

Most available data remains:

Fragmented across multiple sources

Difficult to interpret for non-technical stakeholders

Static, with limited real-time or predictive insight

Urban Health AI addresses this gap by converting raw environmental data into interpretable health-risk signals that can support planning, preparedness, and policy discussions.

This project answers:

Which cities face the highest health risk today?

How does air quality evolve over time?

Can health risk be predicted for cities with limited historical data?

How can such a system operate reliably in production?

---

## 🧠 Solution Architecture
High-Level Pipeline

External APIs → Pollution & Weather data ingestion

Data cleaning, validation, and normalization

AQI computation using PM2.5 and PM10 standards

Feature engineering for machine learning

Health risk classification using an ML model

Interactive visualization via Streamlit

Cloud deployment for public accessibility

This modular architecture allows each stage to be debugged, scaled, or upgraded independently.

---

## 📊 Key Metrics & KPIs (Analyst-Grade)

Metric	Insight
Average PM2.5	Indicates long-term respiratory exposure risk
AQI Severity Distribution	Primary driver of health risk classification
High-Risk City Percentage	Identifies priority intervention zones
Model Prediction Consistency	Validates reliability across environments
Feature Stability	Ensures safe production inference

---

## 🧭 Model Interpretation & Insights

PM2.5 emerged as the strongest contributor to HIGH health risk

Low wind speed combined with high humidity amplifies pollution exposure

Several Tier-2 cities exhibit pollution severity approaching metro-level risk

These insights shift the conversation from “raw pollution numbers” to health-oriented decision intelligence.

---

🚧 Production Considerations (Advanced)

This section documents the real-world engineering and data science challenges encountered while building and deploying the system, along with the design decisions taken to ensure reliability, stability, and production readiness.

---

## 🔄 API Reliability & Failure Handling

Challenge:
External APIs (OpenAQ and weather services) frequently returned:

401 Unauthorized

404 Not Found

Inconsistent or missing response fields

Approach:

Implemented defensive JSON parsing with key-existence checks

Validated HTTP status codes before processing

Designed graceful fallbacks instead of pipeline failures

Outcome:
✔ The data pipeline remains stable even when APIs behave unpredictably.

---

## 🧩 Feature Mismatch Resolution (Critical Issue)

Challenge:
The ML model failed during inference due to mismatched features:

Extra features introduced during visualization (e.g., aqi, latitude)

Missing features expected by the trained model

Approach:

Locked the feature contract using:

model.feature_names_in_


Enforced strict feature selection before prediction

Unified training and inference schemas

Outcome:
✔ Zero feature-related prediction failures in production.

---

## 🧪 Data Consistency Strategy

Normalized inconsistent column names (e.g., temperature_x → temperature)

Centralized feature engineering logic

Established ml_ready.csv as a single source of truth

Outcome:
✔ Prevented silent data corruption and ensured reproducibility.

---

## ☁️ Cloud Deployment Challenges

Issues Encountered:

Missing runtime dependencies (e.g., joblib)

Accidental exposure of API keys

Differences between local and cloud environments

Resolutions:

Explicit dependency management via requirements.txt

Enforced .gitignore and environment-based secrets

Cloud-safe data paths and configurations

Outcome:
✔ Secure, reproducible, and stable cloud deployment.

---

## 🔐 Security & Privacy

All API keys removed from version control history

Secrets managed through environment variables

No personal or sensitive user data collected

Outcome:
✔ Production-safe by design.

---

## 🧠 Engineering Decisions & Trade-offs

API failures:
- Handled through status validation, defensive parsing, and fault-tolerant logic.

Model stability:
- Ensured via locked feature schemas using feature_names_in_.

Deployment debugging:
- Resolved by aligning local and cloud environments and refining dependencies.

Production readiness:
- Achieved through schema validation, secure secrets, and reproducible pipelines.

Next improvements:
- Data expansion over time, automated retraining, API caching, and alerting systems.

---

## 🔮 Future Enhancements

Real-time AQI ingestion and monitoring

Automated model retraining pipeline

Health advisory alerts for high-risk conditions

Policy-oriented dashboards for urban planners

---

## 🛠 Technology Stack

Python, Pandas, NumPy

Scikit-learn (Machine Learning)

Streamlit (Interactive Dashboard)

PyDeck (Geospatial Visualization)

Git & GitHub

Cloud Deployment (Streamlit Cloud)

---

## 🏁 Final Note

Urban Health AI is not just a model or a dashboard.
It represents end-to-end ownership — from data ingestion and debugging to deployment and stakeholder-ready insights.

---

## 👤 Author
**MD ABDUL RAZAQ**  
Bachelor in Technology (Computer Science Engineering – Data Science)  
4th Year - 8th Semester
Noida International University
