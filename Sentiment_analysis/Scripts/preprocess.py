# preprocess.py
import pandas as pd
import re

def clean_text(text):
    if not isinstance(text, str):
        return ""
    # Remove numbers
    text = re.sub(r'\d+', '', text)
    # Remove punctuation and other symbols
    text = re.sub(r'[^\w\s]', '', text)
    # Remove Arabic diacritics
    arabic_diacritics = re.compile("""
                               ّ    | # Tashdid
                               َ    | # Fatha
                               ً    | # Tanwin Fath
                               ُ    | # Damma
                               ٌ    | # Tanwin Damm
                               ِ    | # Kasra
                               ٍ    | # Tanwin Kasr
                               ْ    | # Sukun
                               ـ     # Tatwil/Kashida
                           """, re.VERBOSE) 
    text = re.sub(arabic_diacritics, '', text)
    return text

def preprocess_data(filepath):
    df = pd.read_excel(filepath, engine='openpyxl')
    df['OTHER_COMMENTS'] = df['OTHER_COMMENTS'].apply(clean_text)
    df = df[df['OTHER_COMMENTS'].str.strip() != ""]
    return df

if __name__ == "__main__":
    filepath = 'data/Patient_feedback.xlsx'
    df = preprocess_data(filepath)
    df.to_csv('../data/cleaned_feedback.csv', index=False)
