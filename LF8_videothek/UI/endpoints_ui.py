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

        async def load_ausleihen():
            async with httpx.AsyncClient() as client:
                response = await client.get('http://127.0.0.1:8000/ausleihe/')
                ausleihen = response.json()
                ausleihe_table.rows = ausleihen

        async def load_kunden():
            async with httpx.AsyncClient() as client:
                response = await client.get('http://127.0.0.1:8000/kunde/')
                kunden = response.json()
                kunden_table.rows = kunden

        async def load_mitarbeiter():
            async with httpx.AsyncClient() as client:
                response = await client.get('http://127.0.0.1:8000/mitarbeiter/')
                mitarbeiter = response.json()
                mitarbeiter_table.rows = mitarbeiter

        ui.add_css(
            """
            body.body--dark .app-drawer {
                background-color: #4c4141 !important;
            }
            body:not(.body--dark) .app-drawer {
                background-color: #FFDBDB !important;
            }
            """
            """
                .custom-toggle .q-toggle__inner--falsy .q-toggle__track {
                    background-color: gray;
                }
                .custom-toggle .q-toggle__inner--falsy .q-toggle__thumb::after {
                    background-color: salmon;
                }
                
            """
        )

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

        with ui.tab_panels(tabs).classes('w-full').props('transition-prev=jump-up transition-next=jump-up'):

            with ui.tab_panel('Filme'):
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

            with ui.tab_panel('Ausleihen'):
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

            with ui.tab_panel('Kunden'):
                ui.label('Kunden Übersicht').classes('text-xl font-bold')

                kunden_columns = [{'name': 'Kunde_ID', 'label': 'ID', 'field': 'Kunde_ID'},
                                  {'name': 'Vorname', 'label': 'Vorname', 'field': 'Vorname'},
                                  {'name': 'Nachname', 'label': 'Nachname', 'field': 'Nachname'},
                                  {'name': 'Geburtstag', 'label': 'Geburtstag', 'field': 'Geburtstag'},
                                  {'name': 'Straße_Nr', 'label': 'Straße / Nr.', 'field': 'Straße_Nr'},
                                  {'name': 'PLZ', 'label': 'PLZ', 'field': 'PLZ'},
                                  {'name': 'City', 'label': 'Stadt', 'field': 'City'},
                ]
                kunden_table = ui.table(columns=kunden_columns, rows=[]).classes('w-full')
                ui.button('Kunden laden', on_click=load_kunden, color='red')

            with ui.tab_panel('Mitarbeiter'):
                ui.label('Mitarbeiter Übersicht').classes('text-xl font-bold')

                mitarbeiter_columns = [
                    {'name': 'Mitarbeiter_ID', 'label': 'ID', 'field': 'Mitarbeiter_ID'},
                    {'name': 'Vorname', 'label': 'Vorname', 'field': 'Vorname'},
                    {'name': 'Nachname', 'label': 'Nachname', 'field': 'Nachname'},
                ]

                mitarbeiter_table = ui.table(columns=mitarbeiter_columns, rows=[]).classes('w-full')
                ui.button('Mitarbeiter laden', on_click=load_mitarbeiter, color='red')


