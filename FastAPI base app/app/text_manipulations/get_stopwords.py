import nltk
from nltk.corpus import stopwords


def get_stopwords():
    """
    Загрузить стоп-слова из внешних источников
    Returns:
        list(str): список стоп-слов
    """
    nltk.download('stopwords')
    stopword_ru = stopwords.words('russian')
    with open('stopwords.txt') as f:
        additional_stopwords = [w.strip() for w in f.readlines() if w]
    stopword_ru += additional_stopwords
    return stopword_ru


if __name__ == "__main__":
    assert 776==len(get_stopwords())