from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Define the driver ID
driver_id = 221863


# Define the path to the desktop folder containing photos
desktop_folder = 'C:/Users/lenovo/Desktop/docsProject/ops_docs'

# Create a dictionary to hold the file paths
files = {
    'nationalCard': open(f'{desktop_folder}/{driver_id} - nid_front.jpg', 'rb'),
    'nationalCardBack': open(f'{desktop_folder}/{driver_id} - nid_back.jpg', 'rb'),
    'drivingCertificate': open(f'{desktop_folder}/{driver_id} - licence_front.jpg', 'rb'),
    'drivingCertificateBack': open(f'{desktop_folder}/{driver_id} - licence_back.jpg', 'rb'),
    'registerForm': open(f'{desktop_folder}/{driver_id} - ijaza_front.jpg', 'rb'),
    'registerFormBack': open(f'{desktop_folder}/{driver_id} - ijaza_back.jpg', 'rb'),
    'background': open(f'{desktop_folder}/{driver_id} - nid_front.jpg', 'rb'),
    'termsAndConditions': open(f'{desktop_folder}/{driver_id} - nid_front.jpg', 'rb'),
    'other': open(f'{desktop_folder}/{driver_id} - others.jpg', 'rb')
}

# Initialize Chrome webdriver
driver = webdriver.Chrome()

# Define the URL of the login page and the form submission endpoint
login_url = 'https://backoffice.baly.app/auth/sign-in'
form_submission_url = f'https://backoffice.baly.app/admin/drivers/{driver_id}/docs'

# Navigate to the login page
driver.get(login_url)

# Enter your credentials and submit the login form
username_input = driver.find_element(By.ID, 'email')
password_input = driver.find_element(By.ID, 'password')

# Replace 'your_username' and 'your_password' with your actual credentials
username_input.send_keys('zahraa.jabar@baly.iq')
password_input.send_keys('#Uu.t4j*E3Mgkz)')

login_button = driver.find_element(By.XPATH, '//input[@type="submit"]')
login_button.click()

# Wait for the login process to complete
# WebDriverWait(driver, 30).until(EC.url_contains('backoffice.baly.app/admin'))

time.sleep(2)

# Now that you are logged in, proceed to the form submission page
driver.get(form_submission_url)
time.sleep(1)

# Find and upload files to the form
for field_name, file_obj in files.items():
    # driver.get(form_submission_url)
    # time.sleep(1)
    file_input = driver.find_element(By.NAME, field_name)
    file_input.send_keys(file_obj.name)

    # Find and click the upload button
    upload_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Upload')]")
    upload_button.click()
    time.sleep(2)


# Close the webdriver
driver.quit()
