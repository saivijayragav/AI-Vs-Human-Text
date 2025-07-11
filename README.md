# 🤖 vs 👤 AI Text Detector

> **Detect AI-generated content with confidence** — A sophisticated machine learning solution that distinguishes between artificial and human-written text using advanced TF-IDF features, SMOTE oversampling, and intelligent threshold tuning.

---

## ✨ **Key Highlights**

🔬 **Advanced ML Pipeline** — Complete end-to-end solution combining TF-IDF vectorization, numeric feature engineering, and SMOTE class balancing

🎯 **Smart Confidence Scoring** — Threshold-based predictions using `.predict_proba()` with optimized 0.7 detection threshold for enhanced precision

🎨 **Beautiful Interactive UI** — Streamlit-powered interface featuring animated progress bars and visual confidence indicators

🚀 **Production Ready** — Optimized for detecting GPT-style AI content with flexible architecture for easy extension

---

## 🎯 **Core Features**

| Feature | Description |
|---------|-------------|
| **Intelligent Detection** | Identifies AI-generated text vs authentic human writing |
| **Real-time Analysis** | Instant feedback with animated confidence visualization |
| **Balanced Training** | SMOTE oversampling ensures robust performance across classes |
| **Extensible Design** | Modular architecture supports additional features and models |

---

## 🏆 **Performance Metrics**

Our model demonstrates exceptional performance with rigorous evaluation:

### **Accuracy Scores**
- **Overall Accuracy:** 96% (both training and testing datasets)
- **Precision:** 96% (high reliability in positive predictions)
- **Recall:** 98% (Human class) | 93% (AI class)
- **F1-Score:** 95% (excellent balance between precision and recall)

### **Model Validation**
- **ROC-AUC:** High discrimination capability with curve close to ideal top-left corner
- **Confusion Matrix:** Balanced performance across both classes
- **Cross-validation:** Consistent results across different data splits

### **Key Achievements**
✅ **Balanced Performance** — Equal accuracy on both training and testing sets (no overfitting)  
✅ **High Precision** — Minimizes false positives for reliable detection  
✅ **Strong Recall** — Excellent detection rate for both human and AI content  
✅ **Robust Generalization** — Performs well on unseen real-world examples

---

## 📊 **Dataset Information**

**Source:** [Kaggle - AI vs Human Text Dataset](https://www.kaggle.com/datasets/shanegerami/ai-vs-human-text/data) by Shane Gerami

- **Structure:** `text` content paired with `label` classification
- **Labels:** `Generated` (AI) | `Human` (authentic)
- **Preprocessing:** Binary encoding → `0` = Human, `1` = AI-generated
- **Challenge:** Imbalanced dataset with more AI samples than human ones, requiring SMOTE balancing

---

## ⚙️ **Technical Architecture**

```
📝 Raw Text Input
    ↓
🔧 TfidfVectorizer (stop_words='english')
    ↓
🔢 Feature Engineering (text length, complexity metrics)
    ↓
⚖️ SMOTE Oversampling (class balance optimization)
    ↓
🌲 RandomForestClassifier (class_weight='balanced')
    ↓
🎯 Confidence Thresholding (≥0.7 for AI detection)
    ↓
📊 Streamlit Visualization
```

### **Core Components**
- **Text Processing:** Advanced TF-IDF vectorization with English stop-word filtering
- **Feature Fusion:** ColumnTransformer combining textual and numeric features
- **Class Balancing:** SMOTE algorithm for handling imbalanced datasets
- **Classification:** Ensemble RandomForest with balanced class weighting
- **Decision Logic:** Probabilistic thresholding (≥0.7) for optimal precision-recall balance

---

## 🚀 **Live Demo**

**🌐 Try it now:** [AI vs Human Text Detection App](https://ai-vs-human-text-detection.streamlit.app/)

Experience the model in action with our interactive Streamlit deployment featuring:
- Real-time text analysis with instant results
- Confidence scoring and visual feedback
- User-friendly interface with animated progress indicators
- Deployed on Streamlit Cloud for seamless accessibility

---

## 🚀 **Quick Start**

### **Installation**
```bash
# Clone the repository
git clone https://github.com/saivijayragav/AI-Vs-Human-Text.git

# Navigate to project directory
cd AI-Vs-Human-Text

# Install dependencies
pip install -r requirements.txt
```

### **Launch Application**
```bash
streamlit run deploy.py
```

### **Usage**
1. 📋 **Paste your text** into the input field
2. 🔍 **Click "Analyze"** to start detection
3. 📈 **View results** with confidence visualization and animated feedback

---

## 💡 **Use Cases**

- **Content Verification** — Validate authenticity of articles, essays, and reports
- **Academic Integrity** — Detect AI-assisted writing in educational submissions  
- **Publishing Quality Control** — Ensure original human-authored content
- **Research Applications** — Analyze text generation patterns and AI detection methods

---

## 🔮 **Future Enhancements**

- 🧠 **Deep Learning Models** — Integration with transformer-based architectures
- 📱 **API Endpoint** — REST API for programmatic access
- 🌐 **Multi-language Support** — Detection across different languages
- 📊 **Advanced Analytics** — Detailed reporting and batch processing capabilities

---

## 📚 **References & Research**

This project builds upon extensive research in AI text detection:

1. **[Testing of detection tools for AI-generated text](https://example.com)** — Comprehensive study evaluating various AI text detection methods in academic settings

2. **[Detecting AI Generated Text Based on NLP and Machine Learning Approaches](https://example.com)** — Exploration of different machine learning techniques for AI text classification

3. **[Google SynthID: AI-generated content detection tool](https://example.com)** — Google's innovative approach to watermarking AI-generated content

4. **[Copyleaks AI and Plagiarism Detection](https://example.com)** — Real-time AI detection tools integrated into collaborative platforms

---

**GitHub Repository:** [AI-Vs-Human-Text](https://github.com/saivijayragav/AI-Vs-Human-Text)

---

## 🤝 **Contributing**

We welcome contributions! Please feel free to submit pull requests, report issues, or suggest new features.

---

## 📄 **License**

This project is open source and available under the [MIT License](LICENSE).

---

<div align="center">
  <strong>🌟 Star this repo if you find it useful! 🌟</strong>
</div>
