# src/train_model.py

import os
import pickle
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, roc_auc_score
#from data_loader import load_data
#from preprocess import build_preprocessor
#from src.data_loader import load_data

from src.data_loader import load_data
from src.preprocess import build_preprocessor



BASE_DIR = os.path.dirname(os.path.dirname(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "models", "loan_model.pkl")
PREPROCESSOR_PATH = os.path.join(BASE_DIR, "models", "preprocessor.pkl")

def train():
    df = load_data()

    X = df.drop("Loan_Status", axis=1)
    y = df["Loan_Status"].map({"Y": 1, "N": 0})

    preprocessor = build_preprocessor()

    model = Pipeline(steps=[
        ("preprocess", preprocessor),
        ("classifier", LogisticRegression(max_iter=200))
    ])

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    print("Training model...")
    model.fit(X_train, y_train)

    preds = model.predict(X_test)
    roc = roc_auc_score(y_test, preds)

    print(f"Model Training Complete! ROC-AUC: {roc}")

    with open(MODEL_PATH, "wb") as f:
        pickle.dump(model, f)

    print(f"Model saved to {MODEL_PATH}")

if __name__ == "__main__":
    train()
