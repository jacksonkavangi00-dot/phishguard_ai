import streamlit as st
import joblib
from features import extract_features

model = joblib.load("phishing_model.pkl")

st.title("🛡️ PhishGuard AI")
st.write("Enter a URL to check if it is phishing")

url = st.text_input("Enter URL:")

if st.button("Check URL"):
    features = extract_features(url)
    prediction = model.predict([features])[0]
    prob = model.predict_proba([features])[0][1] * 100
    
    if prediction == 1:
        st.error(f"⚠️ PHISHING DETECTED! Risk: {prob:.2f}%")
    else:
        st.success(f"✅ SAFE WEBSITE. Risk: {prob:.2f}%")
