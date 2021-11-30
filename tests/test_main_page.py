from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_header_presence(browser):
    browser.get("https://demo.opencart.com/")
    browser.implicitly_wait(2)
    WebDriverWait(browser, 1).until(EC.visibility_of_element_located((By.XPATH, 'div[@id="logo"]/h1/a')))
