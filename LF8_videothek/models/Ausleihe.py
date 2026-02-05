from typing import Union

from pydantic import BaseModel
from datetime import date
from dataclasses import dataclass

from pydantic_core.core_schema import nullable_schema


@dataclass # like lombok
class Ausleihe(BaseModel):

    __Ausleihe_ID__ = int
    __Ausleihdatum__: date
    __Rückgabedatum__: Union[date, None] # kann bspw. beim Post auch noch nicht zurückgegeben worden sein
    __Kunde_ID__: int
    __Film_ID__: int
    __Mitarbeiter_ID__: Union[int, None] # es kann auch kein Mitarbeiter beraten haben