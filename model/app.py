import streamlit as st
import pandas as pd
import joblib
import os

st.set_page_config(page_title="Stress Detection", layout="wide")

st.title("🧠 EEG / ECG Stress Detection Dashboard")

# ✅ Safe model loading (Works Local + Streamlit Cloud)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

main_model = joblib.load(os.path.join(BASE_DIR, "stress_model.pkl"))
eeg_model = joblib.load(os.path.join(BASE_DIR, "eeg_model.pkl"))

uploaded = st.file_uploader("Upload CSV or Excel", type=["csv","xlsx"])

if uploaded:

    if uploaded.name.endswith(".xlsx"):
        df = pd.read_excel(uploaded)
    else:
        df = pd.read_csv(uploaded)

    st.subheader("Dataset Preview")
    st.dataframe(df.head())

    # Convert numeric safely
    df_num = df.apply(pd.to_numeric, errors='coerce')
    df_num = df_num.dropna(axis=1, how='all')
    df_num = df_num.dropna()

    # Decide model automatically
    if df_num.shape[1] > 40:
        model = eeg_model
        st.success("EEG Model Selected")
    else:
        model = main_model
        st.success("EEG + ECG Model Selected")

    # Align features
    features = model.named_steps['scaler'].feature_names_in_
    aligned = pd.DataFrame()

    for col in features:
        if col in df_num.columns:
            aligned[col] = df_num[col]
        else:
            aligned[col] = 0

    aligned = aligned.fillna(0)

    # Predict
    pred = model.predict(aligned)

    df["Stress Prediction"] = pred
    df["Stress Prediction"] = df["Stress Prediction"].map(
        {0: "No Stress", 1: "Stress"}
    )

    st.subheader("Prediction Results")
    st.dataframe(df)

    st.download_button(
        "Download Results",
        df.to_csv(index=False),
        "results.csv"
    )

else:
    st.info("Upload EEG or ECG dataset to begin")
