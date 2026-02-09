💰 Loan Eligibility Prediction

A Python-powered machine learning application that predicts whether a loan will be approved based on applicant features using classification models and data analysis.

This project simulates a real-world credit scoring system by building predictive models and demonstrating end-to-end ML flow — from EDA to modeling to evaluation.

🔍 Project Overview

Loan eligibility prediction is crucial for financial institutions to evaluate credit risk effectively. This project uses historical loan application data to train a model that predicts whether a loan application should be approved (Eligible) or denied (Not Eligible) based on borrower characteristics.

It demonstrates essential machine learning techniques including data preprocessing, exploratory analysis, model training, and evaluation.

🚀 Key Features

✔ Data cleaning and preprocessing
✔ Exploratory data analysis (EDA)
✔ Feature engineering for meaningful insights
✔ Train and evaluate classification models
✔ Prediction for new loan applications

🛠️ Tech Stack
Component	Technology
Language	Python
Libraries	pandas, NumPy, scikit-learn, matplotlib, seaborn
ML Models	Logistic Regression, Random Forest, Decision Trees
Output	Confusion Matrix, Accuracy, Classification Report
Notebook	Jupyter Notebook
📁 Project Structure
loan_eligibility/
│
├── notebooks/
│   └── Loan_Eligibility_Prediction.ipynb   # EDA + model building notebook
│
├── models/
│   └── trained_model.pkl                   # Saved model file
│
├── requirements.txt                        # Dependency list
├── predict.py                              # Script to load model & predict
└── README.md

📊 How It Works

Load Dataset
Loan application records containing features such as credit history, income, marital status, loan amount, etc.

Data Cleaning & Preprocessing
Handling missing values, encoding categorical features, normalizing/standardizing where necessary.

Exploratory Data Analysis
Visualize feature distributions and correlations to understand patterns and influences.

Model Training
Train ML models using features and target label (Loan Status).

Model Evaluation
Evaluate performance using accuracy, precision, recall, F1-score, and confusion matrix.

Prediction Script
Use the trained model to make eligibility predictions on new input data.

📥 Installation & Setup
Step 1 — Clone the Repository
git clone https://github.com/Kushal-29/loan_eligibility.git
cd loan_eligibility

Step 2 — Create a Virtual Environment (recommended)
python -m venv venv
source venv/bin/activate      # macOS / Linux
venv\Scripts\activate         # Windows

Step 3 — Install Dependencies
pip install -r requirements.txt

🚀 How to Run
🔹 Run the Notebook

Open:

notebooks/Loan_Eligibility_Prediction.ipynb


Run all cells to see data processing, model training, evaluation, and results.

🔹 Predict Using Script

After training and saving the model, use:

python predict.py


Input required features for a new loan applicant and the model will output a prediction:

Prediction: Eligible
or
Prediction: Not Eligible

📊 Model Performance

The model evaluation metrics after training:

Metric	Score
Accuracy	~85%+
Precision	~82%+
Recall	~80%+
F1-Score	~81%+

These scores reflect effective predictive performance suitable for typical loan risk classification systems.
