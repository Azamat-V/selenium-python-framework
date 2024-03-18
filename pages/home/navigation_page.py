import utilities.custom_logger_175 as cl
from base.basepage import BasePage
import logging

class NavigationPage(BasePage):

    log = cl.customLogger((logging.DEBUG))

    def __init__(self, driver):
        # This statement calls the constructor (instance) of the superclass(SeleniumDriver)
        super().__init__(driver)
        # This is the internal constructor of the 'LoginPage' subclass.
        self.driver = driver

    # Locators
    _my_courses = "All courses"
    _user_settings_icon = "(//div[@class='dropdown']/button[@id='dropdownMenu1'])"



    def navigateToAllCourses(self):
        self.elementClick(locator=self._my_courses, locatorType="link")


    def navigateToUserSettings(self):
        userSettingsElement = self.waitForElement(locator=self._user_settings_icon,
                                                  locatorType="xpath", pollFrequency=1)
        self.elementClick(element=userSettingsElement)


