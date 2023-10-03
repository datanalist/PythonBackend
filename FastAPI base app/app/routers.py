from fastapi import APIRouter
from app import contracts
from starlette.responses import FileResponse
import datetime
from text_manipulations import get_stopwords, clean_text, text_lemmatize

router = APIRouter()


@router.get("/")
def read_root():  # noqa: D103
    """Ordinary function. Print Hello World!"""
    return "This is the start page! You can go to /clean_text/ or to /text_lemmatize/"


@router.get("/clean_text/{person}/{text}")
async def get_text(person: contracts.PersonDB, text: str | None = None) -> str:
    """
    Async function. Return user's text without stopwords and service symbols
    Args:
        text (str): user's text

    Returns:
        str: text without topwords and service symbols
    """
    person_db = person.dict()
    get_stopwords()
    person_db.update({"users_clean_text": clean_text(text)})
    return person_db


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


@router.post("/person/")
async def create_person(person: contracts.Person) -> dict:
    """
    Input personal data about person

    Args:
        data:
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
    person_dict = person.dict()

    assert person.gender in ["male", "female"]
    person_dict["gender"] = 1 if person.gender  == "male" else 0
    if person.age:
        birth_year = datetime.date.today().year - person.age
        person_dict.update({"birth_year": birth_year})
    if person.pet in pets.keys():
        person_dict.update({"pet's photo": f"http://127.0.0.1:8000/picture/{person.pet}"})
    return person_dict