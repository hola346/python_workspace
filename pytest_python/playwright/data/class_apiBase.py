from playwright.async_api import Playwright

# import json
# import order.json
autho = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI2OWMyNjIxMGY4NmJhNTFhNjUyMjQwNDMiLCJ1c2VyRW1haWwiOiJ4Mnh4QGlpLmNvbSIsInVzZXJNb2JpbGUiOjYyNTg2NjU2OTgsInVzZXJSb2xlIjoiY3VzdG9tZXIiLCJpYXQiOjE3NzQzNDc2MTAsImV4cCI6MTgwNTkwNTIxMH0.v_jMvCSpJZe21AmDQi0gI5SJp-frCNXAtfvUlULPkrc"


class APIUtils:
    def getToken(self, playwright: Playwright):
        api_request_context = playwright.request.new_context(
            base_url="https://rahulshettyacademy.com"
        )
        response = api_request_context.post(
            "/api/ecom/auth/login",
            data={
                "userEmail": "adf7777777777@dwer.com",
                "userPassword": "Bb/dffg3412345678",
            },
            # headers={"Content_Type": "application/json"},
        )
        print(
            "THIS IS THE hardcored USER i'M USING: userEmail: adf7777777777@dwer.com, userPassword: Bb/dffg3412345678"
        )
        assert response.ok
        print(response.json())
        a = response.json()
        token = a["token"]
        print("This is the value of the token: ", token)
        return token

    def createOrder(self, playwright: Playwright):
        api_request_context = playwright.request.new_context(
            base_url="https://rahulshettyacademy.com"
        )
        # same thing as browser before, but this is API: define context, now define METHOD: get, post...
        response = api_request_context.post(
            "/api/ecom/order/create-order",
            data={
                "orders": [
                    {
                        "country": "Bulgaria",
                        "productOrderedId": "6960eac0c941646b7a8b3e68",
                    }
                ]
            },
            headers={
                "Authorization": self.getToken(playwright),
                "Content_Type": "application/json",
            },
        )

        print(response.json())
        return response.json()
