"""logout_test_app.py"""
from streamlit.testing.v1 import AppTest

def test_logout():
    "A user tries to logout from the project intro page"
    at = AppTest.from_file("0_project_introduction_page.py").run()
    at.button[0].click().run()
    assert at.switch_page