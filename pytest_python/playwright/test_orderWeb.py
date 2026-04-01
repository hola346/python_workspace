from playwright.sync_api import Page
import time
from test_createUser_withJSONf import test_order

"""THIS WORKS BUT EXECUTES 2 TIMES, NOT SURE WHY"""


def test_orderWeb(page: Page):
    # test_login(page) # we are using user [2] from credentials.json - 77777
    test_order(page)

    # print(order)

    time.sleep(5)
