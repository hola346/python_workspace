from playwright.sync_api import Page, expect
import time, pytest

"""THIS WAS VERIFIED TO BE WORKING FINE, DO NOT MODIFY"""


def test_ricePrice(page: Page):
    page.goto("https://rahulshettyacademy.com/seleniumPractise/#/offers")
    # now page.locators do not work, but frames instead:

    print(page.locator("th").count())  # --> 3
    for index in range(page.locator("th").count()):
        # index is 0 at the beginning, will do for total number of columns -th - (3-1), 0 to 2, 3 times
        print(
            "Number of Price found: ",
            page.locator("th").nth(index).filter(has_text="Price").count(),
        )
        if page.locator("th").nth(index).filter(has_text="Price").count() > 0:
            # count number of times column has text PRICE, if this count > 0 then we found Price column, no need to check further
            colvalue = index
            print("Index of Price column: ", colvalue)
            break

    # expect(page.locator('.my-table-row').nth(colvalue)).to_contain_text('37');

    """ We do this since it's a dinamic table, PRICE column should not be always the 2nd displayed, but cound be in a diff position"""

    row = page.locator("tr").filter(
        has_text="Rice"
    )  # you don't pick here index of the row, but the FULL ROW.
    expect(row.locator("td").nth(colvalue)).to_have_text("37")
    # print(Row.nth())

    time.sleep(5)
