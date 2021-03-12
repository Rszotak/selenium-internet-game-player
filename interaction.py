from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_driver_path ="/Users/rszotak/Desktop/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)


driver.get("http://secure-retreat-92358.herokuapp.com/")

first_name = driver.find_element_by_name("fName")
last_name = driver.find_element_by_name("lName")
email = driver.find_element_by_name("email")

first_name.send_keys("Ryan")
last_name.send_keys("Zoltan")
email.send_keys("test@test.com")

email.send_keys(Keys.ENTER)

# driver.get("https://en.wikipedia.org/wiki/Main_Page")
#
# article_count = driver.find_element_by_css_selector("#articlecount a")
# # article_count.click()
#
# all_portals = driver.find_element_by_link_text("All portals")
# #all_portals.click()

# search_bar = driver.find_element_by_name("search")
# search_bar.send_keys("Python")
# search_bar.send_keys(Keys.ENTER)

#driver.quit()