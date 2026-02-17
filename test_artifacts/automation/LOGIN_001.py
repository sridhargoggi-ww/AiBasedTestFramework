

Manual Test Cases:
------------------

### Login with Valid Credentials

**Preconditions:** User has an account and valid credentials (username and password).

**Steps:**
1. Open the login page by navigating to `https://example.com/login`.
2. Enter the username in the "Username" field.
3. Enter the password in the "Password" field.
4. Click on the "Login" button.
5. Verify that the user is redirected to the dashboard page by checking if the URL contains "/dashboard".
6. Verify that the login was successful by checking for a message indicating so.

**Expected Results:** User should be able to log in with valid credentials and be redirected to the dashboard page. A success message should be displayed.

### Invalid Login

**Preconditions:** User has an account but invalid credentials (wrong username or password).

**Steps:**
1. Open the login page by navigating to `https://example.com/login`.
2. Enter a wrong username in the "Username" field.
3. Enter a valid password in the "Password" field.
4. Click on the "Login" button.
5. Verify that an error message is displayed indicating that the login was unsuccessful.
6. Verify that the user is not redirected to the dashboard page by checking if the URL does not contain "/dashboard".

**Expected Results:** User should receive an error message when attempting to log in with invalid credentials and will not be redirected to the dashboard page.

Automation-Ready Playwright/Python Test Cases:
-----------------------------------------------

### Login with Valid Credentials (Playwright)
```python
from playwright import webdriver
import time

# Launch browser and navigate to login page
driver = webdriver.Chrome()
driver.get("https://example.com/login")

# Enter username and password in fields
username_field = driver.find_element_by_name("username")
password_field = driver.find_element_by_name("password")

username_field.send_keys("valid_username")
password_field.send_keys("valid_password")

# Click on login button and wait for page to load
login_button = driver.find_element_by_xpath("//button[@type='submit']")
login_button.click()
time.sleep(5)  # Wait for dashboard page to load

# Verify that user is redirected to dashboard page and success message is displayed
dashboard_url = "https://example.com/dashboard"
success_message = driver.find_element_by_xpath("//div[@class='success-message']")

assert driver.current_url == dashboard_url, f"User was not redirected to dashboard page: {driver.current_url}"
assert success_message is not None, "Success message was not displayed"
```
### Invalid Login (Playwright)
```python
from playwright import webdriver
import time

# Launch browser and navigate to login page
driver = webdriver.Chrome()
driver.get("https://example.com/login")

# Enter wrong username in field and click on login button
username_field = driver.find_element_by_name("username")
password_field = driver.find_element_by_name("password")

username_field.send_keys("wrong_username")
password_field.send_keys("valid_password")
login_button = driver.find_element_by_xpath("//button[@type='submit']")
login_button.click()
time.sleep(5)  # Wait for error message to be displayed

# Verify that error message is displayed and user is not redirected to dashboard page
error_message = driver.find_element_by_xpath("//div[@class='error-message']")
dashboard_url = "https://example.com/dashboard"

assert error_message is not None, f"Error message was not displayed: {error_message.text}"
assert driver.current_url != dashboard_url, f"User was redirected to dashboard page when invalid login attempt: {driver.current_url}"
```