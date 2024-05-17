"""test_app.py"""
from streamlit.testing.v1 import AppTest

# def test_login():
#     "A user input the username and password, then clicks the login button"
#     at = AppTest.from_file("app.py").run()
#     at.text_input[0].input("jsmith").run()
#     at.text_input[1].input("abcd").run()
#     at.button[0].click().run()
#     assert at.error


def test_logout():
    "A user tries to logout from the project intro page"
    at = AppTest.from_file("../pages/0_project_introduction_page.py").run()
    at.button[0].click().run()
    assert at.switch_page

    at.

# def test_individual_price_analysis_page():
#     "A user tries to select the item_id from the page"
#     at = AppTest.from_file("../pages/1_individual_price_analysis")
