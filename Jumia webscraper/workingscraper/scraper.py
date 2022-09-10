import requests 
from bs4 import BeautifulSoup
import re

URL = 'https://www.jumia.co.ke/calvin-klein-ck-euphoria-intense-100-ml-edt-25602416.html'

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0'}

page = requests.get(URL, headers=headers)  

# soup = BeautifulSoup(page.content, 'html.parser')
# print(soup)

# print(soup.prettify())

# title = soup.find(id="brand").get_text()
# print(soup())
# response = requests.get(URL, headers=headers)
page.raise_for_status()
html = page.text
bsObj = BeautifulSoup(html, features="lxml")
productName = bsObj.find("h1", {"class": "-fs20 -pts -pbxs"}).get_text()
productBrand = (bsObj.find_all("a", {"class": "_more"}))[1].get_text()
currentProductPrice = bsObj.find("span", {"class":"-b -ltr -tal -fs24"}).get_text()
previousProductPrice = bsObj.find("span", {"class":"-tal -gy5 -lthr -fs16"}).get_text()
# productDiscount = bsObj.find("span", {"class":"tag _dsct _dyn -mls"}).get()
productStarRating = bsObj.find("div", {"class":"stars _s _al"}).get_text()
productTotalRatingsTags = bsObj.find("p", {"class":"-fs16 -pts"}).get_text()
# print("Product: ", productName)
# print("Brand: ", productBrand)
# print("Current product price: ", currentProductPrice)
# print("Previous product price: ", previousProductPrice)
# # print(productDiscount)
# print(productStarRating)
# print(productTotalRatingsTags)

if len(productTotalRatingsTags) == 0:
    productTotalRatings = "No ratings"
else:
    productTotalRatings = re.sub("[^0-9]", "", productTotalRatingsTags[0])
productReviewsCountTags = bsObj.find_all("h2", {"class": "-fs14 -m -upp -ptm"})

# if len(productDiscount) == 0:
#     productDiscount = "No Discount"
# else:
#     productDiscount = re.sub("[^0-9]", "", productDiscount[0].get_text())

# try:
#     if productReviewTag.attrs['href'] is not None:
#         productReviewLink = urljoin(URL, productReviewTag["href"])
#     else:
#         productReviewLink = "No reviews"
# except KeyError:
#     productReviewLink = "No reviews"
#     pass
keys = ["productName", "productBrand", "currentProductPrice", "previousProductPrice",
             "productStarRating", "productTotalRatings", "productReviewsCount", "Round"]
values = [productName, productBrand, currentProductPrice, previousProductPrice,
            productStarRating, productTotalRatings, productReviewsCountTags]
productDict = dict(zip(keys, values))
print(productDict, "\n")



