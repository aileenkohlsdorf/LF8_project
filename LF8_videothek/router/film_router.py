from fastapi import APIRouter
from db import get_connection
from models.Film import Film

router = APIRouter(prefix="/films", tags=["Films"])

@router.get("/")
def get_films():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM film")
    rows = cur.fetchall()
    columns = [col[0] for col in cur.description]
    conn.close()
    return [dict(zip(columns, row)) for row in rows]

@router.get("/{film_id}")
def get_film(film_id: int):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM film WHERE film_id=?", (film_id,))
    row = cur.fetchone()
    if row is None:
        conn.close()
        return {"error": "Film not found"}

    columns = [col[0] for col in cur.description]
    conn.close()
    return dict(zip(columns, row))


@router.post("/")
def create_film(film: Film):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO film (Film_ID, Titel, Erscheinungsjahr, Genre, Altersfreigabe) VALUES (?, ?, ?, ?, ?)",
        (film.Film_ID, film.Titel, film.Erscheinungsjahr, film.Genre, film.Altersfreigabe)
    )
    conn.commit()
    conn.close()
    return {"message": "Film created"}
