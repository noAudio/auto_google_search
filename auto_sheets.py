from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import time

searchTerms = ["one", "two"]
driver = webdriver.Chrome(
    'C:/ProgramData/chocolatey/lib/chromedriver/tools/chromedriver.exe')


def autoSearch(driver, url):
    # use driver to perform a GET request
    # while giving it time to render the page
    driver.get(url)
    time.sleep(5)

    # pass it on to BeautifulSoup
    # parse the page using BeautifulSoup
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    # print(soup.prettify())

    # get data using a specific element id and
    # assign it to a variable
    resultStats = soup.find_all(id="resultStats")[0].get_text()
    return resultStats


# iterate through searchTerms list and execute function on it
for i in searchTerms:
    url = "https://www.google.com/search?q={0}".format(i)
    print("Searching " + url)
    resultStats = autoSearch(driver, url)
    print(i, ' has ', resultStats)
