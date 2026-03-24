# Fixtures
import pytest


@pytest.fixture(scope="module")
def preWork():
    print("This is prework instance module")
    return "pass"


@pytest.fixture(scope="function")
def secondWork():
    print("This is second instance function")
    yield  # pause, won't execute further within secondwork. It will run at the end of TCs exec
    print("tear down validation")


@pytest.mark.smoke
def test_initialCheck(preWork, secondWork):
    print("this is first test")
    assert preWork == "pass"


@pytest.mark.skip  ## will skip next one
def test_secondCheck(preWork, secondWork):
    print("this is second test")
