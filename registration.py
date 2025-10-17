from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

# Create a new instance of the Chrome driver
driver = webdriver.Chrome()

# Open the website
driver.get("https://invu.ge")
driver.implicitly_wait(10)  # Wait for elements to load
# Find and click the registration button
register_button = driver.find_element(By.XPATH, "//a[@href='/register']")
register_button.click()

# Enter 'Ana' in the first name input field
first_name_input = driver.find_element(By.XPATH, "//input[@id='firstName']")
first_name_input.send_keys("Ana")

# Enter 'Tvalavadze' in the last name input field
last_name_input = driver.find_element(By.XPATH, "//input[@id='lastName']")
last_name_input.send_keys("Tvalavadze")

# Enter email in the email input field
email_input = driver.find_element(By.XPATH, "//input[@id='email']")
email_input.send_keys("ana.tvalavadze0114@hum.tsu.edu.ge")

# Enter password in the password input field
password_input = driver.find_element(By.XPATH, "//input[@id='password']")
password_input.send_keys("19980604")

# Enter password confirmation in the confirmPassword input field
confirm_password_input = driver.find_element(By.XPATH, "//input[@id='confirmPassword']")
confirm_password_input.send_keys("19980604")

# Click the submit button
submit_button = driver.find_element(By.XPATH, "//button[@type='submit']")
submit_button.click()

# Optional: keep the browser open for a few seconds
import time
time.sleep(5)

# Close the browser
driver.quit()