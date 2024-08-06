# zero_shot_classification.py
import pandas as pd
from transformers import pipeline

def zero_shot_classify(text, classifier, candidate_labels):
    result = classifier(text, candidate_labels)
    return result

def classify_feedback(filepath, candidate_labels):
    df = pd.read_csv(filepath)
    classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")
    df['CLASSIFICATION'] = df['TRANSLATED_COMMENTS'].apply(lambda x: zero_shot_classify(x, classifier, candidate_labels))
    return df

if __name__ == "__main__":
    filepath = '../data/sentiment_feedback.csv'
    candidate_labels = ["positive", "negative", "neutral"]
    df = classify_feedback(filepath, candidate_labels)
    df.to_csv('../data/classified_feedback.csv', index=False)
