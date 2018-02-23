import time
from selenium import webdriver
from random import randint
from urllib.request import urlopen
from bs4 import BeautifulSoup


# my path is '/Users/mcadams/Documents/python/python-beginners'
# yours will be different


driver = webdriver.Chrome('/Users/mcadams/Documents/python/python-beginners/chromedriver')
driver.get('https://www.rottentomatoes.com/browse/dvd-streaming-all');

# click the button exactly 8 times
for n in range(8):
    driver.find_element_by_css_selector('.btn.btn-secondary-rt.mb-load-btn').click()
    # the button tag has class="btn btn-secondary-rt mb-load-btn"
    # ... we told it which button to click
    # make a random wait time between 1 and 10 seconds to look less bot-like
    s = randint(1, 10)
    # sleep that number of seconds
    time.sleep(s)

html = driver.page_source

bsObj = BeautifulSoup(html, "html.parser")
title_list = bsObj.findAll("h3", {"class":"movieTitle"})
for title in title_list:
    print(title.get_text())

print("There are " + str(len(title_list)) + " movies in the list.")

driver.quit()
