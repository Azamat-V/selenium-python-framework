import utilities.custom_logger_175 as cl
from pages.home.navigation_page import NavigationPage
from base.basepage import BasePage
import logging
import time
class LoginPage(BasePage):

    log = cl.customLogger((logging.DEBUG))

    def __init__(self, driver):
        # This statement calls the constructor (instance) of the superclass(SeleniumDriver)
        super().__init__(driver)
        # This is the internal constructor of the 'LoginPage' subclass.
        self.driver = driver
        self.nav = NavigationPage(driver)

    # Locators
    _loging_link = "(//a[@class='dynamic-link' and text()='Sign In'])"
    _email_field = "(//input[@type='email' and @placeholder='Email Address'])"
    _password_field = "(//input[@type='password'])"
    _login_button = "(//button[@id='login'])"
    _login_page = "Login"


    # clickLoginLink method invokes 'elementClick' method from the 'SeleniumDriver' superclass.
    def clickLoginLink(self):
        self.elementClick(self._loging_link, locatorType="xpath")

    # enterEmail method invokes 'sendKeys' method from the 'SeleniumDriver' superclass.
    def enterEmail(self, email):
        self.sendKeys(email, self._email_field)

    # enterPassword method invokes 'sendKeys' method from the 'SeleniumDriver' superclass.
    def enterPassword(self, password):
        self.sendKeys(password, self._password_field)

    # clickLoginButton method invokes 'elementClick' method from the 'SeleniumDriver' superclass.
    def clickLoginButton(self):
        self.elementClick(self._login_button, locatorType="xpath")

    def login(self, email="", password=""):
        self.clickLoginLink()
        # self.clearFields()
        # time.sleep(3)
        self.enterEmail(email)
        self.enterPassword(password)
        self.clickLoginButton()
        time.sleep(6)




    def verifyLoginSuccessful(self):
        result = self.isElementPresent("(//button[@id='dropdownMenu1'])",
                                       locatorType="xpath")
        return result

    def verifyLoginFailed(self):
        result = self.isElementPresent("(//span[contains(text(), 'Incorrect login details. Please try again.')])",
                                       locatorType="xpath")
        return result

    # def clearFields(self):
    #     emailField = self.getElement(locator=self._email_field, locatorType="xpath")
    #     emailField.clear()
    #     passwordField = self.getElement(locator=self._password_field, locatorType="xpath")
    #     passwordField.clear()

    def verifyTitle(self):
        return self.verifyPageTitle("My Courses")

    # def logout(self):
    #     self.nav.navigateToUserSettings()
    #     self.elementClick(locator="(//a[@href='/logout' and contains(text(), 'Logout')])",
    #                       locatorType="xpath")

    def logout(self):
        self.nav.navigateToUserSettings()
        logoutLinkElement = self.waitForElement(locator="(//a[@href='/logout' and contains(text(), 'Logout')])",
                                                locatorType="xpath", pollFrequency=1)
        self.elementClick(element=logoutLinkElement)






