import pytest


@pytest.fixture(scope="session")  # can be module, session, function, class...
def preSetupWork():
    print("Setting up browser")
