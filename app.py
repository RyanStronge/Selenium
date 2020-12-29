from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome()

driver.get("http://www.python.org")
try:
    assert "Java" in driver.title
except AssertionError:
    print("Java not in title.")

try:
    elem = driver.find_element_by_name("q")
    elem.clear()
    elem.send_keys("pycon")
    elem.send_keys(Keys.RETURN)
except NoSuchElementException:
    print("No such element")

try:
    assert "No results found." not in driver.page_source
except AssertionError:
    print("No results found")
