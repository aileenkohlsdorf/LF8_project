from fastapi import APIRouter
from db import get_connection
from models.Ausleihe import Ausleihe
from models.Mitarbeiter import Mitarbeiter

router = APIRouter(prefix="/ausleihe", tags=["Ausleihe"])

@router.get("/")
def get_ausleihe():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM ausleihe")
    rows = cur.fetchall()
    columns = [col[0] for col in cur.description]
    conn.close()
    return [dict(zip(columns, row)) for row in rows]

@router.post("/")
def create_ausleihe(ausleihe: Ausleihe):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO ausleihe (Ausleihdatum, Rückgabedatum, Kunde_ID, Film_ID, Mitarbeiter_ID) VALUES (?, ?, ?, ?, ?)",
        (ausleihe.Ausleihdatum, ausleihe.Rückgabedatum, ausleihe.Kunde_ID, ausleihe.Film_ID, ausleihe.Mitarbeiter_ID)
    )
    conn.commit()
    conn.close()
    return {"message": "Ausleihe created"}
