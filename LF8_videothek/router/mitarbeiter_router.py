from fastapi import APIRouter
from db import get_connection
from models.Mitarbeiter import Mitarbeiter

router = APIRouter(prefix="/mitarbeiter", tags=["Mitarbeiter"])

@router.get("/")
def get_mitarbeiter():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM mitarbeiter")
    rows = cur.fetchall()
    columns = [col[0] for col in cur.description]
    conn.close()
    return [dict(zip(columns, row)) for row in rows]

@router.post("/")
def create_mitarbeiter(mitarbeiter: Mitarbeiter):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO mitarbeiter (Vorname, Nachname) VALUES (?, ?)",
        (mitarbeiter.Vorname, mitarbeiter.Nachname)
    )
    conn.commit()
    conn.close()
    return {"message": "Mitarbeiter created"}

@router.put("/{mitarbeiter_id}")
def change_film(mitarbeiter_id: int, mitarbeiter: Mitarbeiter):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "UPDATE mitarbeiter SET Vorname = %s, Nachname = %s Where Mitarbeiter_ID = %s",
        (mitarbeiter.Vorname, mitarbeiter.Nachname, mitarbeiter_id)
    )
    conn.commit()
    conn.close()
    return {"message": "Mitarbeiter updated"}

@router.delete("/{mitarbeiter_id}")
def delete_film(mitarbeiter_id: int):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "DELETE FROM mitarbeiter WHERE Mitarbeiter_ID = %s",
        (mitarbeiter_id,)
    )
    conn.commit()
    conn.close()
    return {"message": "Mitarbeiter deleted"}