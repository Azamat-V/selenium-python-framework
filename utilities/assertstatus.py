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
        self.resultList = [] # By default, result list is empty

    def setResult(self, result, resultMessage):
        try:
            if result is not None:
                if result: # If result is True
                    self.resultList.append("PASS")
                    self.log.info("### VERIFICATION SUCCESSFUL :: + " + resultMessage)
                else: # If result is False
                    self.resultList.append("FAIL")
                    self.log.error("### VERIFICATION FAILED :: + " + resultMessage)
                    self.screenshot(resultMessage)
            else: # If result is None
                self.resultList.append("FAIL")
                self.log.error("### VERIFICATION FAILED :: + " + resultMessage)
                self.log.info(resultMessage)
                self.screenshot(resultMessage)
        except:
            self.resultList.append("FAIL")
            self.log.error("### Exeption Occured :: + " + resultMessage)
            self.log.info(resultMessage)
            self.screenshot(resultMessage)
            print_stack()

    # AssertStatus.mark.pass or fail(This method applies to the testcase)
    def mark(self, result, resultMessage):
        """
        Mark the result of the verification point in a test case
        """
        self.setResult(result, resultMessage)

    # AssertStatus.markFinal.pass or fail(This method applies to the end of the testcase)
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
