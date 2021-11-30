from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_compare_total_presence(browser, base_url):
    browser.get(base_url + '/index.php?route=product/category&path=20')
    WebDriverWait(browser, 2).until(EC.presence_of_element_located((By.ID, 'compare-total')))


def test_list_view_presence(browser, base_url):
    browser.get(base_url + '/index.php?route=product/category&path=20')
    WebDriverWait(browser, 2).until(EC.presence_of_element_located((By.CLASS_NAME, 'fa.fa-th-list')))


def test_add_to_wishlist_presence(browser, base_url):
    browser.get(base_url + '/index.php?route=product/category&path=20')
    WebDriverWait(browser, 2).until(EC.presence_of_element_located((By.CLASS_NAME, 'fa.fa-heart')))


def test_shopping_cart_presence(browser, base_url):
    browser.get(base_url + '/index.php?route=product/category&path=20')
    WebDriverWait(browser, 2).until(EC.presence_of_element_located((By.CLASS_NAME, 'fa.fa-shopping-cart')))


def test_input_limit_presence(browser, base_url):
    browser.get(base_url + '/index.php?route=product/category&path=20')
    WebDriverWait(browser, 2).until(EC.presence_of_element_located((By.ID, 'input-limit')))
