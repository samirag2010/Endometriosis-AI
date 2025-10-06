import streamlit as st
from PIL import Image
import numpy as np

# Stub predictor for demo purposes
def predict_endometriosis(image_array):
    avg_pixel = np.mean(image_array)
    if avg_pixel < 100:
        return "Possible Endometriosis", 0.85
    else:
        return "Unlikely Endometriosis", 0.70

# Streamlit UI
st.set_page_config(page_title="AI for Endometriosis", layout="centered")

st.title("🩺 AI-Assisted Endometriosis Screening (Demo)")
st.write("""
This is a **demo application** simulating an AI tool for endometriosis detection.  
Upload a pelvic ultrasound or MRI image to test the classifier.  

⚠️ **Disclaimer**: This demo is for educational purposes only and not intended for medical use.
""")

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("L")  # Convert to grayscale
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Resize to fixed size
    img_resized = image.resize((128, 128))
    img_array = np.array(img_resized)

    # Run "AI" prediction (stub)
    prediction, confidence = predict_endometriosis(img_array)

    st.subheader("Prediction Results")
    st.write(f"**Prediction:** {prediction}")
    st.write(f"**Confidence:** {confidence*100:.2f}%")
