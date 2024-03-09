from pages.courses.register_courses_pages import RegisterCoursesPage
from utilities.assertstatus import AssertStatus
import unittest
import pytest

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class RegisterCoursesTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.rp = RegisterCoursesPage(self.driver)
        self.ts = AssertStatus(self.driver)


    @pytest.mark.run()
    def test_invalidEnrollment(self):
        self.rp.enrollCourse("Java", "4400 4345 8071 0712", "12/25", "222")
        self.rp.verifyEnrollFailed()




