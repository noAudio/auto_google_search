import requests

page = requests.get("https://www.google.com/search?q=Yo")

print(page.status_code)
