# src/predict.py

import pickle
import os
import pandas as pd
from src.data_loader import load_data


BASE_DIR = os.path.dirname(os.path.dirname(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "models", "loan_model.pkl")

def load_model():
    with open(MODEL_PATH, "rb") as f:
        return pickle.load(f)

def make_prediction(data):
    model = load_model()
    df = pd.DataFrame([data])
    prediction = model.predict(df)[0]
    return "Approved" if prediction == 1 else "Rejected"
