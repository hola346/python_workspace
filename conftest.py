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
def browserInstance(playwright, request):
    """Browser fixture for BDD tests"""
    browser_name = request.config.getoption("--browser_name")
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
    yield page
    context.close()
    browser.close()


def pytest_collection_modifyitems(items):
    """Auto-mark tests based on their folder"""
    for item in items:
        fspath = str(item.fspath)
        if "1_fixtures_vals_codeExplanation" in fspath:
            item.add_marker(pytest.mark.fixtur)
        elif "2_MockData" in fspath:
            item.add_marker(pytest.mark.mockdata)
        elif "3_StandAlone_tests" in fspath:
            item.add_marker(pytest.mark.standalone)
        elif "4_webapi_with_JSON_and_APIClass" in fspath:
            item.add_marker(pytest.mark.webapi)
        elif "5_webapi_with_JSON_APIClass_and_PARAMS" in fspath:
            item.add_marker(pytest.mark.webapi_params)
        elif "6_TCs_with_classes_PageObject" in fspath:
            item.add_marker(pytest.mark.pageobject)
        elif "7_BDD_Cucumber_Features" in fspath:
            item.add_marker(pytest.mark.bdd)
        elif "8_iPhoneX_test" in fspath:
            item.add_marker(pytest.mark.iphonex)
        elif "9_BDD_iPhoneX" in fspath:
            item.add_marker(pytest.mark.bdd_iphonex)
