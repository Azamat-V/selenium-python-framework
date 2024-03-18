import utilities.custom_logger_175 as cl
import logging
from base.basepage import BasePage
import time

class RegisterCoursesPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    _search_box = "(//input[@id='search' and @placeholder='Search Course'])"
    _search_button = "(//button[@class='find-course search-course'])"
    _all_courses = "(//a[@class='dynamic-link' and text()='ALL COURSES'])"
    _course = "(//div[@id='course-list']//h4[@class='dynamic-heading' and contains (text(),'{0}')])"
    _enroll_button = "(//button[@class='dynamic-button btn btn-default btn-lg btn-enroll' and text()='Enroll in Course'])"
    _cc_num = "(//input[@aria-label='Credit or debit card number'])"
    _cc_exp = "(//input[@name='exp-date'])"
    _cc_cvc = "(//input[@name='cvc'])"
    _submit_enroll = "(//button[@class='zen-subscribe sp-buy btn btn-default btn-lg btn-block btn-gtw btn-submit checkout-button dynamic-button'])"
    _enrol_error_message = "(//span[normalize-space()='Your card number is incorrect.'])[1]"

    def clickAllCoursesTab(self):
        self.elementClick(self._all_courses, locatorType="xpath")

    def enterCourseName(self, name):
        self.sendKeys(name, self._search_box)
        self.elementClick(self._search_button, locatorType="xpath")


    def selectCourseToEnroll(self, fullCourseName):
        self.elementClick(locator=self._course.format(fullCourseName), locatorType="xpath")

    def clickEnrollToCourseButton(self):
        self.elementClick(self._enroll_button)

    def enterCardNum(self, num):
        time.sleep(3)
        self.SwitchFrameByIndex(self._cc_num, locatorType="xpath")
        self.sendKeysWhenReady(num, locator=self._cc_num, locatorType="xpath")
        self.switchToDefaultContent()

    def enterCardExp(self, exp):
        time.sleep(3)
        self.SwitchFrameByIndex(self._cc_exp, locatorType="xpath")
        self.sendKeysWhenReady(exp, locator=self._cc_exp, locatorType="xpath")
        self.switchToDefaultContent()

    def enterCardCvc(self, cvc):
        time.sleep(3)
        self.SwitchFrameByIndex(self._cc_cvc, locatorType="xpath")
        self.sendKeysWhenReady(cvc, locator=self._cc_cvc, locatorType="xpath")
        self.switchToDefaultContent()

    def enterCreditCardInformation(self, num, exp, cvc):
        self.enterCardNum(num)
        self.enterCardExp(exp)
        self.enterCardCvc(cvc)

    def clickEnrollSubmitButton(self):
        self.elementClick(self._submit_enroll, locatorType="xpath")

    def enrollCourse(self, num="", exp="", cvc=""):
        self.webScroll(direction="little down")
        # self.webScroll_1(direction="down")
        self.clickEnrollToCourseButton()
        self.webScroll(direction="down")
        self.enterCreditCardInformation(num, exp, cvc)
        time.sleep(3)
        self.clickEnrollSubmitButton()
        time.sleep(3)


    def verifyEnrollFailed(self):
         result = self.isElementDisplayed(locator=self._enrol_error_message,
                                        locatorType="xpath")
         return result

