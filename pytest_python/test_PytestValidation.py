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
    # now it will finish the first test, then it will execute the code after yield in secondWork, and then it will execute the second test, and then it will execute the code after yield in secondWork again, since secondWork is function scope, so it will execute for each test function that uses it. If it was module scope, it would execute only once after all tests in the module are done.


@pytest.mark.skip  ## will skip next one
def test_secondCheck(preWork, secondWork):
    print("this is second test")
