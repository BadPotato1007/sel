from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
import time

# Set the path to your chromedriver executable

# Set Chrome options to enable incognito mode
chrome_options = Options()
chrome_options.add_argument('--incognito')
chrome_options.add_extension('./chromium_automation/chromium_automation.crx')


user = "neerav gupta neeravgupta07"
x  = user.split()

mail = x[2]
name_1 = x[0]
name_2 = x[1]
print("settings:", mail, name_1, name_2)

driver = webdriver.Chrome(options=chrome_options)

try:
    # Open a website
    driver.get('https://signup.live.com/?lic=1')

    # Wait until an element becomes visible
    wait = WebDriverWait(driver, 1000)  # Wait up to 10 seconds
    get_new_mail = wait.until(EC.visibility_of_element_located((By.ID, 'liveSwitch')))
    
    # Perform an action on the element
    get_new_mail.click()
    
    
    usernameInput = wait.until(EC.visibility_of_element_located((By.ID, 'usernameInput')))
    usernameInput.send_keys(mail)
    
    next_button = wait.until(EC.visibility_of_element_located((By.ID, 'nextButton')))
    next_button.click()
    
    password = wait.until(EC.visibility_of_element_located((By.ID, 'Password')))
    password.send_keys('#Happyboy1234')
    
    next_button = wait.until(EC.visibility_of_element_located((By.ID, 'nextButton')))
    next_button.click()
    
    name1 = wait.until(EC.visibility_of_element_located((By.ID, 'firstNameInput')))
    name1.send_keys(name_1)
    
    name2 = wait.until(EC.visibility_of_element_located((By.ID, 'lastNameInput')))
    name2.send_keys(name_2)
    
    next_button = wait.until(EC.visibility_of_element_located((By.ID, 'nextButton')))
    next_button.click()
    
    month = wait.until(EC.visibility_of_element_located((By.ID, 'BirthMonth')))
    dropdown1 = Select(month)
    dropdown1.select_by_visible_text('February')

    day = wait.until(EC.visibility_of_element_located((By.ID, 'BirthDay')))
    dropdown1 = Select(day)
    dropdown1.select_by_visible_text('12')
    
    year = wait.until(EC.visibility_of_element_located((By.ID, 'BirthYear')))
    year.send_keys('2000')
    
    next_button = wait.until(EC.visibility_of_element_located((By.ID, 'nextButton')))
    next_button.click()
    
    
    time.sleep(100)

finally:
    # Close the browser
    driver.quit()
