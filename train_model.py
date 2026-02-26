import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib
from features import extract_features

# Load dataset
data = pd.read_csv("phishing.csv")  # change filename if needed

# Convert URLs to features
X = data["url"].apply(extract_features).tolist()
y = data["label"]   # 1=phishing, 0=safe

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

print("Accuracy:", model.score(X_test, y_test))

# Save model
joblib.dump(model, "phishing_model.pkl")
