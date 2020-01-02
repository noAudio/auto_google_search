from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import time
import re

# read list of search terms from a text file then
# remove all newline characters
searchTerms = open("search_terms.txt").readlines()
searchTerms = [s.rstrip('\n') for s in searchTerms]

# store position of chrome webdriver in a variable
driver = webdriver.Chrome(
    'C:/ProgramData/chocolatey/lib/chromedriver/tools/chromedriver.exe')


def autoSearch(driver, url):
    # use driver to perform a GET request
    # while giving it time to render the page
    driver.get(url)
    time.sleep(1)

    # pass it on to BeautifulSoup
    # parse the page using BeautifulSoup
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    # print(soup.prettify())

    # get data using a specific element id and
    # assign it to a variable
    results = soup.find_all(id="resultStats")[0].get_text()
    return results


def cleanString(dirtyResult):
    partialClean = dirtyResult[6:]
    fullClean = partialClean[:-24]
    fullClean = re.sub(',', '', fullClean)

    return fullClean


# iterate through searchTerms list and execute function on it
for i in searchTerms:
    url = "https://www.google.com/search?q={0}".format(i)
    print("Searching " + url)

    # pass the driver and url to the function
    resultStats = autoSearch(driver, url)

    finalResults = cleanString(resultStats)
    # write the results to a text file
    f = open("results.txt", "a+")
    f.write("{0}, {1}\n".format(i, finalResults))
    f.close()

    print('The search term ' + i + ' has ' + finalResults + ' results')
    print('Results written to file.')

print('No search terms left')
driver.quit()
