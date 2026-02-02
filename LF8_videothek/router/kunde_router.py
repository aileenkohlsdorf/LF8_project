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

@router.put("/{kunde_id}")
def change_film(kunde_id: int, kunde: Kunde):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "UPDATE Kunde SET Vorname = %s, Nachname = %s, Geburtstag = %s, Straße_Nr = %s, PLZ = %s, City = %s Where Kunde_ID = %s",
        (kunde.Vorname, kunde.Nachname, kunde.Geburtstag, kunde.Straße_Nr, kunde.PLZ, kunde.City, kunde.Kunde_ID)
    )
    conn.commit()
    conn.close()
    return {"message": "Kunde updated"}

@router.delete("/{kunde_id}")
def delete_film(kunde_id: int):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "DELETE FROM Kunde WHERE Kunde_ID = %s",
        (kunde_id,)
    )
    conn.commit()
    conn.close()
    return {"message": "Ausleihe deleted"}