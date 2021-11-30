import time


def test_first_test(browser, url):
    browser.get(url)
    time.sleep(5)

    assert browser.title == "Your Store"

    #driver.save_screenshot("{}.png".format(driver.session_id))