import streamlit as st
from transformers import pipeline
import requests
import json

# Load the misinformation detection model (replace with actual model)
classifier = pipeline("text-classification", model="your_misinformation_model")

# Function to detect misinformation
def detect_misinformation(text):
    result = classifier(text)
    return result[0]['label'], result[0]['score']

# Streamlit UI
st.title("Real-Time Misinformation Detection")

st.subheader("Enter Text for Fact-Checking")
user_input = st.text_area("Type or paste text to analyze:")

if st.button("Check for Misinformation"):
    if user_input:
        label, score = detect_misinformation(user_input)
        st.write(f"Prediction: {label} (Confidence: {score:.2f})")

        if label == "Misinformation":
            st.error("This might be misinformation. Please verify from trusted sources.")
        else:
            st.success("This information appears to be reliable.")
    else:
        st.warning("Please enter some text to analyze.")
