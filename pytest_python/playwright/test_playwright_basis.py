##################
from playwright.sync_api import Page, Playwright, expect
import time

"""THIS WAS VERIFIED TO BE WORKING FINE, DO NOT MODIFY"""

"""///
from playwright.sync_api import sync_playwright, Playwright
def run(playwright: Playwright):
    chromium = playwright.chromium # or "firefox" or "webkit".
    browser = chromium.launch(headless=True)
    page = browser.new_page()


with sync_playwright() as playwright:
    run(playwright)
///"""
################## OPENING BROWSER


def test_playwrightBasics(
    playwright,
):  # playwright fixture can be globally used as it is within pytest_PW package
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()  # like incognito mode
    page = context.new_page()
    page.goto("http:\\www.google.com")


# chromium, headless, by default context - page
def test_playwrightShortcut(page: Page):
    page.goto("http:\\www.google.com")


# Run headed instead of headless - default: "pytest test_playwright_basis.py::test_playwrightShortcut --headed"


def test_coreLocators(page: Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")

    page.get_by_label("Password:").fill("Learning@830$3mK2")
    page.locator("#usertype").nth(
        0
    ).click()  ########################################################

    page.get_by_role("combobox").select_option("teach")  # value defined in the HTML
    # label.customradio:nth-child(2)

    page.get_by_role(role="link", name="terms and conditions").click()
    page.get_by_role(role="checkbox", name="terms").click()
    page.locator("#terms").click()
    page.locator("#terms").click()
    page.get_by_role(role="button", name="Sign In").click()
    # You can use CSS selectors, as in Cypress: # for IDs, . for classes
    """ """
    time.sleep(5)


def test_coreLocatorsIncorrectLogin(page: Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy1")
    page.get_by_label("Password:").fill("Learning@830$3mK21")
    # Using Incorrect name/password
    # You can use CSS selectors, as in Cypress: # for IDs, . for classes

    page.get_by_role("combobox").select_option("teach")  # value defined in the HTML
    # label.customradio:nth-child(2)

    page.get_by_role(role="link", name="terms and conditions").click()
    page.locator("#terms").click()

    page.get_by_role(role="button", name="Sign In").click()

    expect(page.locator(".alert")).to_contain_text("Incorrect")
    expect(page.locator(".alert")).to_have_text("Incorrect username/password.")
    ###### Another way of doing it:
    expect(page.get_by_text("Incorrect username/password.")).to_be_visible()
    ## AUTO-WAIT feature, not necessary to wait for the message to be loaded
    """ """
    time.sleep(5)


def test_FFLocators(playwright: Playwright):
    ffbrowser = playwright.firefox.launch(headless=False)
    # like incognito mode
    page = ffbrowser.new_page()
    page.goto("http:\\www.google.com")
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")

    page.get_by_label("Password:").fill("Learning@830$3mK2")
    # page.get_by_role(role="radio", name="user").click()

    page.get_by_role("combobox").select_option("teach")  # value defined in the HTML
    # label.customradio:nth-child(2)

    page.get_by_role(role="link", name="terms and conditions").click()
    page.get_by_role(role="checkbox", name="terms").click()
    page.locator("#terms").click()
    page.locator("#terms").click()
    page.get_by_role(role="button", name="Sign In").click()
    # You can use CSS selectors, as in Cypress: # for IDs, . for classes
    """ """
    time.sleep(5)
