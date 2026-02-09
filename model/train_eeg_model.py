import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
import joblib
import os

# Load EEG data
eeg = pd.read_excel(
    r"../data/EEG (EO, AC1, AC2).xlsx",
    sheet_name="Normalize"
)

# Convert to numeric
eeg = eeg.apply(pd.to_numeric, errors='coerce')

# Drop empty columns & rows
eeg = eeg.dropna(axis=1, how='all')
eeg = eeg.dropna()

print("Shape after cleaning:", eeg.shape)

# Create labels
split = len(eeg)//2
labels = [0]*split + [1]*(len(eeg)-split)
eeg["stress"] = labels

# Split data
X = eeg.drop("stress", axis=1)
y = eeg["stress"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Pipeline
pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('model', RandomForestClassifier())
])

pipeline.fit(X_train, y_train)

# ===== SAVE IN model FOLDER =====
save_path = r"../model/stress_model.pkl"
joblib.dump(pipeline, save_path)

print("✅ EEG model trained & saved at:", os.path.abspath(save_path))
