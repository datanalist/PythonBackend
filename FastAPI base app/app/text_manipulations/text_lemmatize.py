def text_lemmatize(text):
    """
    Лемматизация текста
        [0] если зашел тип не `str` делаем его `str`
        [1] токенизация предложения через razdel
        [2] проверка есть ли в начале слова '-'
        [3] проверка токена с одного символа
        [4] проверка есть ли данное слово в кэше
        [5] лемматизация слова
        [6] проверка на стоп-слова
    Args:
        text: очищенный текст

    Returns:
        list(str): лемматизированные слова текста пользователя
    """
    '''
    

    на выходе лист лемматизированых токенов
    '''

    # [0]
    if not isinstance(text, str):
        text = str(text)

    # [1]
    tokens = list(tokenize(text))
    words = [_.text for _ in tokens]

    words_lem = []
    for w in words:
        if w[0] == '-':  # [2]
            w = w[1:]
        if len(w) > 1:  # [3]
            if w in cache:  # [4]
                words_lem.append(cache[w])
            else:  # [5]
                temp_cach = cache[w] = morph.parse(w)[0].normal_form
                words_lem.append(temp_cach)

    words_lem_without_stopwords = [i for i in words_lem if not i in stopword_ru]  # [6]

    return words_lem_without_stopwords