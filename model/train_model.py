import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score, classification_report
import joblib

# Load processed data
data = pd.read_csv("data/final_stress_data.csv")

# Split features & label
X = data.drop("stress", axis=1)
y = data["stress"]

# Train/Test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Model pipeline
pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('model', RandomForestClassifier(n_estimators=100))
])

# Train
pipeline.fit(X_train, y_train)

# Test
pred = pipeline.predict(X_test)

print("\nAccuracy:", accuracy_score(y_test, pred))
print("\nReport:\n", classification_report(y_test, pred))

# Save model
joblib.dump(pipeline, "model/stress_model.pkl")

print("\n✅ Model Saved!")
