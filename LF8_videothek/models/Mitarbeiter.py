from pydantic import BaseModel
from dataclasses import dataclass

@dataclass # like lombok
class Mitarbeiter(BaseModel):

    Mitarbeiter_ID: int
    Vorname: str
    Nachname: str