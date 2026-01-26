from pydantic import BaseModel

from dataclasses import dataclass

@dataclass # like lombok
class Film(BaseModel):

    Film_ID: int
    Titel: str
    Erscheinungsjahr: int
    Genre: str
    Altersfreigabe: str