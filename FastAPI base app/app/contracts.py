from pydantic import BaseModel


class Person(BaseModel):
    """Contract for personal data"""
    user_id: str = "11220ASS"
    name: str = "Johny"
    last_name: str | None = "Silverhand"
    city: str = "Night-City"
    gender: str = "male"
    pet: str | None = "dog"
    age: int = "39"