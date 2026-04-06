# Fixtures


import pytest


@pytest.mark.fixtur
def test_ThirdCheck(preSetupWork):
    print("this is 3rd test")


@pytest.mark.fixtur
def test_fourthCheck(preSetupWork):
    print("this is 4th test")
