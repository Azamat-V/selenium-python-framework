import time

from pages.courses.register_courses_pages import RegisterCoursesPage
from utilities.assertstatus import AssertStatus
import unittest
import pytest
from ddt import ddt, data, unpack
from selenium.webdriver.common.by import By

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
@ddt
class RegisterCoursesTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.rp = RegisterCoursesPage(self.driver)
        self.ts = AssertStatus(self.driver)


    @pytest.mark.run()
    @data(("JavaScript for beginners", "8500 4345 8071 0712", "12/25", "222"), ("Cypress.io Test Automation", "8500 4345 8071 0522", "12/25", "222"))
    @unpack
    def test_invalidEnrollment(self, courseName, ccNum, ccExp, cCVC):
        self.rp.clickAllCoursesTab()
        self.rp.selectCourseToEnroll(fullCourseName=courseName)
        self.rp.enrollCourse(num=ccNum, exp=ccExp, cvc=cCVC)
        result = self.rp.verifyEnrollFailed()
        self.ts.markFinal("test_invalidEnrollment", result, "Enrollment Failed Message" )
        self.driver.find_element(By.XPATH, "(//a[@href='/courses' and text()='ALL COURSES'])").click
        print("I clicked on it")
        time.sleep(3)

