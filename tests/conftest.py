"""
Conftest is a configuration file for tests it applies to all tests you want to apply
"""

import pytest
from base.webdriverfactory import WebDriverFactory
from pages.home.login_page_171 import LoginPage

@pytest.fixture()
# Fixture without attributes applies to method
def setUp():
    print("Preconditions method(test)")
    yield
    print("Postconditions method(test)")


@pytest.fixture(scope="class")
# Fixture with attributes applies to the attributes like scope="class" or "module"
def oneTimeSetUp(request, browser):
    print("Preconditions(Class or Module)")
    wdf = WebDriverFactory(browser)
    driver = wdf.getWebDriverInstance()
    lp = LoginPage(driver)
    lp.login("test@email.com", "abcabc")


    if request.cls is not None:
        request.cls.driver = driver

    yield driver
    driver.quit()
    print("Postconditions(Class or module)")
    driver.quit()


def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--osType", help="Type of operating system")

# This methods get options to execute command etg. --browser, --osType
@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")
@pytest.fixture(scope="session")
def osType(request):
    return request.config.getoption("--osType")

# This command launches tests in terminal or command line
# py.test -v -s test_class_demo1_162.py --browser firefox --osType Windows
# py.test -v -s pytestpackage\test_class_demo1_162.py --browser firefox --osType Windows
