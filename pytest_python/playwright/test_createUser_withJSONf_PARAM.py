from playwright.sync_api import Page, expect
import time, json, pytest

"THIS WORKS, DO NOT MODIFY"

"""PARAM - TWO IDEAS:
- Remove data logic out of TCs - reading external JSON files
- Loop test same code - TC using all def params from JSON - test login for 
    dif username - passwords.
"""

# Opening file:
with open("data/newUserData.json") as f:
    userData = json.load(f)
    user_data = userData["user_Data"]
    print(type(user_data))

with open("data/another_cred.json") as f2:
    credential = json.load(f2)
    cred = credential["UserCredentials"]


@pytest.mark.parametrize(
    "newUserData", user_data
)  # we'll use obj in next func of "class" user_data
def test_newUser(page: Page, newUserData):
    page.goto("https://rahulshettyacademy.com/client/#/auth/login")
    # As we use newUserData as in param, we'll create as many users as defined in newUserData.json(loop)
    page.locator(".text-reset").click()

    page.get_by_placeholder("First Name").fill(newUserData["fName"])
    page.get_by_placeholder("Last Name").fill(newUserData["lName"])
    page.get_by_placeholder("Email").fill(newUserData["email"])
    page.get_by_placeholder("enter your number").fill(newUserData["number"])
    page.locator(".custom-select").select_option(newUserData["occupation"])
    page.get_by_role("radio").nth(0).click()
    page.get_by_placeholder("Passsword").nth(0).fill(newUserData["password"])
    page.get_by_placeholder("Confirm Passsword").fill(newUserData["password"])
    page.get_by_role("checkbox").click()
    page.get_by_role("button").click()
    time.sleep(3)
    page.get_by_role("button").click()
    time.sleep(3)


@pytest.mark.parametrize(
    "user_credentials", cred
)  # we'll use obj in next func of "class" cred
def test_login(page: Page, user_credentials):  # this is a FIXTURE - conftest.py
    page.goto("https://rahulshettyacademy.com/client/#/auth/login")

    # Opening credential file: JSON file - you should import it
    # A dictionary {} object is created to save JSON structure and work with it
    page.get_by_placeholder("Email").press_sequentially(user_credentials["userEmail"])
    print(user_credentials["userEmail"])
    # Accessing by brackets [] -> now it's a list.
    # Could also save Dict UserInfo (both user,pass) into a LIST - list1=cred["userCred"][0]
    page.get_by_placeholder("enter your passsword").press_sequentially(
        user_credentials["userPassword"]
    )
    print(user_credentials["userPassword"])
    page.get_by_role("button").click()
    expect(page).to_have_url("https://rahulshettyacademy.com/client/#/dashboard/dash")
    time.sleep(3)


@pytest.mark.parametrize("user_credentials", cred)
def test_order(page: Page, user_credentials):
    test_login(
        page, user_credentials
    )  # We are doing an order for each user in cred.json
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
    page.locator(".fa-search").click()
    # page.keyboard.press("Enter")
    page.locator(".btnn").click()
    # page.locator(".btnn").click()
    # page.get_by_role("button").filter(has_text="Spain").click()
    # page.locator(".btn-custom").filter(has_text="ORDERS").click()
