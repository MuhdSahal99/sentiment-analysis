# pipeline.py
import preprocess
import translate
import sentiment_analysis
import zero_shot_classification

def run_pipeline():
    # Preprocess the data
    preprocess_filepath = '../data/Patient_feedback.xlsx'
    preprocess_df = preprocess.preprocess_data(preprocess_filepath)
    preprocess_df.to_csv('../data/cleaned_feedback.csv', index=False)

    # Translate the data
    translate_filepath = '../data/cleaned_feedback.csv'
    translate_df = translate.translate_data(translate_filepath)
    translate_df.to_csv('../data/translated_feedback.csv', index=False)

    # Perform sentiment analysis
    sentiment_filepath = '../data/translated_feedback.csv'
    sentiment_df = sentiment_analysis.analyze_sentiments(sentiment_filepath)
    sentiment_df.to_csv('../data/sentiment_feedback.csv', index=False)

    # Perform zero-shot classification
    classify_filepath = '../data/sentiment_feedback.csv'
    candidate_labels = ["positive", "negative", "neutral"]
    classify_df = zero_shot_classification.classify_feedback(classify_filepath, candidate_labels)
    classify_df.to_csv('../data/classified_feedback.csv', index=False)

if __name__ == "__main__":
    run_pipeline()
