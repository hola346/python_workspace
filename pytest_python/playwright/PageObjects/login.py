class LoginPage:
    def __init__(self, page):
        self.page = page
        # creating local page def according to in param

    def navigate(self):
        self.page.goto("https://rahulshettyacademy.com/client")

    def login(self, user_credentials):
        self.page.get_by_placeholder("Email").fill(user_credentials["userEmail"])
        self.page.get_by_placeholder("enter your passsword").fill(
            user_credentials["userPassword"]
        )
        self.page.get_by_role("button").click()
