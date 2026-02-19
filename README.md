# Loan Eligibility Prediction using Machine Learning

A machine learning project that predicts whether a loan application will be approved based on applicant details.  
This project demonstrates an end-to-end ML workflow used in real-world financial decision systems.

---

## Project Overview

Loan approval is a critical process for financial institutions to manage credit risk.  
This project uses historical loan application data to train classification models that predict whether an applicant is **Eligible** or **Not Eligible** for a loan.
 
The focus is on:
- Data preprocessing
- Exploratory Data Analysis (EDA)
- Feature engineering
- Model training and evaluation

--- 

## Problem Statement 

Manual loan approval processes are time-consuming and prone to bias.  
An automated ML-based system can help institutions:
- Reduce risk 
- Improve decision accuracy
- Speed up approval workflows 

This project simulates such a system using supervised learning techniques.

---

## Key Features

- Data cleaning and preprocessing
- Exploratory Data Analysis (EDA)
- Categorical feature encoding
- Training multiple classification models
- Performance evaluation using standard metrics
- Prediction for new loan applications

---

## Tech Stack

**Language**
- Python

**Libraries**
- pandas
- NumPy
- scikit-learn
- matplotlib
- seaborn

**ML Models**
- Logistic Regression
- Decision Tree
- Random Forest

---
loan_eligibility/
│
├── notebooks/
│ └── Loan_Eligibility_Prediction.ipynb # EDA and model training
│
├── models/
│ └── trained_model.pkl # Saved trained model
│
├── predict.py # Script to load model and predict
├── requirements.txt # Project dependencies
└── README.md

---

## Workflow

1. Load loan application dataset
2. Handle missing values
3. Encode categorical variables
4. Perform exploratory data analysis
5. Train classification models
6. Evaluate model performance
7. Save the best performing model
8. Predict loan eligibility for new inputs

---

## Model Evaluation

Models are evaluated using:

- Accuracy
- Precision
- Recall
- F1-Score
- Confusion Matrix

**Best model achieved accuracy of ~85%+**, showing reliable prediction capability for loan approval decisions.

---

## How to Run the Project

### 1. Clone the Repository
```bash
git clone https://github.com/Kushal-29/loan_eligibility.git
cd loan_eligibility

2. Create Virtual Environment (Recommended)
python -m venv venv
source venv/bin/activate    # Linux / Mac
venv\Scripts\activate       # Windows

3. Install Dependencies
pip install -r requirements.txt

4. Run the Notebook

Open and run:

notebooks/Loan_Eligibility_Prediction.ipynb

5. Make Predictions
python predict.py
## Project Structure

