from pydantic import BaseModel
from dataclasses import dataclass

@dataclass # like lombok
class Mitarbeiter(BaseModel):

    __Mitarbeiter_ID__: int
    __Vorname__: str
    __Nachname__: str