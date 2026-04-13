import pytest

# this conftest.py is being used by test_e2e_webapi_API_PARAMS.py, but not by test_e2e_webapi_PageObject.py, since it is in a different folder. We can have multiple conftest.py files in different folders, and they will be used by the tests in those folders and subfolders.


@pytest.fixture(scope="session")
def user_credentials(request):
    return request.param


@pytest.fixture(scope="session")
def newUserData(request):
    return request.param
