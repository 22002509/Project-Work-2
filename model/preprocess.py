import pandas as pd

# ==============================
# LOAD EEG (Normalized version)
# ==============================
eeg = pd.read_excel(
    "data/EEG (EO, AC1, AC2).xlsx",
    sheet_name="Normalize"
)

# ==============================
# LOAD ECG WITH LABELS
# ==============================
ecg_EO  = pd.read_excel("data/ECG (EO, AC1, AC2).xlsx", sheet_name="EO")
ecg_AC1 = pd.read_excel("data/ECG (EO, AC1, AC2).xlsx", sheet_name="AC1")
ecg_AC2 = pd.read_excel("data/ECG (EO, AC1, AC2).xlsx", sheet_name="AC2")

# Add stress labels
ecg_EO["stress"] = 0
ecg_AC1["stress"] = 1
ecg_AC2["stress"] = 1

# Combine ECG
ecg = pd.concat([ecg_EO, ecg_AC1, ecg_AC2], ignore_index=True)

# ==============================
# MERGE EEG + ECG
# ==============================

# Keep numeric only
eeg = eeg.select_dtypes(include=['float64','int64'])
ecg = ecg.select_dtypes(include=['float64','int64'])

# Match lengths (important!)
min_len = min(len(eeg), len(ecg))

eeg = eeg.iloc[:min_len]
ecg = ecg.iloc[:min_len]

# Combine features
data = pd.concat([eeg, ecg], axis=1)

# ==============================
# SAVE FINAL DATASET
# ==============================
data.to_csv("data/final_stress_data.csv", index=False)

print("✅ Preprocessing COMPLETE!")
