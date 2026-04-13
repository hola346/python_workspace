class ShopPage:
    def __init__(self, page):
        self.page = page
        # Locators
        self.product_cards = ".card"
        # Using text locator with case-insensitive match
        self.iphone_x_title = "text=iphone X"

    def is_iphone_x_present(self):
        """Check if iPhone X product is present on the page"""
        # Wait for the product cards to be visible
        self.page.locator(self.product_cards).first.wait_for(state="visible")
        return self.page.locator(self.iphone_x_title).count() > 0

    def get_iphone_x_card(self):
        """Get the iPhone X product card element"""
        return self.page.locator(self.iphone_x_title)
