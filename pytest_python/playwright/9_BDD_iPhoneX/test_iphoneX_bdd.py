import os
import sys
import pytest
from pytest_bdd import given, when, then, scenarios, parsers

# Add parent PageObject directory to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../8_iPhoneX_test")

from login_page import LoginPage
from shop_page import ShopPage

scenarios("iPhoneX.feature")


@pytest.fixture()
def shared_data():
    """Fixture to share data between steps"""
    return {}


@given("user navigates to login page")
def user_navigates_to_login_page(browserInstance, shared_data):
    """Navigate to login page"""
    print("GIVEN: User navigates to login page")
    login_page = LoginPage(browserInstance)
    login_page.navigate()
    shared_data["login_page"] = login_page


@when(
    parsers.parse('user enters username "{username}" and password "{password}"')
)
def user_enters_credentials(shared_data, username, password):
    """Enter username and password"""
    print(f"WHEN: User enters username '{username}' and password")
    shared_data["username"] = username
    shared_data["password"] = password


@when("user selects terms checkbox")
def user_selects_terms_checkbox(shared_data):
    """Select terms checkbox - done within login method"""
    print("WHEN: User selects terms checkbox")
    shared_data["terms_checked"] = True


@when("user clicks on Sign In button")
def user_clicks_signin_button(shared_data):
    """Click Sign In button and navigate to shop page"""
    print("WHEN: User clicks on Sign In button")
    login_page = shared_data["login_page"]
    shop_page = login_page.login(shared_data["username"], shared_data["password"])
    shared_data["shop_page"] = shop_page


@then("user is navigated to shop page")
def user_navigated_to_shop_page(browserInstance, shared_data):
    """Verify user is on shop page"""
    print("THEN: User is navigated to shop page")
    assert "angularpractice/shop" in browserInstance.url


@then("iPhone X product should be present on the page")
def iphone_x_product_present(shared_data):
    """Verify iPhone X product is present"""
    print("THEN: Verifying iPhone X product is present")
    shop_page = shared_data["shop_page"]
    assert shop_page.is_iphone_x_present(), "iPhone X product is NOT present on the shop page"
