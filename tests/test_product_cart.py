from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_button_add_presence(browser, base_url):
    browser.get(base_url + '/index.php?route=product/product&product_id=40')
    WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.ID, 'button-cart')))


def test_input_quantity_presence(browser, base_url):
    browser.get(base_url + '/index.php?route=product/product&product_id=40')
    WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.ID, 'input-quantity')))


def test_compare_presence(browser, base_url):
    browser.get(base_url + '/index.php?route=product/product&product_id=40')
    browser.implicitly_wait(2)
    WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.CLASS_NAME, 'fa.fa-exchange')))


def test_addtowishlist_presence(browser, base_url):
    browser.get(base_url + '/index.php?route=product/product&product_id=40')
    browser.implicitly_wait(2)
    WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.CLASS_NAME, 'fa.fa-heart')))


def test_gobackhome_presence(browser, base_url):
    browser.get(base_url + '/index.php?route=product/product&product_id=40')
    browser.implicitly_wait(2)
    WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.CLASS_NAME, 'fa.fa-home')))
