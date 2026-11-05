# Real-Time Fraud Detection System & Dashboard

## Project Overview
This is an advanced Machine Learning pipeline and interactive dashboard designed to detect fraudulent credit card transactions in real-time. The project tackles severe class imbalance (3.5% fraud rate) and provides Explainable AI (SHAP) for transparent decision-making.

## Tech Stack
- **Modeling:** LightGBM, XGBoost, Isolation Forest
- **Data Processing:** Pandas, Scikit-Learn, SMOTE (imbalanced-learn)
- **Explainable AI:** SHAP
- **Dashboard:** Streamlit, Plotly

## How to Run the Dashboard
1. Ensure all dependencies from `requirements.txt` are installed.
2. Open terminal/command prompt in the project folder.
3. Run the following command:
   `streamlit run dashboard/app.py`
4. The live dashboard will open automatically in your default web browser.
