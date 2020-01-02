from bs4 import BeautifulSoup
import requests

# perform a GET request to download the page
page = requests.get("https://www.google.com/search?q=Yo")

# check if the request was successful
print(page.status_code)

# parse the page using BeautifulSoup
soup = BeautifulSoup(page.content, 'html.parser')

# get data using a specific element id
print(soup.find_all(id="resultStats"))
