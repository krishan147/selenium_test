from selenium.webdriver import Chrome

driver = Chrome("chromedriver.exe")
pages = 2

for page in range(1,pages):
    url = "http://quotes.toscrape.com/js/page/" + str(page) + "/"
    driver.get(url)
    items = len(driver.find_elements_by_class_name("quote"))
    print (items)