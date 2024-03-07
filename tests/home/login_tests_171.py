from pages.home.login_page_171 import LoginPage
from utilities.assertstatus import AssertStatus
from pages.home.navigation_page import NavigationPage
import unittest
import pytest


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class LoginTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)
        self.ts = AssertStatus(self.driver)
        self.nav = NavigationPage(self.driver)



    @pytest.mark.run(order=2)
    def test_validLogin(self):
        self.lp.login("test@email.com", "abcabc")
        result1 = self.lp.verifyTitle()
        self.ts.mark(result1, "Title_verification")
        result2 = self.lp.verifyLoginSuccessful()
        self.ts.markFinal("test_validLogin", result2, "Login_verification")

    @pytest.mark.run(order=1)
    def test_invalidLogin(self):
        self.lp.logout()
        self.lp.login("test@email.com", "abcabcgjfj")
        result = self.lp.verifyLoginFailed()
        assert result == True

