# AI vs Human Text Detector

Detect whether a piece of text is AI-generated or human-written using a custom-trained machine learning model with TF-IDF features, SMOTE oversampling, and a confidence-tuned prediction threshold — all wrapped in an interactive Streamlit app.

---

## Features

- End-to-end ML pipeline (TF-IDF + numeric features + SMOTE + classifier)
- Threshold-based decision logic using `.predict_proba()` (default threshold: 0.6)
- Clean UI with animated progress bar and visual confidence indicators
- Detects GPT-like AI-generated content vs real human writing
- Flexible design – can be extended with other features or models

---

## Dataset

Source: [Kaggle - AI vs Human Text](https://www.kaggle.com/datasets/shanegerami/ai-vs-human-text/data)  
- Columns: `text`, `label` (`Generated` or `Human`)  
- Preprocessed to `0` = Human, `1` = AI

---

## How It Works

- **Text preprocessing:** `TfidfVectorizer(stop_words='english')`
- **Feature combination:** `ColumnTransformer` for text + numeric features (like text length)
- **Class imbalance handling:** `SMOTE` from `imblearn`
- **Classifier:** `RandomForestClassifier(class_weight='balanced')`
- **Thresholding:** `predict_proba()[1] >= 0.6` for AI class detection
- **Streamlit UI:** Animated progress bar + bubble + result label

---

## Installation

```bash
git clone https://github.com/saivijayragav/AI-Vs-Human-Text.git
cd AI-Vs-Human-Text
pip install -r requirements.txt
```
---
## Running the App
```bash
streamlit run deploy.py
```
Paste in any text (human or AI-generated) and click "Analyze" to visualize confidence.


