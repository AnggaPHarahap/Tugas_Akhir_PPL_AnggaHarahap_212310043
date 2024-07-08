import sys
import os

# Tambahkan direktori root proyek Anda ke PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.driver_setup import get_driver

def test_admin_login():
    driver = get_driver()
    # Lanjutkan dengan pengujian Anda
    driver.get('https://opensource-demo.orangehrmlive.com/')
    
    # Contoh pengujian login
    username_field = driver.find_element(By.ID, 'txtUsername')
    password_field = driver.find_element(By.ID, 'txtPassword')
    login_button = driver.find_element(By.ID, 'btnLogin')

    username_field.send_keys('Admin')
    password_field.send_keys('admin123')
    login_button.click()

    # Tunggu beberapa detik untuk melihat hasil
    time.sleep(5)

    driver.quit()

if __name__ == "__main__":
    test_admin_login()
