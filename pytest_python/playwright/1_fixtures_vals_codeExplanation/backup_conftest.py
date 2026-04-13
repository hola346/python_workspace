import pytest


@pytest.fixture(scope="session")  # can be module, session, function, class...
def preSetupWork():
    print("Setting up browser")


def pytest_collection_modifyitems(items):
    for item in items:
        item.add_marker(pytest.mark.fixtur)
