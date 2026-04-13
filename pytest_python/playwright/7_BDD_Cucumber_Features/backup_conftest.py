import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name",
        action="store",
        default="chromium",
        help="Browser to run tests",
    )
    parser.addoption(
        "--env",
        action="store",
        default="https://rahulshettyacademy.com/client",
        help="Environment to run tests",
    )


@pytest.fixture(scope="function")
# with (scope="session") only runs 1st time, but we need to run it for each test, so we will use function scope, but here we are using session scope, so it will run only once, and then it will be used for all tests in the session, but if we use function scope, it will run for each test function that uses it.
# before after 1st user testing, it went directly to main page - skipping login.
def browserInstance(playwright, request):
    browser_name = request.config.getoption("--browser_name")
    # with this you can access to global variables defined in terminal, like --browser, and then you can use that variable to define which browser to use in your tests, but here we are defining browser in the test script itself, so we can use it directly without defining it in conftest.py
    if browser_name == "chromium":
        browser = playwright.chromium.launch(headless=False)
    elif browser_name == "firefox":
        browser = playwright.firefox.launch(headless=False)
    elif browser_name == "webkit":
        browser = playwright.webkit.launch(headless=False)

    env = request.config.getoption("--env")
    if env == "dev":
        url = "https://rahulshettyacademy_dev.com/client"
    elif env == "qa":
        url = "https://rahulshettyacademy_qa.com/client"

    context = browser.new_context()
    page = context.new_page()
    ## Once page is defined, you could also insert here the code to navigate to the URL, so you don't need to do it in each test script, but here we are doing it in the test script itself, so we can use it directly without defining it in conftest.py
    # BUT, you could also define a terminal param as done by browser, selecting desired URL - env to navigate
    yield page
    # Remember: yield pauses the function, so after the test is done, it will execute the code after yield. Return instead closes function
    context.close()
    browser.close()
    # this will run at the end, after running TCs.
