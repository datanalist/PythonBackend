import nltk
from nltk.corpus import stopwords
import urllib.request
import os


URL: str = "https://drive.google.com/uc?export=download&id=17wVn5YPpMjHToctGgff_KfSeWcIIlf7c"
STOP_FILE = './stopwords.txt'


def get_stopwords(stop_file:str = STOP_FILE) -> list:
    """
    Загрузить стоп-слова из внешних источников
    Returns:
        list(str): список стоп-слов
    """
    nltk.download('stopwords')
    stopword_ru = stopwords.words('russian')
    if not os.path.exists(stop_file):
        urllib.request.urlretrieve(URL, stop_file)
    with open(stop_file) as f:
        additional_stopwords = [w.strip() for w in f.readlines() if w]
    stopword_ru += additional_stopwords
    return stopword_ru


if __name__ == "__main__":
    from nltk.corpus import stopwords
    nltk.download('stopwords')
    stopword_ru = stopwords.words('russian')
    print(776 - len(stopword_ru))
# assert 776 == len(get_stopwords())