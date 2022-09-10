import requests 
from bs4 import BeautifulSoup

URL = 'https://www.jumia.co.ke/calvin-klein-ck-euphoria-intense-100-ml-edt-25602416.html'

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0'}

page = requests.get(URL, headers=headers)  

soup = BeautifulSoup(page.content, 'html.parser')

print(soup.prettify())

# title = soup.find(id="brand").get_text()
# print(soup())
# item = soup.find(class_="products -euphoria")
# print(item)