# AI-Generated Text Detection  

## Overview  
This project focuses on detecting AI-generated text from human-written content using machine learning techniques. The model is implemented in a **Jupyter Notebook (.ipynb)**, leveraging **Natural Language Processing (NLP)** and classification algorithms to distinguish between AI and human-generated text.  

## Problem Statement  
AI-generated text has become increasingly difficult to differentiate from human-written content, raising concerns about misinformation and authenticity. The goal of this project is to develop a **machine learning model** that accurately classifies text as AI-generated or human-written, ensuring transparency in digital communication.  

## Approach  
1. **Dataset**: Uses a labeled dataset (`AI_Human.csv`) containing AI-generated and human-written text samples.  
2. **Preprocessing**: Applies tokenization and **TF-IDF vectorization** for feature extraction.  
3. **Model Selection**: Employs a **Random Forest Classifier** with **SMOTE oversampling** to address class imbalance.  
4. **Evaluation**: Assesses model performance using **precision, recall, F1-score, and ROC-AUC metrics**.  
5. **Visualization**: Generates a **confusion matrix** and **ROC curve** to evaluate classification results.  

## Results  
- **Accuracy**: 96% on both training and testing datasets.  
- **Balanced precision-recall scores** ensuring reliable classification.  
- **Strong ROC curve performance**, demonstrating effective differentiation between AI and human-written text.  

## Installation & Usage  
### Prerequisites  
- Python 3.12+
- Jupyter Notebook  
- Required libraries: pandas, scikit-learn, imbalanced-learn, matplotlib, joblib  

### Running the Notebook  
1. Clone the repository  
   ```bash
   git clone "https://github.com/saivijayragav/AI-Vs-Human-Text.git"
   ```
2. Navigate to the directory  
   ```bash
   cd /path/to/notebook
   ```
3. Install dependencies  
   ```bash
   pip install -r requirements.txt
   ```
4. Launch Jupyter Notebook  
   ```bash
   jupyter notebook
   ```
5. Open and run `modeltraining.ipynb` to execute the model and view results.  

## Future Enhancements  
- Improving classification accuracy using **deep learning architectures**.  
- Fine-tuning model thresholds for better detection.  
- Expanding the dataset to include more complex AI-generated text patterns.  

## References  
- Research papers on **AI-generated text detection**  
- Documentation on **TF-IDF vectorization, Random Forest, and SMOTE**  
- Libraries used in implementation  
