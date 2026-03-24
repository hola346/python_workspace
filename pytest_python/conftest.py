import pytest


@pytest.fixture(scope="session")  # can be module, session, class...
def preSetupWork():
    print("Setting up browser")
