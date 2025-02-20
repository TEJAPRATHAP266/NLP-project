# -*- coding: utf-8 -*-
"""sentiment_analyas.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/19SeAaPnZtix4G4CchwH0zqMTHpacBGFw
"""

import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
nltk.download('punkt_tab')
nltk.download('stopwords')
import re
import pandas as pd
import numpy as np
df = pd.read_csv('https://github.com/suhasmaddali/Twitter-Sentiment-Analysis/raw/refs/heads/main/train.csv')
df = df[['text','sentiment']]
def preprocess_text(text):
    if isinstance(text, float):
        return ""
    text = text.lower()  # Lowercase
    text = re.sub(r'http\S+|www.\S+', '', text)  # Remove URLs
    text = re.sub(r'[^a-zA-Z ]', '', text)  # Remove special characters & numbers
    words = nltk.word_tokenize(text)  # Tokenization
    words = [word for word in words if word not in stopwords.words('english')]  # Remove stopwords
    return ' '.join(words)

tokens = []
for i in range(len(df)):
    tokens.append(preprocess_text(df['text'][i]))

tokens

from gensim.models import Word2Vec
sentences = [word_tokenize(i) for i in tokens]
model = Word2Vec(tokens,vector_size=300,window=10,min_count=2,workers=4,sg=0)

sentences

model.wv.vectors

