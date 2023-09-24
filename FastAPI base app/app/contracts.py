from pydantic import BaseModel


class Item(BaseModel):
    """Contract for item."""

    items: str
    description: str | None = None
    price: float
    tax: float | None = None
