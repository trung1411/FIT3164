"""test_app.py"""
from streamlit.testing.v1 import AppTest

def test_login():
    "A user input the username and password, then clicks the login button"'
    at = AppTest.from_file("app.py").run()
    at.