"""
@package utilities

CheckPoint class implementation
It provides functionality to assert the result

Example:
    self.check_point.markFinal("Test Name", result, "Message")
"""

import utilities.custom_logger_175 as cl
import logging
from base.selenium_driver_173 import SeleniumDriver
from traceback import print_stack


class AssertStatus(SeleniumDriver):
    log = cl.customLogger(logging.INFO)

    def __init__(self, driver):
        """
        Inits CheckPoint class
        """
        super(AssertStatus, self).__init__(driver)
        self.resultList = []

    def setResult(self, result, resultMessage):
        try:
            if result is not None:
                if result:
                    self.resultList.append("PASS")
                    self.log.info("### VERIFICATION SUCCESSFUL :: + " + resultMessage)
                else:
                    self.resultList.append("FAIL")
                    self.log.error("### VERIFICATION FAILED :: + " + resultMessage)
                    self.screenshot(resultMessage)
            else:
                self.resultList.append("FAIL")
                self.log.error("### VERIFICATION FAILED :: + " + resultMessage)
                self.log.info(resultMessage)
        except:
            self.resultList.append("FAIL")
            self.log.error("### Exeption Occured :: + " + resultMessage)
            self.log.info(resultMessage)
            print_stack()


    def mark(self, result, resultMessage):
        """
        Mark the result of the verification point in a test case
        """
        self.setResult(result, resultMessage)

    def markFinal(self, testName, result, resultMessage):
        """
        Mark the final result of the verification point in a test case
        This needs to be called at least once in a test case
        This should be final test status of the test case
        """
        self.setResult(result, resultMessage)

        if "FAIL" in self.resultList:
            self.log.error(testName + "### TEST IS FAILED")
            self.resultList.clear()
            assert True == False
        else:
            self.log.info(testName + "### TEST IS SUCCESSFUL")
            self.resultList.clear()
            assert True == True
