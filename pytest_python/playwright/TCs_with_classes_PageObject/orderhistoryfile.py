from orderdetailsfile import OrderDetails


class OrderHistory:
    def __init__(self, page):
        self.page = page

    def viewOrder(self, orderNum):
        row = self.page.locator("tr").filter(has_text=orderNum)
        row.get_by_role("button", name="View").click()
        OrderDetailsPage = OrderDetails(self.page)
        return OrderDetailsPage
