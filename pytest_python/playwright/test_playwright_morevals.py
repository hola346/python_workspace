from playwright.sync_api import Page, expect
import time


def test_UIChecks(page: Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")

    page.get_by_placeholder("Type to Select Countries").fill("Spain")
    # used when predefined text is displayed, to be filled/inserted by user data
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_visible
    page.locator("#hide-textbox").click()
    expect(page.get_by_placeholder("Hide/Show Example")).not_to_be_visible
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_hidden
    page.locator("#show-textbox").click()
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_visible
    expect(page.get_by_placeholder("Hide/Show Example")).not_to_be_hidden

    time.sleep(5)


def test_AlertBoxes(
    page: Page,
):  # these are not supported since they are js popups, not HTML
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")

    page.on("dialog", lambda dialog: dialog.accept())
    # we are defining here a listener, if there is any event - click submit - triggering a dialog box, click - accept
    # accept is a pre-defined function, to call functions anonimously within a line, LAMBDA is used

    # page.locator("#confirmbtn").click()
    page.get_by_role("button", name="Confirm").click()

    time.sleep(5)


def test_frames(page: Page):
    # frames are diffs htmls embedded in one, so while you navigate on the second below, this 1st above remains
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    # now page.locators do not work, but frames instead:
    pageFrame = page.frame_locator(
        "#courses-iframe"
    )  # we identify the frame uniquely, so we have access to it
    pageFrame.get_by_role("link", name="All Access plan").click()
    expect(pageFrame.get_by_text("Happy Subscibers")).to_be_visible
    expect(pageFrame.locator("body")).to_contain_text("Happy Subscibers")
    time.sleep(5)


def test_HoverButtons(
    page: Page,
):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")

    page.locator("#mousehover").hover()
    time.sleep(5)
    page.get_by_role("link", name="Top").click()
    page.locator("#mousehover").hover()
    time.sleep(5)
    page.locator(".mouse-hover-content").filter(has_text="Reload").click()
    time.sleep(5)
