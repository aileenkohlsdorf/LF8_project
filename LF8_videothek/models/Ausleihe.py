from typing import Union

from pydantic import BaseModel
from datetime import date
from dataclasses import dataclass

@dataclass # like lombok
class Ausleihe(BaseModel):

    Ausleihe_ID: int
    Ausleihdatum: date
    Rückgabedatum: Union[date, None] # kann bspw. beim Post auch noch nicht zurückgegeben worden sein
    Kunde_ID: str
    Film_ID: int
    Mitarbeiter_ID: Union[str, None] # es kann auch kein Mitarbeiter beraten haben