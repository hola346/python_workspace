import pytest
import json
import os
from playwright.async_api import Playwright
from login_page import LoginPage


# Load credentials from JSON file (using absolute path based on this file's location)
current_dir = os.path.dirname(os.path.abspath(__file__))
credentials_path = os.path.join(current_dir, "credentials.json")
with open(credentials_path) as f:
    credentials = json.load(f)
    cred = credentials["user_credentials"]


@pytest.fixture(scope="function")
def browserInstance(playwright, request):
    """Browser fixture following existing framework pattern"""
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()
    browser.close()


def test_iphone_x_present(browserInstance):
    """
    Test to verify iPhone X product is present after login

    Steps:
    1. Navigate to login page
    2. Enter credentials from credentials.json
    3. Select terms checkbox
    4. Click Sign In button
    5. Wait for navigation to shop page
    6. Verify iPhone X product is present
    """
    page = browserInstance

    # GIVEN: User is on login page
    login_page = LoginPage(page)
    login_page.navigate()

    # WHEN: User logs in with valid credentials from JSON file
    shop_page = login_page.login(cred["username"], cred["password"])

    # THEN: Verify iPhone X product is present on the shop page
    assert shop_page.is_iphone_x_present(), "iPhone X product is NOT present on the shop page"
