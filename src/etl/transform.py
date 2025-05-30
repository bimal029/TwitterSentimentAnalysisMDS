import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords

def clean_text(text):
    stop_words = set(stopwords.words('english'))
    text = re.sub(r"http\S+", "", text)
    text = re.sub(r"@\w+", "", text)
    text = re.sub(r"[^a-zA-Z\s]", "", text).lower()
    words = text.split()
    return ' '.join([word for word in words if word not in stop_words])

def transform_data(df):
    df.columns = ['sentiment', 'id', 'date', 'query', 'user', 'text']
    df['clean_text'] = df['text'].apply(clean_text)
    return df[['sentiment', 'clean_text']]
