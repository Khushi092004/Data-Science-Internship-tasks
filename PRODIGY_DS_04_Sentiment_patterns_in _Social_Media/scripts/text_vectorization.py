import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer

# Load cleaned data
df = pd.read_csv('../data/cleaned_twitter_data.csv')

# Initialize CountVectorizer
vectorizer = CountVectorizer(max_features=1000, stop_words='english')
X = vectorizer.fit_transform(df['cleaned_text']).toarray()

# Save vectorized features for model training
import numpy as np
np.save('../data/vectorized_features.npy', X)
