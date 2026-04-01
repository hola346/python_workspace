from orderhistoryfile import OrderHistory


class Dashboard:
    def __init__(self, page):
        self.page = page
        # creating local page def according to in param

    def select_Orders(self):
        self.page.get_by_role("button", name="ORDERS").click()
        OrderList = OrderHistory(self.page)
        return OrderList
