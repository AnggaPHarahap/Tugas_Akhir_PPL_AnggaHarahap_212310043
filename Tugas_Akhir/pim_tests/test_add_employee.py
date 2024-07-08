import unittest
from selenium.webdriver.common.by import By
from utils.driver_setup import get_driver

class AddEmployeeTest(unittest.TestCase):

    def setUp(self):
        self.driver = get_driver()
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        self.login_as_admin()

    def login_as_admin(self):
        driver = self.driver
        driver.find_element(By.ID, "txtUsername").send_keys("Admin")
        driver.find_element(By.ID, "txtPassword").send_keys("admin123")
        driver.find_element(By.ID, "btnLogin").click()

    def test_add_employee(self):
        driver = self.driver
        driver.find_element(By.ID, "menu_pim_viewPimModule").click()
        driver.find_element(By.ID, "menu_pim_addEmployee").click()
        driver.find_element(By.ID, "firstName").send_keys("John")
        driver.find_element(By.ID, "lastName").send_keys("Doe")
        driver.find_element(By.ID, "btnSave").click()
        self.assertTrue(driver.find_element(By.ID, "personal_txtEmpFirstName").is_displayed())

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
