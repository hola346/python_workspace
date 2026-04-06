import os
import sys

import pytest

from pytest_bdd import given, scenarios, then, when, parsers

sys.path.append(
    os.path.dirname(os.path.abspath(__file__)) + "/../6_TCs_with_classes_PageObject"
)

from class_login import LoginPage
from class_apiBase_withJSONf_PARAM import APIUtils

from test_e2e_webapi_PageObject import arrangeOrderNum


scenarios(
    "orderTransaction.feature"
)  # we are linking here the feature file to this test script, so we can execute the steps defined in the feature file, and we can use the same steps in other test scripts if we want to, since we are linking the feature file to this test script, but if we want to link it to another test script, we can do it by defining the steps in that test script and then linking the feature file to that test script, but since we want to link it to this test script, we will define the steps in this test script and then link the feature file to this test script


@pytest.fixture()
def shared_data():
    return {}


# we create this fixture in order to extract data from steps and use it in other steps, since we want to use the same data for all the steps in the scenario, but if we want to use different data for each step, we can define it in each step, but since we want to use the same data for all the steps in the scenario, we will use this fixture to share data between steps, since we want to use the same data for all the steps in the scenario, but if we want to use different data for each step, we can define it in each step, but since we want to use the same data for all the steps in the scenario, we will use this fixture to share data between steps
# note is empty dictionary, we will create keys and assign values to it in the steps, so we can use those keys to access the values in other steps, since we want to use the same data for all the steps in the scenario, but if we want to use different data for each step, we can define it in each step, but since we want to use the same data for all the steps in the scenario, we will use this fixture to share data between steps, since we want to use the same data for all the steps in the scenario, but if we want to use different data for each step, we can define it in each step, but since we want to use the same data for all the steps in the scenario, we will use this fixture to share data between steps


# @given("Login by API using {credentials} and create order")
# we are using credentials from feature file, not from JSON, since we want to use parameterization in feature file, so we can run the same test with different credentials, but if we want to use credentials from JSON, we can use the function defined in class_apiBase_withJSONf_PARAM and call it here, but since we want to use parameterization in feature file, we will use credentials from feature file, so we can run the same test with different credentials, but if we want to use credentials from JSON, we can use the function defined in class_apiBase_withJSONf_PARAM and call it here, but since we want to use parameterization in feature file, we will use credentials from feature file, so we can run the same test with different credentials


@given(parsers.parse("Login by API using {username} and {password} and create order"))
def login_by_api(playwright, username, password, shared_data):
    credentials = {"userEmail": username, "userPassword": password}
    print("THIS IS FIRST GIVEN: credentials: ", credentials)
    api_Utils = APIUtils()
    response_order_OK = api_Utils.createOrder(playwright, credentials)
    print("THIS IS FIRST GIVEN: response_order_OK: ", response_order_OK)
    shared_data["response_order_OK"] = response_order_OK


@given("take note of the ORDER number")
def take_note_of_order_number(shared_data):
    shared_data["orderNum"] = arrangeOrderNum(shared_data["response_order_OK"])
    print("THIS IS 2ND GIVEN, which arranges order number: ", shared_data["orderNum"])


@given("user is on landing page")
def user_is_on_landing_page(browserInstance, shared_data):
    # we are using browserInstance from conftest.py - fixture, since we want to use the same browser instance for all the steps in the scenario, but if we want to use a different browser instance for each step, we can define it in each step, but since we want to use the same browser instance for all the steps in the scenario, we will use browserInstance from conftest.py, since we want to use the same browser instance for all the steps in the scenario, but if we want to use a different browser instance for each step, we can define it in each step, but since we want to use the same browser instance for all the steps in the scenario, we will use browserInstance from conftest.py
    # we are using shared_data to share data between steps, since we want to use the same loginPageObj for all the steps in the scenario, but if we want to use a different loginPageObj for each step, we can define it in each step, but since we want to use the same loginPageObj for all the steps in the scenario, we will use shared_data to share data between steps, since we want to use the same loginPageObj for all the steps in the scenario, but if we want to use a different loginPageObj for each step, we can define it in each step, but since we want to use the same loginPageObj for all the steps in the scenario, we will use shared_data to share data between steps
    # notice at the begining of definition, we have an empty dictionary, we are creating here a key with name "loginPageObj" and we are assigning to it the value of loginPageObj, so we can use it in other steps, since we want to use the same loginPageObj for all the steps in the scenario, but if we want to use a different loginPageObj for each step, we can define it in each step, but since we want to use the same loginPageObj for all the steps in the scenario, we will use shared_data to share data between steps, since we want to use the same loginPageObj for all the steps in the scenario, but if we want to use a different loginPageObj for each step, we can define it in each step, but since we want to use the same loginPageObj for all the steps in the scenario, we will use shared_data to share data between steps
    print("User is on landing page")
    loginPageObj = LoginPage(browserInstance)
    loginPageObj.navigate()
    shared_data["loginPageObj"] = loginPageObj


# @when("Login to the application using UI with same {credentials}")
@when(
    parsers.parse(
        "Login to the application using UI with same {username} and {password}"
    )
)
def login_to_application_UI(shared_data, username, password):
    credentials = {"userEmail": username, "userPassword": password}
    dashboardObj = shared_data["loginPageObj"].login(credentials)
    shared_data["dashboardObj"] = dashboardObj
    print("WHEN 1, which logs in using UI: credentials: ", credentials)


@when("go to order history")
def go_to_order_history(shared_data):
    OrderList = shared_data["dashboardObj"].select_Orders()
    shared_data["OrderList"] = OrderList
    print("WHEN 2, which goes to order history: ")


@when("select order details using previous ORDER number")
def select_order_details(shared_data):
    OrderDetailsObj = shared_data["OrderList"].viewOrder(shared_data["orderNum"])
    shared_data["OrderDetailsObj"] = OrderDetailsObj
    print("WHEN 3, which selects order details: ")


@then(
    'Validate the order details - order message should be "Thank you for Shopping With Us"'
)
def validate_order_details(shared_data):
    shared_data["OrderDetailsObj"].test_order_details()
    print("THEN, which validates order details: ")
