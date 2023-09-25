from pydantic import BaseModel


class Item(BaseModel):
    """Contract for item."""

    items: str
    description: str | None = None
    price: float
    tax: float | None = None


class Person(BaseModel):
    """Contract for personal data"""
    user_id: str = "13158asd"
    name: str = "Tony"
    last_name: str | None = "Stark"
    city: str = "Malibu"
    gender: str = "male"
    pet: str | None = cat
    age: int = 51