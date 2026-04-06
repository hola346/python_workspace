from playwright.async_api import Playwright

import os
import sys

import pytest

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../3_StandAlone_tests")

from test_createUser_withJSONf import test_login
import time

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../data")
from class_apiBase_withJSONf import APIUtils


"""THIS WAS VERIFIED TO BE WORKING FINE, DO NOT MODIFY"""

"""BEST PRACTICES:
- User info (email, password, username..) should not be hardcored, but saved in separated files - JSON
- code should be modular and reusable - use classes, functions, etc
- Organize py - JSONs - class files adequatly in folders
- provide var / function names with self-explanatory names
- proper indentation to visually see the extension of structures - jsons, functions...
- comment lines or functions for better human understanding

"""


@pytest.mark.webapi4
def test_e2e_webapi(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    api_Utils = APIUtils()
    response_order_OK = api_Utils.createOrder(playwright)
    print("This is the value in e2e_webapi of response_order_OK: ", response_order_OK)

    test_login(page)

    # page.locator("button", name="ORDERS").click()
    page.locator(".fa-handshake-o").click()
    orderNum = str(response_order_OK["orders"])

    orderNum = orderNum.replace("'", "")
    orderNum = orderNum.replace("[", "")
    orderNum = orderNum.replace("]", "")

    print("printing order number????", orderNum)

    """    row = page.locator("tr").filter(
        has_text="Rice"
    )  # you don't pick here index of the row, but the FULL ROW.
    expect(row.locator("td").nth(colvalue)).to_have_text("37")
    # print(Row.nth())"""

    row = page.locator("tr").filter(has_text=orderNum)
    time.sleep(5)
    row.get_by_role("button", name="View").click()
    # ----->expect(page.locator(".tagline")).to_have_text("Thank you for Shopping With Us")
    # expect(page.locator(".tagline")).to_contain_text("you for Shopping")

    time.sleep(5)
