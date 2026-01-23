from pydantic import BaseModel
from datetime import date
from dataclasses import dataclass

@dataclass # like lombok
class Ausleihe(BaseModel):

    Ausleihe_ID: int
    Ausleihdatum: date
    Rückgabedatum: date
    Kunde_ID: int
    Film_ID: int
    Mitarbeiter_ID: int

## was just for testing
## print(Ausleihe(Ausleihe_ID = 1, Ausleihdatum = '2026-02-02', Rückgabedatum = '2026-02-03', Kunde_ID = 2, Film_ID = 2, Mitarbeiter_ID = 3).model_dump())