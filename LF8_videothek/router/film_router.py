from fastapi import APIRouter
from db import get_connection
from models.Film import Film

router = APIRouter(prefix="/films", tags=["Films"])  ##für die URL .../films/

@router.get("/")
def get_films():
    conn = get_connection() ## Verbindung zu Datenbank
    cur = conn.cursor()
    cur.execute("SELECT * FROM film")
    rows = cur.fetchall()
    columns = [col[0] for col in cur.description] ## col[0] = Spaltenname - wird in den Schlüssel für das json Key-Value-Paar aufgelöst
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
        "INSERT INTO film (Titel, Erscheinungsjahr, Genre, Altersfreigabe) VALUES (?, ?, ?, ?)",
        (film.Titel, film.Erscheinungsjahr, film.Genre, film.Altersfreigabe)
    )
    conn.commit()
    conn.close()
    return {"message": "Film created"}

@router.put("/{film_id}")
def change_film(film: Film):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "UPDATE film SET Titel = %s, Erscheinungsjahr = %s, Genre = %s, Altersfreigabe = %s Where Film_ID = %s",
        (film.Titel, film.Erscheinungsjahr, film.Genre, film.Altersfreigabe, film.Film_ID)
    )
    conn.commit()
    conn.close()
    return {"message": "Film updated"}

@router.delete("/{film_id}")
def delete_film(film_id: int):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "DELETE FROM film WHERE Film_ID = %s",
        (film_id,)
    )
    conn.commit()
    conn.close()
    return {"message": "Film deleted"}