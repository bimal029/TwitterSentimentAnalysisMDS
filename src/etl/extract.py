import pandas as pd

def extract_data():
    return pd.read_csv('data/training.1600000.processed.noemoticon.csv', encoding='latin1', header=None)
