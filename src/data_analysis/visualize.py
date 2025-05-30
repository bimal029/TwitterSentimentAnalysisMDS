import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def plot_sentiment_distribution(csv_path):
    df = pd.read_csv(csv_path)
    sns.countplot(x='sentiment', data=df)
    plt.title('Sentiment Distribution')
    plt.show()
