from selenium import webdriver

chrome_driver_path ="/Users/rszotak/Desktop/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.python.org/")

dates = driver.find_elements_by_css_selector(".event-widget ul li time")
events = driver.find_elements_by_css_selector(".event-widget ul li a")
event_dict = {}
for i in range (0, len(dates)):
    event_dict[i] = {
        "time": dates[i].text,
        "name": events[i].text
    }
print(event_dict)
#print(dates[0].get_attribute("datetime"))
#print(events[0].get_attribute("href"))

# price_element = driver.find_element_by_id("priceblock_ourprice")
# print(price_element.text)

# search_bar = driver.find_element_by_name("q")
# print(search_bar.get_attribute("placeholder"))

#driver.find_element_by_css_selector(".documentation-widget a")

#driver.find_element_by_xpath("copied xpath goes here!")


driver.quit()