from shop_page import ShopPage


class LoginPage:
    def __init__(self, page):
        self.page = page
        # Locators
        self.username_field = "#username"
        self.password_field = "#password"
        self.terms_checkbox = "#terms"
        self.signin_button = "#signInBtn"

    def navigate(self):
        self.page.goto("https://rahulshettyacademy.com/loginpagePractise/")

    def login(self, username, password):
        self.page.fill(self.username_field, username)
        self.page.fill(self.password_field, password)
        self.page.check(self.terms_checkbox)
        self.page.click(self.signin_button)
        # Wait for navigation to shop page
        self.page.wait_for_url("**/angularpractice/shop")
        self.page.wait_for_load_state("networkidle")
        shop_page = ShopPage(self.page)
        return shop_page
