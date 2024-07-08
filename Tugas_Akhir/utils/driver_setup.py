from selenium import webdriver

def get_driver():
    # Ubah path ke lokasi ChromeDriver yang Anda unduh
    driver_path = 'path/to/chromedriver'
    return webdriver.Chrome(executable_path=driver_path)
