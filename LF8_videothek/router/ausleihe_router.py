from fastapi import APIRouter
from mariadb import IntegrityError

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
    try:
        cur.execute(
            "INSERT INTO ausleihe (Ausleihdatum, Rückgabedatum, Kunde_ID, Film_ID, Mitarbeiter_ID) VALUES (?, ?, ?, ?, ?)",
            (ausleihe.Ausleihdatum, ausleihe.Rückgabedatum, ausleihe.Kunde_ID, ausleihe.Film_ID, ausleihe.Mitarbeiter_ID)
        )
        conn.commit()
    except IntegrityError:
        conn.close()
        return {"Error": "Ausleihdatum größer Rückgabedatum (muss kleiner sein oder Rückgabe = null)"}
    else:
        conn.close()
        return {"message": "Ausleihe created"}

@router.put("/{ausleihe_id}")
def change_film(ausleihe: Ausleihe):
    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute(
            "UPDATE Ausleihe SET Ausleihdatum = %s, Rückgabedatum = %s, Kunde_ID = %s, Film_ID = %s, Mitarbeiter_ID = %s Where Ausleihe_ID = %s",
            (ausleihe.Ausleihdatum, ausleihe.Rückgabedatum, ausleihe.Kunde_ID, ausleihe.Film_ID, ausleihe.Mitarbeiter_ID, ausleihe.Ausleihe_ID)
        )
        conn.commit()
    except IntegrityError:
        conn.close()
        return {"Error": "Ausleihdatum größer Rückgabedatum (muss kleiner sein oder Rückgabe = null)"}
    else:
        conn.close()
        return {"message": "Ausleihe updated"}

@router.delete("/{ausleihe_id}")
def delete_film(ausleihe_id: int):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "DELETE FROM Ausleihe WHERE AUsleihe_ID = %s",
        (ausleihe_id,)
    )
    conn.commit()
    conn.close()
    return {"message": "Ausleihe deleted"}