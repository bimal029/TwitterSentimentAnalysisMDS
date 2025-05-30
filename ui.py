import streamlit as st
import pandas as pd
from pymongo import MongoClient

st.title("Sentiment140 Tweet Sentiment Dashboard")
client = MongoClient("mongodb://localhost:27017/")
collection = client['sentiment140']['tweets']
data = list(collection.find())
df = pd.DataFrame(data)
st.write(df.head())
