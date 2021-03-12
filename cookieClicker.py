from selenium import webdriver
import time

chrome_driver_path ="/Users/rszotak/Desktop/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)


driver.get("https://orteil.dashnet.org/cookieclicker/")
cookie = driver.find_element_by_id("bigCookie")
cookie_count_element = driver.find_element_by_id("cookies")
print(cookie_count_element.text)
full_timeout = time.time() + 60*5
timeout = time.time() + 5
while True:
    cookie.click()
    if time.time() >= timeout:
        timeout = time.time() + 12
        products = driver.find_elements_by_class_name("enabled")
        index = len(products) - 1
        for i in range (0, 2):
            products[index].click()
    if time.time() > full_timeout:
        break

