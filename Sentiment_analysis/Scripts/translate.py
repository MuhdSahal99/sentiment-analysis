# translate.py
import pandas as pd
from googletrans import Translator

def translate_text(text, translator):
    try:
        translation = translator.translate(text, src='ar', dest='en')
        return translation.text
    except Exception as e:
        print(f"Error Translating text: {e}")
        return""
        

def translate_data(filepath):
    df = pd.read_csv(filepath)
    translator = Translator()
    df['TRANSLATED_COMMENTS'] = df['OTHER_COMMENTS'].apply(lambda x: translate_text(x, translator))
    return df

if __name__ == "__main__":
    filepath = '../data/cleaned_feedback.csv'
    df = translate_data(filepath)
    df.to_csv('../data/translated_feedback.csv', index=False)
