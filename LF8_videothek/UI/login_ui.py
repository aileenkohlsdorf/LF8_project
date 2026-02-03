# import os
# from nicegui import ui
# from dotenv import load_dotenv
#
# load_dotenv('C:\dev\java\LF8_project\LF8_videothek')
#
# def setup_login():
#     @ui.page('/login')
#     def login_page():
#         username = ui.input('Username')
#         password = ui.input('Password', password=True)
#
#         def do_login():
#             if username.value == os.getenv('LOGIN_USERNAME') and password.value == os.getenv('LOGIN_PASSWORD'):
#                 ui.context.client.storage['logged_in'] = True
#                 ui.navigate.to('/test')
#             else:
#                 ui.notify('Invalid credentials', color='red')
#
#         ui.button('Login', on_click=do_login)