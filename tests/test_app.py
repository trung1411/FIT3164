"""test_app.py"""
from streamlit.testing.v1 import AppTest




def test_login():
    "A user input the username and password, then clicks the login button"
    at = AppTest.from_file("app.py").run()
    at.text_input[0].input("jsmith").run()
    at.text_input[1].input("abcd").run()
    at.button[0].click().run()
    assert at.error[0].value == "Username/password is incorrect"


