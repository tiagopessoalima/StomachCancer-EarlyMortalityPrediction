# Predictive Factors for Early Mortality in Older Adults with Stomach Cancer

This repository contains the code and data for a **prospective study** focused on predicting early mortality in older adults with **stomach cancer**. By leveraging **baseline laboratory tests** and the **Comprehensive Geriatric Assessment (CGA)**, this project aims to improve risk stratification and assist in clinical decision-making using **machine learning models**.

## 📝 Project Overview

Older adults diagnosed with stomach cancer face unique challenges, including comorbidities and frailty, which can impact their treatment outcomes. This study explores the integration of **geriatric-specific assessments** with **laboratory biomarkers** to predict early mortality risk, helping oncologists provide personalized treatment plans.

### Key Objectives:
- Identify key **predictive factors** for early mortality in older adults with stomach cancer.
- Develop a **machine learning model** that combines clinical and geriatric data for enhanced risk stratification.
- Provide a tool to support **clinical decision-making** in oncology by incorporating these predictive factors.

## 🚀 Features

- **Data Collection**: Use of comprehensive geriatric assessments (CGA) and baseline laboratory tests.
- **Predictive Modeling**: Machine learning algorithms to identify high-risk patients.
- **Model Evaluation**: Performance evaluation using multiple metrics like accuracy, precision, recall, and AUC.

## 🔬 Methodology

1. **Data Source**: This study includes a cohort of older adults diagnosed with stomach cancer. Data includes:
   - Comprehensive Geriatric Assessment (CGA) measures.
   - Baseline laboratory results.
2. **Machine Learning**: 
   - Models used include Logistic Regression, Random Forest, Naive Bayes, Support Vector Machine, Multilayer Perceptron,Gradient Boosting and Decision Tree
   - Feature importance analysis to identify the most significant predictors.
3. **Outcome**: Prediction of early mortality, defined as death within 6 months after diagnosis.

## 📊 Model Performance

| Model            | Accuracy | Precision | Recall | AUC  |
|------------------|----------|-----------|--------|------|
| Logistic Regression | 77.90%      | 57.79%       | **74.29%**    | 0.8447 |
| Random Forest    | 78.41%      | 59.45%       | 72.86%    | 0.8178 |
| Naive Bayes          | 77.10%      | 57.83%       | 73.43%    | **0.8560** |
| Multilayer Perceptron          | 78.39%      | 58.61%       | 73.14%    | 0.8493 |
| Gradient Boosting          | **78.58%**      | **62.39%**       | 63.70%    | 0.8112 |
| Decision Tree          | 67.96%      | 44.41%       | 67.14%    | 0.6843 |
| Support Vector Machine          | 62.31%      | 39.04%       | 71.71%    | 0.7133 |

## ⚙️ Setup

To replicate the results or use the code, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/tiagopessoalima/StomachCancer-EarlyMortalityPrediction.git
   cd StomachCancer-EarlyMortalityPrediction
   ```

## 📚 Technologies

- **Python 3.8+**
- **Pandas & NumPy & Pandas** for data manipulation
- **Scikit-learn** for model training
- **Matplotlib & Seaborn** for data visualization
- **Jupyter Notebooks** for experiments and analysis

## 🔍 Try it out


<img src="qrCodeHuggingFace.png" alt="QR Code HuggingFace" width="500"/>

