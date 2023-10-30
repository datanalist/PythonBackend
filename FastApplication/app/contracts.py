from pydantic import BaseModel
import datetime

class Product(BaseModel):
    """Data about products for a shop"""
    id: str = "qwerty12345"
    name: str = "Bread"
    producer: str = "BredBread&Co"
    date: datetime.strptime = datetime.strptime("01.01.2023", "%d.%m.%y")