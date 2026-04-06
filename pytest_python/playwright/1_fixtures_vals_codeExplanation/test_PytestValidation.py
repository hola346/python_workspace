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


@pytest.mark.fixtur
def test_initialCheck(preWork, secondWork):
    print("this is first test")
    assert preWork == "pass"
    # now it will finish the first test, then it will execute the code after yield in secondWork, and then it will execute the second test, and then it will execute the code after yield in secondWork again, since secondWork is function scope, so it will execute for each test function that uses it. If it was module scope, it would execute only once after all tests in the module are done.


## mark.prueba: you can define your own markers, and then you can use them to run specific tests, like "pytest -m prueba" will run only the tests that are marked with @pytest.mark.prueba, and you can also combine markers, like "pytest -m 'prueba and not secondCheck'" will run only the tests that are marked with @pytest.mark.prueba and not marked with @pytest.mark.skip, so it will run only the first test and skip the second test.
## with custom marks, warning may be shown, to avoid it, you can define your custom marks in pytest.ini file, like this:
# [pytest]
# markers = prueba: mark test as part of prueba group
#           otherMark: mark test as part of otherMark group

"""
You can also run TCs by name / keywords, like "pytest -k 'initialCheck' will run only the test that contains 'initialCheck' in its name, so it will run only the first test and skip the second test, but if you run "pytest -k 'Check'" it will run both tests, since both tests contain 'Check' in their name.
don't forget also other terminal tags, like -m for marks, -k for keywords, -s to show print statements, -v for verbose, etc.
as long as other hard-coded commands: --headed, --ignore, --continue-on-collection-errors, --collect-only, --disable-warnings, --ff to run failed tests first, etc.
"""

"""
Run TCs in parallel: need to install pytest-xdist plugin, by typing "pip install pytest-xdist" and then you can run "pytest -n 2" to run tests in parallel with 2 workers, so it will run 2 tests at the same time, and if you have more tests, it will run them in batches of 2, but if you have less tests than workers, it will run them all at the same time, so it's better to use the number of workers equal to the number of tests, or less than the number of tests, but not more than the number of tests, otherwise it will run all tests at the same time and it may cause issues with resources, like database connections, etc.
"""

"""you may consider also to create a virtual environment for your project, to avoid conflicts with other projects, and to keep your dependencies organized, you can create a virtual environment by typing "python -m venv env" and then you can activate it by typing "env\Scripts\activate" on Windows or "source env/bin/activate" on Linux/Mac, and then you can install your dependencies in the virtual environment, and they will be isolated from other projects, so you can have different versions of the same package in different projects without conflicts.
how to create venv when you already started the project: you can create a venv in the root directory of your project, and then you can activate it, and then you can install your dependencies in the venv, and then you can use the venv to run your tests, and it will use the dependencies from the venv, so you can have different versions of the same package in different projects without conflicts.
py -m venv venv\ - this will create a venv in the current directory with the name "venv", you can choose any name you want for the venv, but it's common to use "venv" or "env" as the name of the virtual environment.
"""

"""
Another interesting plugin: pytest-html - to generate HTML reports for your tests, you can install it by typing "pip install pytest-html" and then you can run "pytest --html=report.html" to generate an HTML report for your tests, and you can open the report in your browser to see the results of your tests in a more visual way, with details about each test, like the name, the status, the duration, etc.
"""

"""
Finally another one: --trace - to show the stack trace for failed tests, you can run "pytest --trace" to show the stack trace for failed tests, and it will help you to debug your tests by showing you where the error occurred in your code, and you can also use it with other terminal options, like "pytest -k 'initialCheck' --trace" to show the stack trace for failed tests that contain 'initialCheck' in their name.
It has following options: 
--trace: on 
--trace: off
--trace: retain-on-failure: to show the stack trace only for failed tests, and it will not show the stack trace for passed tests, so it's better to use this option to avoid cluttering your console with stack traces for passed tests, and it will help you to focus on the failed tests and debug them more efficiently.
you can see results on trace.playwright.dev, where you can see the stack trace and the code that caused the error, and you can also see the variables and the state of the application at the time of the error, which can help you to understand why the test failed and how to fix it.
pytest --browser_name chromium -m prueba -n 5 --tracing on --html=report.html -s -v
--- You go to trace.playwright.dev, upload zip file for one test, and see results. 
"""


@pytest.mark.skip  ## will skip next one
def test_secondCheck(preWork, secondWork):
    print("this is second test")
