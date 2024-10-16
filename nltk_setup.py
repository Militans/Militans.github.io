import nltk
from nltk.corpus import stopwords
import os

try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords')
try:
    nltk.data.find('corpora/words')
except LookupError:
    nltk.download('punkt')
if not os.path.exists(nltk.data.find('corpora/stopwords')):
    nltk.download('stopwords')
if not os.path.exists(nltk.data.find('tokenizers/punkt')):
    nltk.download('punkt')
# Инициализация переменных
stop_words = set(stopwords.words('english'))
