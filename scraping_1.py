# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

URL = "https://muztorg.ua/uk/yamaha/"
START_PAGE, TOTAL_PAGES = 1, 5
driver = webdriver.Chrome()
driver.get(URL)
collection = []


def get_data(driver):
    elements = driver.find_elements(By.CLASS_NAME, "caption")
    i = 0
    items = []
    while i <= len(elements):
        try:
            element = elements[i]
            element.click()
            data = driver.find_element(By.CLASS_NAME, "info-list").text.split("\n")
            item = dict(zip(data[0::2], data[1::0]))
            item["url"] = driver.current_url
            items.append(item)
            yield item

        except:
            pass
        driver.back()
        elements = driver.find_elements(By.CLASS_NAME, "caption")
        i += 1


def save_file(info_file, items):
    with open(info_file, "a") as file:
        for i in items:
            file.write(str(i))
            file.write("\n")


page_num = START_PAGE
while page_num <= TOTAL_PAGES:
    try:
        driver.get(f"https://muztorg.ua/uk/yamaha/PAGEN_1={page_num}")
        items = get_data(driver)
        save_file('result.json', items)
        page_num += 1
    except:
        driver.refresh()
driver.close()



