import time
from pages.courses.register_courses_pages import RegisterCoursesPage
from utilities.assertstatus import AssertStatus
import unittest
import pytest
from ddt import ddt, data, unpack
from utilities.read_data import getCSVData
from pages.home.navigation_page import NavigationPage

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
@ddt
class RegisterCoursesCSVDataTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.courses = RegisterCoursesPage(self.driver)
        self.ts = AssertStatus(self.driver)
        self.nav = NavigationPage(self.driver)

    def setUP(self):
        self.nav.navigateToAllCourses()



    @pytest.mark.run()
    @data(*getCSVData("C:\\Users\\User\\workspace_python\\Letskodeit\\testdata.csv"))
    @unpack
    def test_invalidEnrollment(self, courseName, ccNum, ccExp, ccCVC):
        self.courses.clickAllCoursesTab()
        self.courses.enterCourseName(courseName)
        time.sleep(2)
        self.courses.selectCourseToEnroll(courseName)
        time.sleep(2)
        self.courses.enrollCourse(num=ccNum, exp=ccExp, cvc=ccCVC)
        self.courses.verifyEnrollFailed()
        print("Clicked on it")
