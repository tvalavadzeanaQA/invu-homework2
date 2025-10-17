# Imports at the top
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


# Create a new instance of the Chrome driver
driver = webdriver.Chrome()

try:
	# Open the website
	driver.get("https://invu.ge")
	time.sleep(5)

	# Click the login button
	login_button = WebDriverWait(driver, 10).until(
		EC.element_to_be_clickable((By.XPATH, "//a[@class='desktop-login'][contains(text(),'შესვლა')]"))
	)
	login_button.click()

	# Enter email address
	email_input = WebDriverWait(driver, 10).until(
		EC.visibility_of_element_located((By.XPATH, "//input[@id='email']"))
	)
	email_input.clear()
	email_input.send_keys("gogiashviligvants@gmail.com")

	# Enter password
	password_input = WebDriverWait(driver, 10).until(
		EC.visibility_of_element_located((By.XPATH, "//input[@id='password']"))
	)

	password_input.clear()
	password_input.send_keys("genofit2025")

	# Click the 'Sign In' button
	signin_button = WebDriverWait(driver, 10).until(
		EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Sign In']"))
	)
	signin_button.click()

	# Wait for URL to change after login
	WebDriverWait(driver, 10).until(lambda d: d.current_url != "https://invu.ge/login")
	print("--- PAGE SOURCE AFTER LOGIN ---")
	print(driver.page_source)

	# Click the 'შაბლონები' link in the desktop nav
	templates_link = WebDriverWait(driver, 10).until(
		EC.element_to_be_clickable((By.XPATH, "//div[@class='desktop-nav']//a[contains(text(),'შაბლონები')]"))
	)
	templates_link.click()

	# Wait for URL to change after clicking 'შაბლონები'
	WebDriverWait(driver, 10).until(lambda d: "/templates" in d.current_url)
	print("--- PAGE SOURCE AFTER TEMPLATES CLICK ---")
	print(driver.page_source)

	# Wait for the first template card to be visible and clickable
	template_card_xpath = "//body/div[@id='root']/div[@class='min-h-screen bg-gray-50 text-primary-500']/div[@class='pt-20']/main[@class='min-h-screen bg-gray-50 relative overflow-hidden']/div[@class='relative max-w-7xl mx-auto px-4 py-8']/div[@class='flex flex-col lg:flex-row gap-8']/div[@class='flex-1 w-full']/div[@class='grid gap-4 sm:gap-6 grid-cols-1 sm:grid-cols-2 lg:grid-cols-3']/div[1]"
	try:
		first_template = WebDriverWait(driver, 20).until(
			EC.element_to_be_clickable((By.XPATH, template_card_xpath))
		)
		first_template.click()

		# Print page source for debugging after clicking the template card
		print("--- PAGE SOURCE AFTER TEMPLATE CARD CLICK ---")
		print(driver.page_source)

		# Increase wait time for page load/navigation
		time.sleep(5)

		# TODO: Identify a better XPath for the parent container if needed
		general_parent_xpath = "//form"  # Try changing this XPath if the form does not appear
		WebDriverWait(driver, 20).until(
			EC.visibility_of_element_located((By.XPATH, general_parent_xpath))
		)

		# Enter 'იუბილე' into the event name field
		jubilee_input = WebDriverWait(driver, 10).until(
			EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='მაგალითად, ემა და ნოას ქორწილი']"))
		)
		jubilee_input.clear()
		jubilee_input.send_keys("იუბილე")

		# Enter 'თბილისი' into the location field
		tbilisi_input = WebDriverWait(driver, 10).until(
			EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='მაგალითად, ცენტრალური პარკი, ნიუ-იორკი']"))
		)
		tbilisi_input.clear()
		tbilisi_input.send_keys("თბილისი")

		# Enter 'მოუთმენად გელოდებით' into the message textarea
		message_textarea = WebDriverWait(driver, 10).until(
			EC.visibility_of_element_located((By.XPATH, "//textarea[@placeholder='დაამატეთ პერსონალური შეტყობინება თქვენი სტუმრებისთვის...']"))
		)
		message_textarea.clear()
		message_textarea.send_keys("მოუთმენად გელოდებით")

		# Select the date '2025-10-20' in the date input
		date_input = WebDriverWait(driver, 10).until(
			EC.visibility_of_element_located((By.XPATH, "//input[@type='date']"))
		)
		date_input.clear()
		date_input.send_keys("2025-10-20")
	except Exception as e:
		print(f"Error in template card or form filling: {e}")
		# Check if browser is still open before taking screenshot
		try:
			if driver.session_id:
				driver.save_screenshot("template_card_error.png")
			else:
				print("Browser session is closed, cannot take screenshot.")
		except Exception as screenshot_error:
			print(f"Screenshot error: {screenshot_error}")
		# Do not close the browser immediately for debugging
		input("Press Enter to close the browser...")
		raise
finally:
	driver.quit()