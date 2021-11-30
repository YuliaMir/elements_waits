from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_header_presence(browser, base_url):
    browser.get(base_url + '/admin')
    browser.implicitly_wait(2)

    input1 = browser.find_element(By.ID, "input-username")
    input1.send_keys("demo")
    input2 = browser.find_element(By.ID, "input-password")
    input2.send_keys("demo")
    button = browser.find_element(By.CLASS_NAME, "btn.btn-primary")
    button.click()
    time.sleep(5)
    #WebDriverWait(browser, 2).until(EC.visibility_of_element_located((By.ID, 'button-setting')))


