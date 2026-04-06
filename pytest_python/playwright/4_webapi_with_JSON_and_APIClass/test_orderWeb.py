from playwright.sync_api import Page
import time

import os
import sys

import pytest

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../3_StandAlone_tests")

from test_createUser_withJSONf import test_order

"""THIS WORKS BUT EXECUTES 2 TIMES, NOT SURE WHY"""


@pytest.mark.webapi4
def test_orderWeb(page: Page):
    # test_login(page) # we are using user [2] from credentials.json - 77777
    test_order(page)

    # print(order)

    time.sleep(5)
