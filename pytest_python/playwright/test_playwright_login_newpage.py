##################
from playwright.sync_api import Page, expect
import time
import re

"""THIS WAS VERIFIED TO BE WORKING FINE, DO NOT MODIFY"""


def test_coreLocators(page: Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("Learning@830$3mK2")

    page.get_by_role("combobox").select_option("teach")  # value defined in the HTML
    # label.customradio:nth-child(2)
    page.locator("#terms").click()
    page.get_by_role(role="button", name="Sign In").click()
    # You can use CSS selectors, as in Cypress: # for IDs, . for classes
    """ LOGIN OK """
    page.wait_for_url("**/angularpractice/shop")
    # expect(page.url()).to_contain_text("/angularpractice/shop")
    expect(page.get_by_text("iphone X")).to_be_visible()
    expect(page.get_by_text("Samsung Note 8")).to_be_visible()
    expect(page.get_by_text("Nokia Edge")).to_be_visible()
    expect(page.get_by_text("Blackberry")).to_be_visible()
    expect(page.get_by_text("Checkout")).to_be_visible()

    page.locator(
        "app-card.col-lg-3:nth-child(1) > div:nth-child(1) > div:nth-child(3) > button:nth-child(1)"
    ).click()
    page.locator(
        "app-card.col-lg-3:nth-child(2) > div:nth-child(1) > div:nth-child(3) > button:nth-child(1)"
    ).click()
    expect(page.get_by_text("Checkout ( 2 )")).to_be_visible()

    #### Another method: instead of selecting direct locator, filter by product tag first:
    Blackberryproduct = page.locator("app-card").filter(has_text="Blackberry")
    Blackberryproduct.locator(".btn").click()
    # or by role = button
    expect(page.get_by_text("Checkout ( 3 )")).to_be_visible()

    # now clicking cart, we should see 3 elements:

    page.locator(".btn").filter(has_text="Checkout").click()
    ##### could be also page.get_by_text  checkout
    expect(page.get_by_text("Quantity")).to_be_visible()
    expect(page.get_by_text("Price")).to_be_visible()
    expect(page.locator(".media")).to_have_count(
        3
    )  # checking there are 3 elements in cart

    time.sleep(5)


def test_childpage(page: Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")

    with page.expect_popup() as new_page:
        page.locator(".blinkingText").filter(has_text="Resume").click()
        new_page.value.wait_for_url("**/documents-request")
        expect(new_page.value.locator(".red")).to_have_text(
            "Please email us at mentor@rahulshettyacademy.com with below template to receive response "
        )
        expect(new_page.value.locator(".red")).to_be_visible()
        # printing in output content of the red text:
        text = new_page.value.locator(".red").text_content()
        print(text)
        # extract emails with reg Exp
        emails = re.findall("([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)", text)
        print(emails)

        # extract emails considering "at" keyword
        text2 = text.split("at ")  # will split text in dif list elems when at found
        print(text2)

        text3 = text2[1].split(".com")
        text4 = text3[0] + ".com"
        print(text4)
        assert text4 == "mentor@rahulshettyacademy.com"
        time.sleep(5)


# html body app-root app-shop div.container div.row div.col-lg-9 app-card-list.row app-card.col-lg-3.col-md-6.mb-3 div.card.h-100 div.card-footer button.btn.btn-info
