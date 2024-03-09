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
    @data(("JavaScript for beginners", "8500 4345 8071 0712", "12/25", "222"), ("Cypress.io Test Automation", "4400 4345 8071 0712", "12/25", "222"))
    @unpack
    def test_invalidEnrollment(self, courseName, ccNum, ccExp, ccCVC):
        self.rp.enrollCourse(courseName, num=ccNum, exp=ccExp, cvc=ccCVC)
        self.rp.verifyEnrollFailed()
        self.driver.find_element(By.XPATH, "(//a[@href='/courses' and text()='ALL COURSES'])").click
        print("I clicked on it")
        time.sleep(3)

