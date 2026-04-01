from playwright.sync_api import Page, expect
import time, json

"""THIS WORKS STANDALONE, CAREFUL MODIFYING"""


def test_newUser(page: Page):
    page.goto("https://rahulshettyacademy.com/client/#/auth/login")
    page.locator(".text-reset").click()

    # Opening file:
    with open("data/simple_userData.json") as f:
        userData = json.load(f)

    page.get_by_placeholder("First Name").fill(userData["fName"])
    page.get_by_placeholder("Last Name").fill(userData["lName"])
    page.get_by_placeholder("Email").fill(userData["email"])
    page.get_by_placeholder("enter your number").fill(userData["number"])
    page.locator(".custom-select").select_option(userData["occupation"])
    page.get_by_role("radio").nth(0).click()
    page.get_by_placeholder("Passsword").nth(0).fill(userData["password"])
    page.get_by_placeholder("Confirm Passsword").fill(userData["password"])
    page.get_by_role("checkbox").click()
    page.get_by_role("button").click()
    time.sleep(3)
    page.get_by_role("button").click()
    time.sleep(3)


def test_login(page: Page):
    page.goto("https://rahulshettyacademy.com/client/#/auth/login")

    # Opening credential file: JSON file - you should import it
    with open("data/credentials.json") as f2:
        cred = json.load(f2)
    # A dictionary {} object is created to save JSON structure and work with it
    page.get_by_placeholder("Email").press_sequentially(
        cred["UserCredentials"][2]["emailUsername"]
    )
    print(
        "NOTICE: we are printing user [2],", cred["UserCredentials"][2]["emailUsername"]
    )
    # Accessing by brackets [] -> now it's a list.
    # Could also save Dict UserInfo (both user,pass) into a LIST - list1=cred["userCred"][0]
    page.get_by_placeholder("enter your passsword").press_sequentially(
        cred["UserCredentials"][2]["password"]
    )
    page.get_by_role("button").click()
    expect(page).to_have_url("https://rahulshettyacademy.com/client/#/dashboard/dash")
    time.sleep(6)


def test_order(page: Page):
    test_login(page)
    expect(page.get_by_text("ADIDAS ORIGINAL")).to_be_visible()
    expect(page.get_by_text("ZARA COAT 3")).to_be_visible()
    expect(page.get_by_text("iphone 13 pro")).to_be_visible()

    product = page.locator(".card").filter(has_text="ADIDAS ORIGINAL")
    product.get_by_role("button", name="View").click()
    expect(page.get_by_text("product details")).to_be_visible()
    page.locator(".continue").click()

    product.get_by_role("button", name="Add to Cart").click()

    page.locator(".btn-custom").filter(has_text="Cart").click()
    # page.get_by_role("button", name="Cart").click()
    page.get_by_role("button", name="Buy").click()

    page.get_by_placeholder("Select Country").press_sequentially("Germany")
    # page.get_by_placeholder("Select Country").press("Enter")
    print("IS SEQUENTIALLY WORKIN??")
    page.locator(".fa-search").click()
    # page.keyboard.press("Enter")
    page.locator(".btnn").click()
    # page.locator(".btnn").click()
    # page.get_by_role("button").filter(has_text="Spain").click()
    # page.locator(".btn-custom").filter(has_text="ORDERS").click()
    print("this is the end of the ORDERRRRRRR")
    time.sleep(6)
