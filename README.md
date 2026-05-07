# 🧠 Endometriosis AI Detection Assistant

Healthcare-focused AI project exploring symptom analysis and explainable NLP-based decision support for endometriosis awareness.

Users enter symptom descriptions, and the system analyzes the input using Natural Language Processing (NLP) techniques to generate structured, explainable insights.  

## Disclaimer

⚠️ This tool is **not a diagnostic system**. It is designed for **educational and awareness purposes only** and encourages users to consult healthcare professionals.

---

## Why This Matters

Endometriosis affects millions of individuals worldwide and is often underdiagnosed due to delayed recognition of symptoms.

This project explores how AI-assisted symptom analysis and natural language processing could help improve awareness, early guidance, and healthcare accessibility.

---

## The Vision
Endometriosis is often underdiagnosed and can take years to identify.  

This project aims to:
- Help users better understand symptom patterns
- Provide structured, explainable AI insights
- Encourage earlier medical consultation
- Demonstrate responsible AI use in healthcare

---

## Project Goal

The goal of this project is to explore how AI systems can analyze symptom-related input and generate structured, explainable healthcare-oriented insights.

---

## The Architecture (The Brains 🧠)

The system follows a simple AI pipeline:

1. **User Input**
   - Text-based symptom descriptions → NLP Model
   - (Future) Medical Images → Computer Vision Model

2. **Preprocessing**
   - Text cleaning
   - Tokenization
   - Encoding into embeddings

3. **Model Layer**
   - Machine Learning / NLP model (TensorFlow / future transformer-based model)
   - Pattern recognition for symptom indicators

4. **Output Layer**
   - Confidence score
   - Explanation of findings
   - Recommendation for medical consultation

5. **Frontend**
   - Streamlit interface for interaction

---

## Technologies Used

- Python
- Streamlit
- TensorFlow (baseline model)
- Pandas / NumPy
- (Planned/Future) Hugging Face Transformers
- GitHub for version control

---

## Features

- Accepts natural language symptom input
- Generates structured, explainable output
- Displays confidence levels
- Provides medical guidance recommendations
- Simple and interactive UI using Streamlit

---

## Future Improvements

- Expanded symptom datasets
- Structured medical data integration
- Explainable AI enhancements
- Multi-language support
- Improved NLP pipelines
- Clinical collaboration research

---

## Privacy & Security

This project follows a **privacy-first design**:

- No permanent storage of user input
- Data processed in temporary session memory
- No personal health information retained
- Optional export features (future enhancement)
- Medical disclaimer included in outputs

---

## How to Run the Project

### 1. Clone the repository
```bash
git clone https://github.com/samirag2010/Endometriosis-AI.git
cd Endometriosis-AI
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the application
```bash
streamlit run app.py
```

---

## Example Output

### Input
![Input Screenshot](docs/demo.png)

### Results
![Results Screenshot](docs/demo2.png)

## Presentation

[View Project Presentation](presentation/Endometriosis-AI-Detection-Assistant%20(final).pdf)


