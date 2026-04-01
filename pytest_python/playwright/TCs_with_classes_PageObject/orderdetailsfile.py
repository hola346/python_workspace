from playwright.sync_api import expect


class OrderDetails:
    def __init__(self, page):
        self.page = page

    def test_order_details(self):
        expect(self.page.locator(".tagline")).to_have_text(
            "Thank you for Shopping With Us"
        )
        expect(self.page.locator(".tagline")).to_contain_text("you for Shopping")
