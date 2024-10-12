import pandas as pd
import re
from nltk.corpus import stopwords

def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)  # Remove punctuation
    text = re.sub(r'\d+', '', text)      # Remove numbers
    stop_words = set(stopwords.words('english'))
    text = ' '.join([word for word in text.split() if word not in stop_words])
    return text

# Load the dataset
df = pd.read_csv('../data/twitter_validation.csv')

# Clean the text data
df['cleaned_text'] = df['text '].apply(lambda x: clean_text(x))

# Save cleaned data to a new CSV file
df.to_csv('../data/cleaned_twitter_data.csv', index=False)
