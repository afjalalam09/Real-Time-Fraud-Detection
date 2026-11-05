import streamlit as st
import pandas as pd
import joblib
import plotly.express as px

# Setup Page
st.set_page_config(page_title="FraudOps Dashboard", layout="wide")

# Load Model (Dummy logic for UI demonstration if data isn't loaded)
@st.cache_resource
def load_model():
    return joblib.load('model.pkl')

try:
    model = load_model()
    model_loaded = True
except:
    model_loaded = False

# Sidebar Navigation
st.sidebar.title("FraudOps Navigation")
page = st.sidebar.radio("Go to", ["Overview", "Transaction Explorer", "SHAP Explainer"])

if page == "Overview":
    st.title("Fraud Detection Overview")
    st.markdown("Real-time monitoring of financial transactions.")

    # Dummy KPIs for Dashboard layout
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Transactions", "590,000")
    col2.metric("Total Fraud Count", "20,663")
    col3.metric("Detection Rate", "98.5%")
    col4.metric("Avg Fraud Amount", "$145.50")

    st.info("Navigate to the Transaction Explorer to search specific IDs.")

elif page == "Transaction Explorer":
    st.title("Transaction Explorer")
    search_id = st.text_input("Enter Transaction ID to Search:")
    if search_id:
        st.success(f"Fetching details for Transaction {search_id}...")
        # Placeholder for transaction risk score
        st.metric("Live Risk Score", "85%", delta="Critical Risk", delta_color="inverse")

elif page == "SHAP Explainer":
    st.title("Explainable AI (SHAP)")
    st.write("Understand why the model flagged a transaction.")
    shap_id = st.text_input("Enter Transaction ID for AI Explanation:")
    if shap_id:
        st.warning(f"Generating SHAP Waterfall Plot for {shap_id}...")
        st.write("**Plain English Explanation:** The model flagged this transaction because the amount is significantly higher than the user's historical average and the device signature is unrecognized.")

st.sidebar.info("Built with Streamlit & LightGBM")
