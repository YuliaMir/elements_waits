from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_settings_presence(browser, base_url):
    browser.get(base_url + '/admin')
    button = browser.find_element(By.CLASS_NAME, "btn.btn-primary")
    button.click()
    WebDriverWait(browser, 2).until(EC.presence_of_element_located((By.ID, 'button-setting')))


def test_header_logo_presence(browser, base_url):
    browser.get(base_url + '/admin')
    button = browser.find_element(By.CLASS_NAME, "btn.btn-primary")
    button.click()
    WebDriverWait(browser, 2).until(EC.presence_of_element_located((By.ID, 'header-logo')))


def test_user_profile_presence(browser, base_url):
    browser.get(base_url + '/admin')
    button = browser.find_element(By.CLASS_NAME, "btn.btn-primary")
    button.click()
    WebDriverWait(browser, 2).until(EC.presence_of_element_located((By.ID, 'user-profile')))


def test_zoomin_presence(browser, base_url):
    browser.get(base_url + '/admin')
    button = browser.find_element(By.CLASS_NAME, "btn.btn-primary")
    button.click()
    WebDriverWait(browser, 2).until(EC.presence_of_element_located((By.CLASS_NAME, 'jqvmap-zoomin')))


def test_zoomout_presence(browser, base_url):
    browser.get(base_url + '/admin')
    button = browser.find_element(By.CLASS_NAME, "btn.btn-primary")
    button.click()
    WebDriverWait(browser, 2).until(EC.presence_of_element_located((By.CLASS_NAME, 'jqvmap-zoomout')))
