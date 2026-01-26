from fastapi import APIRouter
from db import get_connection
from models.Kunde import Kunde

router = APIRouter(prefix="/kunde", tags=["Kunden"])

@router.get("/")
def get_kunden():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM kunde")
    rows = cur.fetchall()
    columns = [col[0] for col in cur.description]
    conn.close()
    return [dict(zip(columns, row)) for row in rows]

@router.post("/")
def create_kunde(kunde: Kunde):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO kunde (Vorname, Nachname, Geburtstag, Straße_Nr, PLZ, City) VALUES (?, ?, ?, ?, ?, ?)",
        (kunde.Vorname, kunde.Nachname, kunde.Geburtstag, kunde.Straße_Nr, kunde.PLZ, kunde.City)
    )
    conn.commit()
    conn.close()
    return {"message": "Kunde created"}
