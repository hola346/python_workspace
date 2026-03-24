from playwright.sync_api import Page, expect
import time


def test_newUser(page: Page):
    page.goto("https://rahulshettyacademy.com/client/#/auth/login")
    page.locator(".text-reset").click()

    page.get_by_placeholder("First Name").fill("Hola2")
    page.get_by_placeholder("Last Name").fill("Adios")
    page.get_by_placeholder("Email").fill("x2xx@ii.com")
    page.get_by_placeholder("enter your number").fill("6258665698")
    page.locator(".custom-select").select_option("Student")
    page.get_by_role("radio").nth(0).click()
    page.get_by_placeholder("Passsword").nth(0).fill("Aa/12345678")
    page.get_by_placeholder("Confirm Passsword").fill("Aa/12345678")
    page.get_by_role("checkbox").click()
    page.get_by_role("button").click()
    time.sleep(3)
    page.get_by_role("button").click()
    time.sleep(3)


def test_login(page: Page):
    page.goto("https://rahulshettyacademy.com/client/#/auth/login")
    page.get_by_placeholder("Email").fill("x2xx@ii.com")
    page.get_by_placeholder("enter your passsword").fill("Aa/12345678")
    page.get_by_role("button").click()
    expect(page).to_have_url("https://rahulshettyacademy.com/client/#/dashboard/dash")
    time.sleep(3)
