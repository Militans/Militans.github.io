from tokenizers import Tokenizer
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
import numpy as np

from nltk_setup import stop_words
import nltk
import re
import pymorphy2 as p2
import os
from django.conf import settings

def remove_stopwords(text):
    words = nltk.word_tokenize(text)
    filtered_words = [word for word in words if word.lower() not in stop_words and word.isalnum()]
    return " ".join(filtered_words)

def remove_html(text):
    clean = re.compile('<.*?>|&.*?;')
    return re.sub(clean, '', text)

morph = p2.MorphAnalyzer()

def lemmatisation(text):
    words = text.split()
    return " ".join([morph.parse(word)[0].normal_form for word in words])

def preprocess_text(text):
    text = remove_stopwords(text)
    text = remove_html(text)
    text = lemmatisation(text)
    return text

def load_keras_model():
    model_path = os.path.join(settings.BASE_DIR, 'reviews', 'model', 'Fourth_model.h5')
    model = load_model(model_path)
    return model

def load_tokenizer():
    tokenizer_path = os.path.join(settings.BASE_DIR, 'reviews', 'model', 'tokenizer.json')
    tokenizer = Tokenizer.from_file(tokenizer_path)
    return tokenizer

# Глобальные переменные
model = load_keras_model()
tokenizer = load_tokenizer()

max_review_len = 350

def tokenize_text(text):
    sequences = [tokenizer.encode(t).ids for t in text]
    padded_sequences = pad_sequences(sequences, maxlen=max_review_len)
    return padded_sequences

# Функция для предсказания количества звезд
def predict_stars(preprocessed_text):
    tokenized_text = tokenize_text([preprocessed_text])
    predictions = model.predict(tokenized_text)
    reverse_mapping = {0: 1, 1: 2, 2: 3, 3: 4, 4: 7, 5: 8, 6: 9, 7: 10}
    predicted_indices = np.argmax(predictions, axis=1)
    predicted_stars = reverse_mapping[predicted_indices[0]]
    return predicted_stars
