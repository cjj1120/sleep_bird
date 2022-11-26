print("START")
import os 
from dotenv import load_dotenv

load_dotenv()
os.getenv('sleep_email')


login_page = "https://accounts.fitbit.com/login?targetUrl=https%3A%2F%2Fwww.fitbit.com%2Flogin%2Ftransferpage%3Fredirect%3Dhttps%25253A%25252F%25252Fwww.fitbit.com%25252Fsettings%25252Fdata%25252Fexport&lcl=en_MY"
email = os.getenv('sleep_email')
password = os.getenv('sleep_password')

# Use Selenium 
from datetime import datetime 
import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import chromedriver_binary 
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(login_page)

element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/main/div/div/div/div[3]/form/div[1]/div/input'))
    )

# gotta do this the selenium way, for example!
# wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Sign in']"))).click()


driver.find_element("xpath", '/html/body/div[2]/div/main/div/div/div/div[3]/form/div[1]/div/input').send_keys(email);
driver.find_element("xpath", '/html/body/div[2]/div/main/div/div/div/div[3]/form/div[2]/div/input').send_keys(password);
driver.find_element("xpath", '/html/body/div[2]/div/main/div/div/div/div[3]/form/div[5]/button').click();



# click on custom button 
custom_button = "//input[@id='ember64' and @value='CUSTOM']"
element = WebDriverWait(driver, 10).until(            
        EC.presence_of_element_located((By.XPATH, custom_button)))
driver.find_element(By.XPATH, custom_button).click()


start_date_xpath = "//input[@id='ember92' and @data-test-qa='data-export-start-date'] "
driver.find_element(By.XPATH, start_date_xpath).click()



date_today_xpath = f"//div[@class='dayContainer']//*[contains(text(), {datetime.now().day})]"
driver.find_element(By.XPATH, date_today_xpath).click()

time.sleep(5)
download_button = "//button[@class='button important download-button' and text() = 'Download']"
driver.find_element(By.XPATH, download_button).click()
time.sleep(10)
driver.close()

print("END")