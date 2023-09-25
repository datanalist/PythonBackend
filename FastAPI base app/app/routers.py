from fastapi import APIRouter
from app import contracts
from starlette.responses import FileResponse
import datetime
router = APIRouter()


@router.get("/")
def read_root():  # noqa: D103
    """Ordinary function. Print Hello World!"""
    return "Hello World!"


@router.get("/items/{item_id}")
async def read_item(item_id: int) -> dict:
    """
    Async function. Return item id

    Args:
        item_id (int): id of item

    Returns:
        dict(item_id=item_id)"""
    return {"item_id": item_id}


@router.get("/users/")
async def read_user(user_id: str, q: str | None = None) -> dict:
    """
    Async function. Return information about user

    Args:
        user_id (str): id for user
        q (str): some description

    Returns:
        dict(item_id=user_id, q=q) | dict(item_id=user_id)
    """
    if q:
        return {"item_id": user_id, "q": q}
    return {"item_id": user_id}


@router.get("/info/{get_info}")
async def read_info(get_info: str | None = None) -> object | str:
    """
    Print some information for user

    Args:
        get_info (str|None): get certain information, use this options ["history", "about", "contacts"]

    Returns:
        list|dict|tuple
    """
    try:
        if get_info not in ["history", "about", "contacts"] or get_info is None:
            raise Exception
        if get_info == "history":
            return ["This page formed for pass the first home task of Python Backend!"]
        elif get_info == "about":
            return {"about": "You get this dictionary because you wanted it!"}
        else:
            return ("Name", "Mikhail"), ("Telegram", "@datanalist"), ("Email", "some@mail.ru")
    except Exception:
        return "No such function!"


@router.get("/picture/{type_of}")
async def get_animal_pict(type_of: str | None = None) -> FileResponse | str:
    """
    Paint picture of some animals: dolphin, cat, dog, student

    Args:
        type_of (str | None): Name of animal: list(dolphin, cat, dog, student)

    Returns:
        object (FileResponse)
    """
    global pets
    pets = dict(dolphin="../pictures/dolphin-coming-out-the-water.jpg",
                cat="../pictures/cat.jpg",
                dog="../pictures/pesel.jpg",
                student="../pictures/student.jpg")
    try:
        if type_of == "dolphin":
            return FileResponse(pets["dolphin"])
        elif type_of == "cat":
            return FileResponse(pets["cat"])
        elif type_of == "dog":
            return FileResponse(pets["dog"])
        elif type_of == "student":
            return FileResponse(pets["student"])
        else:
            raise Exception
    except Exception:
        return "No such pictures!"


@router.get("/users/{user_id}/items/{item_id}")
async def read_user_item(
        user_id: int,
        item_id: str,
        q: str | None = None,
        short: bool = False) -> dict:
    """
    Update item by id

    Args:
        user_id (int): id of user
        item_id (str): id of item
        q (str | None): some description
        short (bool): marker

    Returns:
        dict: updated item for user
    """
    item: dict[str, str | int] = dict(item_id=item_id, owner_id=user_id)
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item


@router.post("/items/")
async def create_item(item: contracts.Item) -> dict:
    """
    Create some custom item

    Args:
        item (contracts.Item): some item

    Returns:
        dict: updated item
    """
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict

@router.post("/person/")
async def create_person(data: contracts.Person) -> dict:
    """
    Input personal data about person

    Args:
        user_id (str): id fo user
        name (str): user's name
        last_name (str): user's lastname
        city (str): user's hometown
        gender (str): male/female
        pet (str | None): person's pet
        age (int): age
    Returns:
        dict: fields of personal data
    """
    data_dict = data.dict()
    assert data_dict.gender in ["male", "female"]
    data_dict.gender = map(lambda x: 1 if x == "male" else 0, data_dict.gender)
    if data_dict.age:
        birth_year = datetime.date.today().year - data_dict.age
        data_dict.update({"birth_year": birth_year})
    if data_dict.pet in pets.keys():
        data_dict.update({"pet's photo": f"http://127.0.0.1:8000/picture/{pets[data_dict.pet]}"})
    return data_dict