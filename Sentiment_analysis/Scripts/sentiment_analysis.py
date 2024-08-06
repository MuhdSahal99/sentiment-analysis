# sentiment_analysis.py
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def sentiment_analysis(text, analyzer):
    sentiment = analyzer.polarity_scores(text)
    return sentiment

def analyze_sentiments(filepath):
    df = pd.read_csv(filepath)
    analyzer = SentimentIntensityAnalyzer()
    df['SENTIMENT'] = df['TRANSLATED_COMMENTS'].apply(lambda x: sentiment_analysis(x, analyzer))
    return df

if __name__ == "__main__":
    filepath = '../data/translated_feedback.csv'
    df = analyze_sentiments(filepath)
    df.to_csv('../data/sentiment_feedback.csv', index=False)
