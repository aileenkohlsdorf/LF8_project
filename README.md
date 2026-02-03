# LF8_project
Projekt für LF8

# Filmverleih REST API

Dieses Projekt stellt eine RESTful API zur Verwaltung eines Filmverleihsystems bereit.  
Über die API können Filme, Kunden, Mitarbeiter und Ausleihen verwaltet werden.  
Die Daten werden in einer relationalen Datenbank gespeichert.

## Technologien
- REST API
- Relationale Datenbank (z. B. MySQL / PostgreSQL)
- Git für Versionsverwaltung  
*(Framework/Programmiersprache je nach Implementierung)*

## Datenmodell

<img width="821" height="799" alt="Videothek_V2 drawio" src="https://github.com/user-attachments/assets/e9fa23a4-dd14-4e2c-b1bb-15a82f3bb4b4" />


### Entitäten

#### Film
- Titel
- Erscheinungsjahr
- Genre
- Altersfreigabe

#### Kunde
- Vorname
- Nachname
- Alter
- Adresse

#### Mitarbeiter
- Vorname
- Nachname

#### Ausleihe
- Ausleihdatum
- Rückgabedatum

### Beziehungen
- Ein Kunde kann mehrere Filme ausleihen
- Ein Film kann mehrfach ausgeliehen werden (zu unterschiedlichen Zeitpunkten)
- Eine Ausleihe ist genau einem Kunden, einem Film und einem Mitarbeiter zugeordnet

## REST API Endpunkte (Beispiel)

### Filme
- `GET /api/filme` – Alle Filme abrufen
- `GET /api/filme/{id}` – Film nach ID abrufen
- `POST /api/filme` – Neuen Film anlegen
- `PUT /api/filme/{id}` – Film aktualisieren
- `DELETE /api/filme/{id}` – Film löschen

### Kunden
- `GET /api/kunden`
- `POST /api/kunden`

### Mitarbeiter
- `GET /api/mitarbeiter`
- `POST /api/mitarbeiter`

### Ausleihe
- `POST /api/ausleihen` – Film ausleihen
- `PUT /api/ausleihen/{id}` – Film zurückgeben
- `GET /api/ausleihen`

## Beispiel JSON für eine Ausleihe

```json
{
  "filmId": 1,
  "kundeId": 3,
  "mitarbeiterId": 2,
  "ausleihdatum": "2026-01-16"
}
```

### Requirements / Dependencies
- pydantic (py -m pip install pydantic)
- mariadb  (py -m pip install mariadb)
- dotenv   (py -m pip install python-dotenv)

### Startup
- py -m fastapi dev API.py
