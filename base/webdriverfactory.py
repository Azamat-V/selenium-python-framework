"""
@package base

WebDriver Factory class implementation
It creates a webdriver instance based on browser configurations

Example:
    wdf = WebDriverFactory(browser)
    wdf.getWebDriverInstance()
"""

import traceback
from selenium import webdriver


class WebDriverFactory():


    def __init__(self, browser):
        """
        Inits WebDriveryFactory
        Returns:
            None
        :param browser:
        """
        self.browser = browser
        """
            Set chrome driver and iexplorer environment based on OS

            chromedriver = "C:/.../chromedriver.exe"
            os.environ["webdriver.chrome.driver"] = chromedriver
            self.driver = webdriver.Chrome(chromedriver)

            PREFERRED: Set the path on the machine where browser will be executed
        """

    def getWebDriverInstance(self):
        """
            Get WebDriver Instance based on the browser configuration

            Returns:
            'WebDriver Instance'
        """

        baseURL = "https://www.letskodeit.com/"
        if self.browser == "chrome":
            # Set chrome driver as above code if it's necessary
            driver = webdriver.Chrome()
        elif self.browser == "firefox":
            driver = webdriver.Firefox()
        else:
            driver = webdriver.Firefox()
        driver.implicitly_wait(3)
        driver.maximize_window()
        driver.get(baseURL)
        return driver
