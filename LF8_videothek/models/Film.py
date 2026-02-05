from pydantic import BaseModel

from dataclasses import dataclass

@dataclass # like lombok
class Film(BaseModel):

    __Film_ID__: int
    __Titel__: str
    __Erscheinungsjahr__: int
    __Genre__: str
    __Altersfreigabe__: str