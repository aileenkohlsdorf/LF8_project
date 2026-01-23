from pydantic import BaseModel
from datetime import date
from dataclasses import dataclass

@dataclass # like lombok
class Film(BaseModel):

    Film_ID: int
    Titel: str
    Erscheinungsjahr: date
    Genre: str
    Alterfreigabe: str