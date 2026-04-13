import os
import sys

from playwright.async_api import Playwright

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../3_StandAlone_tests")
from test_createUser_withJSONf_PARAM import test_login
import json, pytest, time

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../data")

from class_apiBase_withJSONf_PARAM import APIUtils

"""WE'LL TRY TO PARAM API CALL"""

with open(
    "C:\\python\\python_workspace\\pytest_python\\playwright\\data\\another_cred.json"
) as f:
    credentials = json.load(f)
    cred = credentials["UserCredentials"]


@pytest.mark.parametrize("user_credentials", cred)
def test_e2e_webapi(playwright: Playwright, user_credentials):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    api_Utils = APIUtils()
    response_order_OK = api_Utils.createOrder(playwright, user_credentials)
    print("This is the value in e2e_webapi of response_order_OK: ", response_order_OK)

    test_login(page, user_credentials)

    # page.locator("button", name="ORDERS").click()
    page.locator(".fa-handshake-o").click()
    orderNum = str(response_order_OK["orders"])

    orderNum = orderNum.replace("'", "")
    orderNum = orderNum.replace("[", "")
    orderNum = orderNum.replace("]", "")

    print("printing order number????", orderNum)

    row = page.locator("tr").filter(has_text=orderNum)
    time.sleep(5)
    row.get_by_role("button", name="View").click()
    # ----->expect(page.locator(".tagline")).to_have_text("Thank you for Shopping With Us")
    # expect(page.locator(".tagline")).to_contain_text("you for Shopping")

    time.sleep(5)
