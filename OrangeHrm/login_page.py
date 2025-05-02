from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

# Initialize the driver
driver = webdriver.Chrome()

# Open the OrangeHRM demo site
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()

# Add some delay to allow page to load
time.sleep(2)

# Locate username and password fields and login button
driver.find_element(By.NAME, "username").send_keys("Admin")
driver.find_element(By.NAME, "password").send_keys("admin123")
driver.find_element(By.XPATH, "//button[@type='submit']").click()

# Wait to observe the result (later you'll use assertions instead)
time.sleep(5)

# Close the browser
driver.quit()
