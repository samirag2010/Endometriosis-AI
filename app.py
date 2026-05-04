import streamlit as st

# ------------------------------------------------------------
# Endometriosis AI Detection Assistant
# Educational NLP-style prototype for symptom-based analysis.
# This application does NOT diagnose medical conditions.
# ------------------------------------------------------------

st.set_page_config(
    page_title="Endometriosis AI Detection Assistant",
    page_icon="🩺",
    layout="centered"
)

st.title("Endometriosis AI Detection Assistant")
st.caption("Educational AI prototype for symptom-based awareness and early screening support.")

st.warning(
    "Medical Disclaimer: This tool does not provide a diagnosis. "
    "It is for educational purposes only and should not replace advice from a qualified healthcare professional."
)

st.header("Describe Your Symptoms")

symptom_text = st.text_area(
    "Enter symptoms or health notes:",
    placeholder="Example: Severe pelvic pain, painful periods, fatigue, irregular cycles, pain during intercourse...",
    height=160
)

# Symptom keywords commonly discussed in endometriosis awareness contexts.
# This is a rule-based educational prototype, not a trained clinical model.
symptom_keywords = {
    "pelvic pain": 3,
    "painful periods": 3,
    "cramps": 2,
    "heavy bleeding": 2,
    "fatigue": 2,
    "irregular periods": 2,
    "pain during intercourse": 3,
    "painful sex": 3,
    "bloating": 1,
    "lower back pain": 1,
    "nausea": 1,
    "infertility": 3,
    "painful bowel movements": 2,
    "painful urination": 2
}

def analyze_symptoms(text):
    """
    Analyze symptom text using a simple keyword-based scoring method.

    Returns:
        matched_symptoms: list of symptom keywords found
        score: total weighted score
        confidence: simulated confidence percentage
        risk_level: educational risk category
    """
    text = text.lower()
    matched_symptoms = []

    score = 0
    for keyword, weight in symptom_keywords.items():
        if keyword in text:
            matched_symptoms.append(keyword)
            score += weight

    confidence = min(95, 35 + score * 7)

    if score >= 8:
        risk_level = "Higher symptom pattern match"
    elif score >= 4:
        risk_level = "Moderate symptom pattern match"
    elif score > 0:
        risk_level = "Low symptom pattern match"
    else:
        risk_level = "No clear symptom pattern detected"

    return matched_symptoms, score, confidence, risk_level

if st.button("Analyze Symptoms"):
    if not symptom_text.strip():
        st.error("Please enter symptom information before analyzing.")
    else:
        matched_symptoms, score, confidence, risk_level = analyze_symptoms(symptom_text)

        st.header("Analysis Results")
        st.metric("Confidence Score", f"{confidence}%")
        st.subheader(risk_level)

        if matched_symptoms:
            st.write("**Symptoms detected in your description:**")
            for symptom in matched_symptoms:
                st.write(f"- {symptom}")
        else:
            st.write("No major symptom keywords were detected in the current input.")

        st.write("**Explanation:**")
        st.write(
            "The assistant reviewed the symptom description and looked for patterns commonly associated "
            "with endometriosis awareness, such as pelvic pain, painful periods, fatigue, heavy bleeding, "
            "and pain-related symptoms."
        )

        st.info(
            "Recommendation: If these symptoms are frequent, severe, or affecting daily life, consider "
            "speaking with a gynecologist or qualified healthcare provider."
        )

st.divider()

st.header("Future Expansion")
st.write(
    "Future versions of this project could expand into multimodal AI by combining text-based symptom "
    "analysis with medical imaging support, such as MRI or ultrasound review, using computer vision models."
)
