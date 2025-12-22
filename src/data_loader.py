# src/data_loader.py

import os
import pandas as pd

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DATA_PATH = os.path.join(BASE_DIR, "data", "loan.csv")

def load_data():
    if not os.path.exists(DATA_PATH):
        raise FileNotFoundError("Dataset file loan.csv not found in /data/")
    return pd.read_csv(DATA_PATH)
