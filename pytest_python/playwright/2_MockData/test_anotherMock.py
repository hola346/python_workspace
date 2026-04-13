from playwright.sync_api import Page

import os
import sys

import pytest

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../3_StandAlone_tests")

from test_createUser_withJSONf import test_login
import time

"""THIS WORKS AS EXPECTED"""

"""Same thing with order details
Here instead of insert a fake json file, we are going to redirect the URL to a fake one - ROUTE(CONTINUE_
In this case, our user has no auth to see that URL, therefore we'll get an error message for our user
but same button was clicked as before
Before we were mocking RESPONSE - json FILE, now we are mocking REQUEST - URL"""


def intercept_Request(route):
    route.continue_(url="https:\\wwww.google.com")


def test_network2(page: Page):
    test_login(page)
    # test_order(page)
    # listening when selecting orders - execute event - intercept_response:
    page.route(
        "https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=*",
        intercept_Request,
    )
    page.get_by_role("button", name="ORDERS").click()
    time.sleep(3)

    page.get_by_role("button", name="View").first.click()
    message = page.locator(".blink_me").text_content()

    print(message)

    assert message == "You are not authorize to view this order"

    time.sleep(3)
