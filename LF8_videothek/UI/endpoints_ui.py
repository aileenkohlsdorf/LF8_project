from nicegui import ui
import httpx

def setup_pages():
    @ui.page('/')
    async def show_page():

        async def load_films():
            async with httpx.AsyncClient() as client:
                response = await client.get('http://127.0.0.1:8000/films/')
                films = response.json()
                film_table.rows = films

        async def post_film(film_id, titel, jahr, genre, fsk):
            async with httpx.AsyncClient() as client:
                payload = {
                    "Film_ID": film_id,
                    "Titel": titel,
                    "Erscheinungsjahr": jahr,
                    "Genre": genre,
                    "Altersfreigabe": fsk,
                }
                response = await client.post('http://127.0.0.1:8000/films/', json=payload)
                return response

        async def load_ausleihen():
            async with httpx.AsyncClient() as client:
                response = await client.get('http://127.0.0.1:8000/ausleihe/')
                ausleihen = response.json()
                ausleihe_table.rows = ausleihen

        async def post_ausleihe(ausleihe_id, ausleihdatum, rueckgabedatum, kunde_id, film_id, mitarbeiter_id):
            async with httpx.AsyncClient() as client:
                rueckgabedatum = rueckgabedatum or None
                mitarbeiter_id = mitarbeiter_id or None

                payload = {
                    "Ausleihe_ID": int(ausleihe_id),
                    "Ausleihdatum": ausleihdatum,
                    "Rückgabedatum": rueckgabedatum,
                    "Kunde_ID": int(kunde_id),
                    "Film_ID": int(film_id),
                    "Mitarbeiter_ID": int(mitarbeiter_id) if mitarbeiter_id else None,
                }

                response = await client.post(
                    'http://127.0.0.1:8000/ausleihe/',
                    json=payload
                )
                return response

        async def load_kunden():
            async with httpx.AsyncClient() as client:
                response = await client.get('http://127.0.0.1:8000/kunde/')
                kunden = response.json()
                kunden_table.rows = kunden

        async def post_kunde(kunde_id, kunde_vorname, kunde_nachname, geburtstag, strasse_nr, plz, city):
            async with httpx.AsyncClient() as client:
                payload = {
                    "Kunde_ID": kunde_id,
                    "Vorname": kunde_vorname,
                    "Nachname": kunde_nachname,
                    "Geburtstag": geburtstag,
                    "Straße_Nr": strasse_nr,
                    "PLZ": plz,
                    "City": city,
                }
                response = await client.post('http://127.0.0.1:8000/kunde/', json=payload)
                return response

        async def load_mitarbeiter():
            async with httpx.AsyncClient() as client:
                response = await client.get('http://127.0.0.1:8000/mitarbeiter/')
                mitarbeiter = response.json()
                mitarbeiter_table.rows = mitarbeiter

        async def post_mitarbeiter(mitarbeiter_id, vorname, nachname):
            async with httpx.AsyncClient() as client:
                payload = {
                    "Mitarbeiter_ID": mitarbeiter_id,
                    "Vorname": vorname,
                    "Nachname": nachname,
                }
                response = await client.post('http://127.0.0.1:8000/mitarbeiter/', json=payload)
                return response

        ui.add_css("""
            body.body--dark .app-drawer { background-color: #4c4141 !important; }
            body:not(.body--dark) .app-drawer { background-color: #FFDBDB !important; }

            body:not(.body--dark) .custom-toggle .q-toggle__track { background-color: gray !important; }
            body:not(.body--dark) .custom-toggle .q-toggle__thumb::after { background-color: red !important; }

            body.body--dark .custom-toggle .q-toggle__track { background-color: gray !important; }
            body.body--dark .custom-toggle .q-toggle__thumb::after { background-color: black !important; }
        """)

        ui.label("Ich geh springen hihi")

        with ui.header(elevated=True).style('background-color: #d60808').classes('items-center justify-between'):
            ui.label('VIDEOTHEK')
            dark = ui.dark_mode()
            ui.switch('Dark mode').bind_value(dark).classes('custom-toggle')

        with ui.left_drawer().classes('app-drawer').props('width=200 breakpoint=500'):
            with ui.tabs().props('vertical switch-indicator swipeable').classes('w-full') as tabs:
                ui.tab('Filme')
                ui.tab('Ausleihen')
                ui.tab('Kunden')
                ui.tab('Mitarbeiter')

        with ui.tab_panels(tabs).classes('w-full'):

            with ui.tab_panel('Filme'):

                with ui.tabs().classes('w-full') as film_actions:
                    ui.tab('GET')
                    ui.tab('POST')
                    ui.tab('PUT')
                    ui.tab('DELETE')

                with ui.tab_panels(film_actions).classes('w-full'):

                    with ui.tab_panel('GET'):
                        ui.label('Filme Übersicht').classes('text-xl font-bold')
                        columns = [
                            {'name': 'Film_ID', 'label': 'ID', 'field': 'Film_ID'},
                            {'name': 'Titel', 'label': 'Titel', 'field': 'Titel'},
                            {'name': 'Erscheinungsjahr', 'label': 'Jahr', 'field': 'Erscheinungsjahr'},
                            {'name': 'Genre', 'label': 'Genre', 'field': 'Genre'},
                            {'name': 'Altersfreigabe', 'label': 'FSK', 'field': 'Altersfreigabe'},
                        ]
                        film_table = ui.table(columns=columns, rows=[]).classes('w-full')
                        ui.button('Filme laden', on_click=load_films, color='red')

                    with ui.tab_panel('POST'):
                        ui.label("Neuen Film hinzufügen").classes('text-lg font-bold')

                        film_id = ui.input("Film_ID")
                        titel = ui.input("Titel")
                        jahr = ui.input("Erscheinungsjahr")
                        genre = ui.input("Genre")
                        fsk = ui.input("FSK")

                        async def submit_film():
                            resp = await post_film(film_id.value, titel.value, jahr.value, genre.value, fsk.value)
                            if resp.status_code in (200, 201):
                                ui.notify("Film erfolgreich hinzugefügt!", color="green")
                            else:
                                ui.notify(f"Fehler: {resp.text}", color="red")

                        ui.button("Film speichern", on_click=submit_film, color="red")

                    with ui.tab_panel('PUT'):
                        ui.label("Film bearbeiten").classes('text-lg font-bold')

                        put_film_id = ui.input("Film_ID (zu ändern)")
                        put_titel = ui.input("Neuer Titel")
                        put_jahr = ui.input("Erscheinungsjahr")
                        put_genre = ui.input("Genre")
                        put_fsk = ui.input("FSK")

                        async def submit_put_film():
                            payload = {
                                "Film_ID": int(put_film_id.value),
                                "Titel": put_titel.value,
                                "Erscheinungsjahr": put_jahr.value,
                                "Genre": put_genre.value,
                                "Altersfreigabe": put_fsk.value,
                            }

                            async with httpx.AsyncClient() as client:
                                resp = await client.put(f"http://127.0.0.1:8000/films/{put_film_id.value}",
                                                        json=payload)

                            if resp.status_code == 200:
                                ui.notify("Film erfolgreich geändert!", color="green")
                            else:
                                ui.notify(f"Fehler: {resp.text}", color="red")

                        ui.button("Film ändern", on_click=submit_put_film, color="red")

                    with ui.tab_panel('DELETE'):
                        ui.label("Film löschen").classes('text-lg font-bold')

                        del_film_id = ui.input("Film_ID (Pflicht)")

                        async def submit_delete_film():
                            if not del_film_id.value:
                                ui.notify("Bitte Film_ID angeben.", color="red")
                                return

                            async with httpx.AsyncClient() as client:
                                resp = await client.delete(f"http://127.0.0.1:8000/films/{del_film_id.value}")

                            if resp.status_code in (200, 204):
                                ui.notify("Film erfolgreich gelöscht!", color="green")
                            else:
                                ui.notify(f"Fehler: {resp.text}", color="red")

                        ui.button("Film löschen", on_click=submit_delete_film, color="red")

            with ui.tab_panel('Ausleihen'):

                with ui.tabs().classes('w-full') as aus_actions:
                    ui.tab('GET')
                    ui.tab('POST')
                    ui.tab('PUT')
                    ui.tab('DELETE')

                with ui.tab_panels(aus_actions).classes('w-full'):

                    with ui.tab_panel('GET'):
                        ui.label('Ausleihen Übersicht').classes('text-xl font-bold')
                        ausleihe_columns = [
                            {'name': 'Ausleihe_ID', 'label': 'ID', 'field': 'Ausleihe_ID'},
                            {'name': 'Ausleihdatum', 'label': 'Ausleihdatum', 'field': 'Ausleihdatum'},
                            {'name': 'Rückgabedatum', 'label': 'Rückgabedatum', 'field': 'Rückgabedatum'},
                            {'name': 'Kunde_ID', 'label': 'Kunde', 'field': 'Kunde_ID'},
                            {'name': 'Film_ID', 'label': 'Film', 'field': 'Film_ID'},
                            {'name': 'Mitarbeiter_ID', 'label': 'Mitarbeiter', 'field': 'Mitarbeiter_ID'},
                        ]
                        ausleihe_table = ui.table(columns=ausleihe_columns, rows=[]).classes('w-full')
                        ui.button('Ausleihen laden', on_click=load_ausleihen, color='red')

                    with ui.tab_panel('POST'):
                        ui.label("Neue Ausleihe hinzufügen").classes('text-lg font-bold')

                        aus_ausleihe_id     = ui.input("Ausleihe_ID")
                        aus_ausleihdatum    = ui.input("Ausleihdatum")
                        aus_rueckgabedatum  = ui.input("Rückgabedatum (optional)")
                        aus_kunde_id        = ui.input("Kunde_ID")
                        aus_film_id         = ui.input("Film_ID")
                        aus_mitarbeiter_id  = ui.input("Mitarbeiter_ID (optional)")

                        async def submit_ausleihe():
                            resp = await post_ausleihe(
                                aus_ausleihe_id.value,
                                aus_ausleihdatum.value,
                                aus_rueckgabedatum.value,
                                aus_kunde_id.value,
                                aus_film_id.value,
                                aus_mitarbeiter_id.value
                            )

                            if resp.status_code in (200, 201):
                                ui.notify("Ausleihe erfolgreich hinzugefügt!", color="green")
                            else:
                                ui.notify(f"Fehler: {resp.text}", color="red")

                        ui.button("Ausleihe speichern", on_click=submit_ausleihe, color="red")

                    with ui.tab_panel('PUT'):
                        ui.label("Ausleihe bearbeiten").classes('text-lg font-bold')

                        put_aus_id = ui.input("Ausleihe_ID (zu ändern)")
                        put_aus_datum = ui.input("Neues Ausleihdatum")
                        put_aus_rueck = ui.input("Neues Rückgabedatum (optional)")
                        put_aus_kunde = ui.input("Neuer Kunde_ID")
                        put_aus_film = ui.input("Neuer Film_ID")
                        put_aus_mitarbeiter = ui.input("Neuer Mitarbeiter_ID (optional)")

                        async def submit_put_ausleihe():
                            payload = {
                                "Ausleihe_ID": int(put_aus_id.value),
                                "Ausleihdatum": put_aus_datum.value,
                                "Rückgabedatum": put_aus_rueck.value or None,
                                "Kunde_ID": int(put_aus_kunde.value),
                                "Film_ID": int(put_aus_film.value),
                                "Mitarbeiter_ID": int(put_aus_mitarbeiter.value) if put_aus_mitarbeiter.value else None,
                            }

                            async with httpx.AsyncClient() as client:
                                resp = await client.put(f"http://127.0.0.1:8000/ausleihe/{put_aus_id.value}",
                                                        json=payload)

                            if resp.status_code == 200:
                                ui.notify("Ausleihe erfolgreich geändert!", color="green")
                            else:
                                ui.notify(f"Fehler: {resp.text}", color="red")

                        ui.button("Ausleihe ändern", on_click=submit_put_ausleihe, color="red")

                    with ui.tab_panel('DELETE'):
                        ui.label("Ausleihe löschen").classes('text-lg font-bold')

                        del_aus_id = ui.input("Ausleihe_ID (Pflicht)")

                        async def submit_delete_ausleihe():
                            if not del_aus_id.value:
                                ui.notify("Bitte Ausleihe_ID angeben.", color="red")
                                return

                            async with httpx.AsyncClient() as client:
                                resp = await client.delete(f"http://127.0.0.1:8000/ausleihe/{del_aus_id.value}")

                            if resp.status_code in (200, 204):
                                ui.notify("Ausleihe erfolgreich gelöscht!", color="green")
                            else:
                                ui.notify(f"Fehler: {resp.text}", color="red")

                        ui.button("Ausleihe löschen", on_click=submit_delete_ausleihe, color="red")

            with ui.tab_panel('Kunden'):

                with ui.tabs().classes('w-full') as kunden_actions:
                    ui.tab('GET')
                    ui.tab('POST')
                    ui.tab('PUT')
                    ui.tab('DELETE')

                with ui.tab_panels(kunden_actions).classes('w-full'):

                    with ui.tab_panel('GET'):
                        ui.label('Kunden Übersicht').classes('text-xl font-bold')
                        kunden_columns = [
                            {'name': 'Kunde_ID', 'label': 'ID', 'field': 'Kunde_ID'},
                            {'name': 'Vorname', 'label': 'Vorname', 'field': 'Vorname'},
                            {'name': 'Nachname', 'label': 'Nachname', 'field': 'Nachname'},
                            {'name': 'Geburtstag', 'label': 'Geburtstag', 'field': 'Geburtstag'},
                            {'name': 'Straße_Nr', 'label': 'Straße / Nr.', 'field': 'Straße_Nr'},
                            {'name': 'PLZ', 'label': 'PLZ', 'field': 'PLZ'},
                            {'name': 'City', 'label': 'Stadt', 'field': 'City'},
                        ]
                        kunden_table = ui.table(columns=kunden_columns, rows=[]).classes('w-full')
                        ui.button('Kunden laden', on_click=load_kunden, color='red')

                    with ui.tab_panel('POST'):
                        ui.label("Neuen Kunden hinzufügen").classes('text-lg font-bold')

                        kunde_id = ui.input("Kunde_ID")
                        kunde_vorname = ui.input("Vorname")
                        kunde_nachname = ui.input("Nachname")
                        geburtstag = ui.input("Geburtstag")
                        strasse_nr = ui.input("Straße / Nr.")
                        plz = ui.input("PLZ")
                        city = ui.input("City")

                        async def submit_kunde():
                            resp = await post_kunde(
                                kunde_id.value,
                                kunde_vorname.value,
                                kunde_nachname.value,
                                geburtstag.value,
                                strasse_nr.value,
                                plz.value,
                                city.value
                            )
                            if resp.status_code in (200, 201):
                                ui.notify("Kunde erfolgreich hinzugefügt!", color="green")
                            else:
                                ui.notify(f"Fehler: {resp.text}", color="red")

                        ui.button("Kunde speichern", on_click=submit_kunde, color="red")

                    with ui.tab_panel('PUT'):
                        ui.label("Kunde bearbeiten").classes('text-lg font-bold')

                        put_knd_id = ui.input("Kunde_ID (zu ändern)")
                        put_knd_vor = ui.input("Neuer Vorname")
                        put_knd_nach = ui.input("Neuer Nachname")
                        put_knd_geb = ui.input("Neuer Geburtstag")
                        put_knd_str = ui.input("Neue Straße / Nr.")
                        put_knd_plz = ui.input("Neue PLZ")
                        put_knd_city = ui.input("Neue Stadt")

                        async def submit_put_kunde():
                            payload = {
                                "Kunde_ID": int(put_knd_id.value),
                                "Vorname": put_knd_vor.value,
                                "Nachname": put_knd_nach.value,
                                "Geburtstag": put_knd_geb.value,
                                "Straße_Nr": put_knd_str.value,
                                "PLZ": put_knd_plz.value,
                                "City": put_knd_city.value,
                            }

                            async with httpx.AsyncClient() as client:
                                resp = await client.put(f"http://127.0.0.1:8000/kunde/{put_knd_id.value}", json=payload)

                            if resp.status_code == 200:
                                ui.notify("Kunde erfolgreich geändert!", color="green")
                            else:
                                ui.notify(f"Fehler: {resp.text}", color="red")

                        ui.button("Kunde ändern", on_click=submit_put_kunde, color="red")

                    with ui.tab_panel('DELETE'):
                        ui.label("Kunde löschen").classes('text-lg font-bold')

                        del_knd_id = ui.input("Kunde_ID (Pflicht)")

                        async def submit_delete_kunde():
                            if not del_knd_id.value:
                                ui.notify("Bitte Kunde_ID angeben.", color="red")
                                return

                            async with httpx.AsyncClient() as client:
                                resp = await client.delete(f"http://127.0.0.1:8000/kunde/{del_knd_id.value}")

                            if resp.status_code in (200, 204):
                                ui.notify("Kunde erfolgreich gelöscht!", color="green")
                            else:
                                ui.notify(f"Fehler: {resp.text}", color="red")

                        ui.button("Kunde löschen", on_click=submit_delete_kunde, color="red")

            with ui.tab_panel('Mitarbeiter'):

                with ui.tabs().classes('w-full') as mit_actions:
                    ui.tab('GET')
                    ui.tab('POST')
                    ui.tab('PUT')
                    ui.tab('DELETE')

                with ui.tab_panels(mit_actions).classes('w-full'):

                    with ui.tab_panel('GET'):
                        ui.label('Mitarbeiter Übersicht').classes('text-xl font-bold')
                        mitarbeiter_columns = [
                            {'name': 'Mitarbeiter_ID', 'label': 'ID', 'field': 'Mitarbeiter_ID'},
                            {'name': 'Vorname', 'label': 'Vorname', 'field': 'Vorname'},
                            {'name': 'Nachname', 'label': 'Nachname', 'field': 'Nachname'},
                        ]
                        mitarbeiter_table = ui.table(columns=mitarbeiter_columns, rows=[]).classes('w-full')
                        ui.button('Mitarbeiter laden', on_click=load_mitarbeiter, color='red')

                    with ui.tab_panel('POST'):
                        ui.label("Neuen Mitarbeiter hinzufügen").classes('text-lg font-bold')

                        mitarbeiter_id = ui.input("Mitarbeiter_ID")
                        vorname = ui.input("Vorname")
                        nachname = ui.input("Nachname")

                        async def submit_mitarbeiter():
                            resp = await post_mitarbeiter(
                                mitarbeiter_id.value,
                                vorname.value,
                                nachname.value
                            )
                            if resp.status_code in (200, 201):
                                ui.notify("Mitarbeiter erfolgreich hinzugefügt!", color="green")
                            else:
                                ui.notify(f"Fehler: {resp.text}", color="red")

                        ui.button("Mitarbeiter speichern", on_click=submit_mitarbeiter, color="red")

                    with ui.tab_panel('PUT'):
                        ui.label("Mitarbeiter bearbeiten").classes('text-lg font-bold')

                        put_mit_id = ui.input("Mitarbeiter_ID (zu ändern)")
                        put_mit_vor = ui.input("Neuer Vorname")
                        put_mit_nach = ui.input("Neuer Nachname")

                        async def submit_put_mitarbeiter():
                            payload = {
                                "Mitarbeiter_ID": int(put_mit_id.value),
                                "Vorname": put_mit_vor.value,
                                "Nachname": put_mit_nach.value,
                            }

                            async with httpx.AsyncClient() as client:
                                resp = await client.put(f"http://127.0.0.1:8000/mitarbeiter/{put_mit_id.value}",
                                                        json=payload)

                            if resp.status_code == 200:
                                ui.notify("Mitarbeiter erfolgreich geändert!", color="green")
                            else:
                                ui.notify(f"Fehler: {resp.text}", color="red")

                        ui.button("Mitarbeiter ändern", on_click=submit_put_mitarbeiter, color="red")

                    with ui.tab_panel('DELETE'):
                        ui.label("Mitarbeiter löschen").classes('text-lg font-bold')

                        del_mit_id = ui.input("Mitarbeiter_ID (Pflicht)")

                        async def submit_delete_mitarbeiter():
                            if not del_mit_id.value:
                                ui.notify("Bitte Mitarbeiter_ID angeben.", color="red")
                                return

                            async with httpx.AsyncClient() as client:
                                resp = await client.delete(f"http://127.0.0.1:8000/mitarbeiter/{del_mit_id.value}")

                            if resp.status_code in (200, 204):
                                ui.notify("Mitarbeiter erfolgreich gelöscht!", color="green")
                            else:
                                ui.notify(f"Fehler: {resp.text}", color="red")

                        ui.button("Mitarbeiter löschen", on_click=submit_delete_mitarbeiter, color="red")