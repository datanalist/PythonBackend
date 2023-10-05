from pydantic import BaseModel

DEFAULT_TEXT = """Первый закон кибернетики№№ #$!@#$%^&*)_++==: невозможно создать вечный двигатель первого рода.
Второй закон кибернетики: количество информации в системе ограничено и не может превышать ее энтропию.
Третий закон кибернетики: информация должна быть структурирована для того, чтобы быть полезной.
Четвертый закон кибернетики: любая система 1234567890стремится к состоянию максимальной энтропии, если на нее не действуют внешние факторы.
Пятый закон кибернетики: система может быть описана с помощью математической модели, <>:?}|{|||\/если она является достаточно простой и линейной"""


class Person(BaseModel):
    """Contract for personal data"""
    user_id: str = "11220ASS"
    name: str = "Johny"
    last_name: str | None = "Silverhand"
    city: str = "Night-City"
    gender: str = "male"
    pet: str | None = "dog"
    age: int = "39"


class PersonDB(BaseModel):
    """Contract for user by his id"""
    user_id: str = "6513"
    name: str = "Winer"
    user_text: str | None = DEFAULT_TEXT
