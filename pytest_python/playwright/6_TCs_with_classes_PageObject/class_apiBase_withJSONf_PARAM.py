from playwright.async_api import Playwright
import json

"""THIS WORKS OK, LAST RESPONSE HEADERS CAN'T BE TAKEN FROM JSON SINCE WE PROCESS TOKEN"""

"""with open("data/another_cred.json") as f3:
    cred = json.load(f3)
    cred1 = cred["UserCredentials"]


@pytest.mark.parametrize("user_credentials", cred1)"""


class APIUtils:
    def getToken(self, playwright: Playwright, user_credentials):
        api_request_context = playwright.request.new_context(
            base_url="https://rahulshettyacademy.com"
        )

        response = api_request_context.post(
            "/api/ecom/auth/login",
            data=user_credentials,
            # headers={"Content_Type": "application/json"},
        )
        # assert response.ok
        a = response.json()
        print("This is value of response.json: ", a)
        token = a["token"]
        print("This is the value of the token: ", token)
        return token

    def createOrder(self, playwright: Playwright, user_credentials):
        api_request_context = playwright.request.new_context(
            base_url="https://rahulshettyacademy.com"
        )
        # same thing as browser before, but this is API: define context, now define METHOD: get, post...

        with open(
            "C:\\python\\python_workspace\\pytest_python\\playwright\\6_TCs_with_classes_PageObject\\order.json"
        ) as f3:
            orders = json.load(f3)

        response = api_request_context.post(
            "/api/ecom/order/create-order",
            data=orders,
            headers={
                "Authorization": self.getToken(playwright, user_credentials),
                "Content_Type": "application/json",
            },
        )
        return response.json()
