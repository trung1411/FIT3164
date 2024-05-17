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
    at.button[1].click().run()
    assert at.switch_page

def test_traversing_through_pages():
    "Assuming users start at the project introduction page"
    at2 = AppTest.from_file("../pages/0_project_introduction_page.py").run()
    at2.button[1].click().run()
    assert at2.success
    # Assert if there is a page switch
    assert at2.switch_page
    
    # #Assume the users pick one value of item_id from the selectbox in the sidebar
    # at2.sidebar.selectbox.select("HOUSEHOLD_2_516").run()

    # assert not at2.exception

def test_page2():
    #Loading page 2
    at3 = AppTest.from_file("../pages/1_📈individual_price_analysis.py").run()
    #Check if the header of the page is correct
    assert at3.header[0].value == "Individual item price analysis" 
    item_id = "HOUSEHOLD_2_516"
    #Setting the value of the item_id selectbox to be the same as item_id
    at3.selectbox[0].select(item_id).run()
    #CHeck if the title for the graph changes
    assert at3.markdown[1].value == "This is the line graph showing price analysis of {a}".format(a = item_id)


def test_page3():
    #Loading page 3
    at4 = AppTest.from_file("../pages/2_📈individual_sales_analysis.py").run()
    #Check if the header of the page is correct
    assert at4.header[0].value == "Individual item sales analysis" 
    item_id = "FOODS_3_827"
    store_id = "CA_1"
    # Setting the value for item_id selectbox
    at4.selectbox[0].select(item_id).run()
    # Setting the value for store_id selectbox
    at4.selectbox[1].select(store_id).run()

    assert not at4.exception

def test_page4():
    #Loading page 4
    at4 = AppTest.from_file("../pages/3_📈department_sales_analysis.py").run()
    #Check if the header of the page is correct
    assert at4.header[0].value == "Department sales analysis" 
    dept_id = "HOUSEHOLD_2"
    # Setting the value for dept_id selectbox
    at4.selectbox[0].select(dept_id).run()

    assert not at4.exception

def test_page5():
    #Loading page 5
    at4 = AppTest.from_file("../pages/4_💲price_elasticity_modelling.py").run()
    #Check if the header of the page is correct
    assert at4.header[0].value == "Price Elasticity Modelling for individual products" 
    item_id = "HOUSEHOLD_2_516"
    # Setting the value for dept_id selectbox
    at4.selectbox[0].select(item_id).run()
    assert not at4.exception

def test_page6():
    #Loading page 6
    at4 = AppTest.from_file("../pages/4_💲department_price_elasticity_modelling.py").run()
    #Check if the header of the page is correct
    assert at4.header[0].value == "Price Elasticity Modelling aggregated by deparments"
    dept_id = "HOBBIES_2"
    # Setting the value for dept_id selectbox
    at4.selectbox[0].select(dept_id).run()
    assert not at4.exception


# def test_individual_price_analysis_page():
#     "A user tries to select the item_id from the page"
#     at = AppTest.from_file("../pages/1_individual_price_analysis")
