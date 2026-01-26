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
        "INSERT INTO mitarbeiter (Vorname, Nachname) VALUES (?, ?, ?, ?, ?, ?)",
        (mitarbeiter.Vorname, mitarbeiter.Nachname)
    )
    conn.commit()
    conn.close()
    return {"message": "Mitarbeiter created"}
