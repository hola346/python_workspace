from playwright.sync_api import Playwright, sync_playwright


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://rahulshettyacademy.com/client/#/auth/login")
    page.get_by_role("textbox", name="email@example.com").click()
    page.get_by_role("textbox", name="email@example.com").fill("rahu")
    page.get_by_role("textbox", name="email@example.com").click()
    page.get_by_role("textbox", name="email@example.com").fill("rahulshetty@gmail.com")
    page.get_by_role("textbox", name="enter your passsword").click()
    page.get_by_role("textbox", name="enter your passsword").click()
    page.get_by_role("textbox", name="enter your passsword").fill("123456")
    page.get_by_role("button", name="Login").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
