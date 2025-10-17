# Imports at the top
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


# Create a new instance of the Chrome driver
driver = webdriver.Chrome()


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
first_template = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, template_card_xpath))
)
first_template.click()

# Print page source for debugging after clicking the template card
print("--- PAGE SOURCE AFTER TEMPLATE CARD CLICK ---")
print(driver.page_source)

try:
    # Debug: print page source before trying to find the event name input
    print("--- PAGE SOURCE BEFORE EVENT NAME INPUT ---")
    print(driver.page_source)

    # Try to find the event name input
    event_name_xpath = "//input[@placeholder='მაგალითად, ემა და ნოას ქორწილი']"
    try:
        event_name_input = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, event_name_xpath))
        )
        print("Found event name input. Sending keys...")
        event_name_input.clear()
        event_name_input.send_keys("Party")
        # Now enter 'Tbilisi' into the location input field
        location_xpath = "//input[@placeholder='მაგალითად, ცენტრალური პარკი, ნიუ-იორკი']"
        try:
            location_input = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, location_xpath))
            )
            print("Found location input. Sending keys...")
            location_input.clear()
            location_input.send_keys("Tbilisi")
            # Now enter the message into the guest message textarea
            message_xpath = "//textarea[@placeholder='დაამატეთ პერსონალური შეტყობინება თქვენი სტუმრებისთვის...']"
            try:
                message_textarea = WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located((By.XPATH, message_xpath))
                )
                print("Found message textarea. Sending keys...")
                message_textarea.clear()
                message_textarea.send_keys("you are more then welcome to come with a friend")
                # Now enter the date into the date input field
                date_xpath = "//input[@type='date']"
                try:
                    date_input = WebDriverWait(driver, 10).until(
                        EC.visibility_of_element_located((By.XPATH, date_xpath))
                    )
                    print("Found date input. Sending keys...")
                    date_input.clear()
                    date_input.send_keys("10/10/2025")
                    # Now click the 'მოსაწვევის შექმნა' button
                    create_button_xpath = "//button[contains(text(),'მოსაწვევის შექმნა')]"
                    try:
                        create_button = WebDriverWait(driver, 10).until(
                            EC.element_to_be_clickable((By.XPATH, create_button_xpath))
                        )
                        print("Found create invitation button. Clicking...")
                        create_button.click()
                    except Exception as e:
                        print(f"Could not find or interact with create invitation button: {e}")
                        driver.save_screenshot("create_button_error.png")
                        input("Press Enter to close the browser...")
                except Exception as e:
                    print(f"Could not find or interact with date input: {e}")
                    driver.save_screenshot("date_input_error.png")
                    input("Press Enter to close the browser...")
            except Exception as e:
                print(f"Could not find or interact with message textarea: {e}")
                driver.save_screenshot("message_textarea_error.png")
                input("Press Enter to close the browser...")
        except Exception as e:
            print(f"Could not find or interact with location input: {e}")
            driver.save_screenshot("location_input_error.png")
            input("Press Enter to close the browser...")
    except Exception as e:
        print(f"Could not find or interact with event name input: {e}")
        # Optionally, save a screenshot for debugging
        driver.save_screenshot("event_name_input_error.png")
        input("Press Enter to close the browser...")
finally:
    driver.quit()
