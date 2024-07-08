import unittest
from selenium.webdriver.common.by import By
from utils.driver_setup import get_driver

class ApplyLeaveTest(unittest.TestCase):

    def setUp(self):
        self.driver = get_driver()
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        self.login_as_employee()

    def login_as_employee(self):
        driver = self.driver
        driver.find_element(By.ID, "txtUsername").send_keys("Employee")
        driver.find_element(By.ID, "txtPassword").send_keys("employee123")
        driver.find_element(By.ID, "btnLogin").click()

    def test_apply_leave(self):
        driver = self.driver
        driver.find_element(By.ID, "menu_leave_viewLeaveModule").click()
        driver.find_element(By.ID, "menu_leave_applyLeave").click()
        driver.find_element(By.ID, "applyleave_txtLeaveType").send_keys("Annual Leave")
        driver.find_element(By.ID, "applyleave_txtFromDate").send_keys("2022-12-01")
        driver.find_element(By.ID, "applyleave_txtToDate").send_keys("2022-12-10")
        driver.find_element(By.ID, "applyBtn").click()
        self.assertTrue(driver.find_element(By.ID, "applyleave_leaveBalance").is_displayed())

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
