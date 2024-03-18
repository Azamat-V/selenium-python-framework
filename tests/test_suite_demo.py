import unittest
from tests.home.login_tests_171 import LoginTests
from tests.courses.register_courses_csv_data_197 import RegisterCoursesCSVDataTests

# Get all tests from the test classes

tc_1 = unittest.TestLoader().loadTestsFromTestCase(LoginTests)
ts_2 = unittest.TestLoader().loadTestsFromTestCase(RegisterCoursesCSVDataTests)

# Create a test suite combining all test classes

smokeTest = unittest.TestSuite([tc_1, ts_2])

unittest.TextTestRunner(verbosity=2).run(smokeTest)