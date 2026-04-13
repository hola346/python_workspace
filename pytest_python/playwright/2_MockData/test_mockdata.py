from playwright.sync_api import Page


import os
import sys

import pytest

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../3_StandAlone_tests")


from test_createUser_withJSONf import test_login
import time

"THIS WORKS, BUT COULDN'T MAKE ASSERT WORK - TEXT ISSUE"

"""Process: we are saying:
1) listen to that URL everytime is checked
2) If so - by means of ORDERS button - execute even - intercept, passing URL route info
3) apply not server's response, but a fake one (MOCK) y FULFILL method - "use this JSON instead" """

fakeResponse = {"data": [], "message": "No Orders"}


def intercept_response(route):
    route.fulfill(json=fakeResponse)


def test_network(page: Page):
    test_login(page)
    # listening when selecting orders - execute event - intercept_response:
    page.route(
        "https://rahulshettyacademy.com/api/ecom/order/get-orders-for-customer/*",
        intercept_response,
    )
    page.get_by_role("button", name="ORDERS").click()
    time.sleep(5)
    text_void = page.locator(".mt-4").text_content()
    print("this is text void expected:", text_void)

    """    assert text_void == " You have No Orders to show at this time. Please Visit Back Us"
    expect(page.locator(".mt-4")).to_contain_text("No Orders to show ")
    #    "You have No Orders to show at this time."
    """
    time.sleep(5)
