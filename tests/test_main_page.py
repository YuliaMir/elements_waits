from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_elements_presence(browser, base_url):
    browser.get(base_url + '/')
    WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.ID, 'form-currency')))


def test_cart_total_presence(browser, base_url):
    browser.get(base_url + '/')
    WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.ID, 'cart-total')))


def test_search_window_presence(browser, base_url):
    browser.get(base_url + '/')
    WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.ID, 'search')))


def test_cart_presence(browser, base_url):
    browser.get(base_url + '/')
    WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.ID, 'cart')))


def test_menu_presence(browser, base_url):
    browser.get(base_url + '/')
    WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.ID, 'menu')))
