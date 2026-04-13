from playwright.async_api import Playwright
import json, pytest, time
from class_login import LoginPage
from class_apiBase_withJSONf_PARAM import APIUtils

"""AIM: FOR EVERY NEW WEBPAGE - URL, WE ARE CREATING A CLASS SPECIFIC FOR IT"""

with open(
    "C:\\python\\python_workspace\\pytest_python\\playwright\\6_TCs_with_classes_PageObject\\another_cred.json"
) as f:
    credentials = json.load(f)
    cred = credentials["UserCredentials"]
## files route can trigger errors sometimes, so you can use absolute path, or you can use relative path, but you have to be careful with the route, since it can change depending on where you are running the test, so it's better to use absolute path to avoid errors, but if you want to use relative path, you have to be careful with the route and make sure it's correct.


def arrangeOrderNum(response_order_OK):
    orderNum = str(response_order_OK["orders"])
    orderNum = orderNum.replace("'", "")
    orderNum = orderNum.replace("[", "")
    orderNum = orderNum.replace("]", "")
    print("printing order number????", orderNum)
    return orderNum


@pytest.mark.parametrize("user_credentials", cred)
def test_e2e_webapi(playwright: Playwright, browserInstance, user_credentials):
    print("This is the value in e2e_webapi of user_credentials: ", user_credentials)
    # You can define in your terminal which browser to use, by "pytest -test_XX --browser=chromium" or "pytest -test_XX --browser=firefox" or "pytest -test_XX --browser=webkit"
    # you can do that by defining in CONFTEST.PY a function (FIXTURE) with name "browser" and then use that function in your test script, but here we are defining browser in the test script itself, so we can use it directly without defining it in conftest.py
    """@@@@@@@@@@@1st GIVEN: login by API, create order and take note of the ORDER number"""
    api_Utils = APIUtils()
    response_order_OK = api_Utils.createOrder(playwright, user_credentials)
    print("This is the value in e2e_webapi of response_order_OK: ", response_order_OK)
    """@@@@@@@@@@@1st GIVEN: login by API, create order and take note of the ORDER number"""

    """@@@@@@@@@@@2nd GIVEN: take note of the ORDER number"""
    orderNum = arrangeOrderNum(
        response_order_OK
    )  ############################################## RESOLVE
    """@@@@@@@@@@@2nd GIVEN: take note of the ORDER number"""

    """@@@@@@@@@@@3rd GIVEN: user is on landing page"""
    # login - we log here using Login class, not method
    loginPageObj = LoginPage(browserInstance)  # page will be init in CLASS
    # we get now the "page" from fixture defined in conftest.py, and we pass it to the class, so we can use it in the methods of the class, and we can use it to navigate and do actions on the webpage, but we don't need to define it in the test script, since we are using it in the class, so we can define it in the class itself, and
    loginPageObj.navigate()
    """@@@@@@@@@@@3rd GIVEN: user is on landing page"""

    """@@@@@@@@@@@1st WHEN: Login to the application using UI with same <credentials>"""
    dashboardObj = loginPageObj.login(user_credentials)
    """@@@@@@@@@@@1st WHEN: Login to the application using UI with same <credentials>"""

    """@@@@@@@@@@@2nd WHEN: go to order history"""
    OrderList = dashboardObj.select_Orders()
    """@@@@@@@@@@@2nd WHEN: go to order history"""

    # page.locator("button", name="ORDERS").click()
    # page.locator(".fa-handshake-o").click()

    # row = page.locator("tr").filter(has_text=orderNum)
    """@@@@@@@@@@@3rd WHEN: select order details using previous ORDER number"""
    OrderDetailsObj = OrderList.viewOrder(orderNum)
    """@@@@@@@@@@@3rd WHEN: select order details using previous ORDER number"""

    """@@@@@@@@@@@THEN: Validate the order details - order message should be "Thank you for Shopping With Us"""
    OrderDetailsObj.test_order_details()
    """@@@@@@@@@@@THEN: Validate the order details - order message should be "Thank you for Shopping With Us"""

    time.sleep(5)

    # ----->expect(page.locator(".tagline")).to_have_text("Thank you for Shopping With Us")
    # expect(page.locator(".tagline")).to_contain_text("you for Shopping")

    time.sleep(5)
