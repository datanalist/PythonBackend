import re
from pprint import pprint


def clean_text(text: str) -> str:
    """
    Очистить текст от лишних символов и слов
    Args:
        text(str): произвольный текст

    Returns:
        str: очищенный текст
    """
    if not isinstance(text, str):
        text = str(text)

    text = text.lower()
    text = text.strip('\r').strip('\t')
    text = text.replace("\n", " ")
    text = re.sub("-\s\r\n\|-\s\r\n|\r\n", '', str(text))

    text = re.sub("[0-9]|[-—.,:;_%©«»?*!@#№$^•·&()]|[+=]|[[]|[]]|[/]|", '', text)
    text = re.sub(r"\r\n\t|\n|\\s|\r\t|\\n", '', text)
    text = re.sub(r'[\xad]|[\s+]', ' ', text)
    text = re.sub(r'[\\<>{}/|]', '', text)
    text = re.sub('n', ' ', text)
    return " ".join(text.split())


if __name__ == "__main__":
    pprint(clean_text(
        "№№ $!@#$%^&*)_++==1234567890И было Слово И не было. А все та"
        "+ки?<>:?}|{|||"
    ))