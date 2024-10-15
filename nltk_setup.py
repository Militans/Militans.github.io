import nltk
from nltk.corpus import stopwords
import os


if not os.path.exists(nltk.data.find('corpora/stopwords')):
    nltk.download('stopwords')
if not os.path.exists(nltk.data.find('tokenizers/punkt')):
    nltk.download('punkt')
# Инициализация переменных
stop_words = set(stopwords.words('english'))
