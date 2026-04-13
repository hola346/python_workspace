from playwright.async_api import Playwright, Page

import os
import sys

import pytest

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../data")

from class_apiBase import APIUtils
import time

"""THIS WORKS FINE ALMOST, THING WITH EXPECT WHEN NOT USING PAGE BUT PLAYWRIGHT"""


"""The idea: everytime I login in, my generated token - see token caught in API testing in class -
is created and maintained throughout navigation. Therefore if I'm able to create and pass the token in 
navigation, I can really skip the login process, and test directly the webs/URLs, saving execution time if you 
are running a test set with many test cases.
On web navigation, TOKEN once created is kept in LOCAL STORAGE"""


def test_session_storage(playwright: Playwright, page: Page):
    api_utils = APIUtils()
    getToken = api_utils.getToken(playwright)
    print("this is recovered token: ", getToken)

    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    #### we need to insert token in web local storage to access directly to URL with no login - this is JS:
    page.add_init_script(f"""localStorage.setItem('token', '{getToken}')""")
    page.goto("https://rahulshettyacademy.com/client")

    page.get_by_role("button", name="ORDERS").click()
    time.sleep(5)
    """expect(
        page.get_by_text("Your Orders")
    ).to_be_visible()  ################################"""
    time.sleep(5)
