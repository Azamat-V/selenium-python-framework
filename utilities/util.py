"""
@package utilities

Util class implementation
All most commonly used utilities should be implemented in this class

Example:
    name = self.util.getUniqueName()
"""
import time
import traceback
import random, string
import utilities.custom_logger_175 as cl
import logging
class Util(object):

    log = cl.customLogger(logging.INFO)

    def sleep(self, sec, info=""):
        """
        Put the program to wait for the specified amount of time
        """
        if info is not None:
            self.log.info("Wait :: '" + str(sec) + "' seconds for " + info)
        try:
            time.sleep()
        except InterruptedError:
            traceback.print_stack()

    def getAlphaNumeric(self, lenghth, type="letters"):
        """
        Get random string of characters

        Parameters:
            length: Length of string, number of characters string should have
            type: Type of characters string should have. Default is letters
            Provide lower/upper/digits for different types

        """
        alpha_num = ""
        if type == "lower":
            case = string.ascii_lowercase
        elif type == "upper":
            case = string.ascii_uppercase
        elif type == "digits":
            case = string.digits
        elif type == "mix":
            case = string.ascii_letters + string.digits
        else:
            case = string.ascii_letters
        return alpha_num.join(random.choice(case) for i in range(lenghth))

    def getUniqueName(self, charCount=10):
        """
        Get a unique name
        """
        return self.getAlphaNumeric(charCount, "lower")

    def getUniqueNameList(self, listSize=5, itemLength=None):
        """
        Parameters:
            listSize: Number of names. Default is 5 names in a list
            itemLength: It should be a list containing number of items equal to the listSize
                        This determines the length of the each item in the list -> [1, 2, 3, 4, 5]

        """

        nameList = ""
        for i in range(0, listSize):
            nameList.append(self.getUniqueName(itemLength))
            return nameList

    def verifyTextContains(self, expectedText, actualText):
        """
        Verify actual text contains expected text string
        :param actualText:
        :param expectedText:
        :return:
        """
        self.log.info("Actual Text From Application Web UI --> :: " + actualText)
        self.log.info("Expected Text From Application Web UI --> :: " + expectedText)
        if expectedText.lower() in actualText.lower():
            self.log.info("### Verification contains !!!")
            return True
        else:
            self.log.info()
            return False

    def verifyTextMatch(self, actualText, expectedText):
        """
        Verify text match
        :param actualText:
        :param expectedText:
        :return:
        """
        self.log.info("Actual Text From Application Web UI --> :: " + actualText)
        self.log.info("Expected Text From Application Web UI --> :: " + expectedText)
        if actualText.lower() == expectedText.lower():
            self.log.info("### Verification matches")
            return True
        else:
            self.log.info("### Verification doesn't match")
            return False

    def verifyListMatch(self, expectedList, actualList):
        """
        Verify two lists matches
        :param expectedList:
        :param actualList:
        :return:
        """
        return set(expectedList) == set(actualList)

    def verifyListContains(self, expectedList, actualList):
        """
        Verify actual list contains elements of expected list
        :param expectedList:
        :param actualList:
        :return:
        """
        length = len(expectedList)
        for i in range(0, length):
            if expectedList[i] not in actualList:
                return False
        else:
            return True




