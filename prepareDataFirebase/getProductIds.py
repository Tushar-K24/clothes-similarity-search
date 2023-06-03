from tqdm import tqdm
from bs4 import BeautifulSoup
from .utils.getPage import getPage
from .utils.config import *

#################### Global Variables #######################################################

filters = "?sort=stock&image-size=small&image=model&offset={offset}&page-size={pagesize}".replace(
    "{pagesize}", str(pagesize)
)


def getTotalArticles(htmlPage):
    """
    returns the total count of products
    """
    soup = BeautifulSoup(htmlPage, "html.parser")
    totalArticles = int(soup.find(class_="load-more-heading")["data-total"])
    return totalArticles


def getItemDetails(htmlPage):
    """
    returns all the product ids and corresponding images available on htmlPage
    """
    ids, imageLinks, prices = [], [], []
    soup = BeautifulSoup(htmlPage, "html.parser")
    for product_item in soup.find_all(class_="hm-product-item"):
        itemLink = product_item.a.get("href")
        imageLink = product_item.img["data-src"]
        price = product_item.find(class_="item-price").text
        ids.append(itemLink[19:-5])
        imageLinks.append(imageLink)
        prices.append(price)
    return ids, imageLinks, prices


def getProductIds():
    """
    returns all clothing article ids after scraping from hm store and update it to fireStore database
    """
    productIds = {}

    # extract product links for every category
    for categoryDict in categories:
        category = categoryDict["category"]
        subcategory = categoryDict["subcategory"]

        articleIds, articleImageLinks, articlePrices = [], [], []

        relUrl_ = relUrl.replace("{category}", category).replace(
            "{subcategory}", subcategory
        )

        # extract the total count of articles present in this category
        htmlPage = getPage(baseUrl + relUrl_)
        totalCount = getTotalArticles(htmlPage)

        print(f"Category: {category}, subcategory: {subcategory}, total: {totalCount}")

        # extract links in batches of pagesize
        for offset in tqdm(range(0, totalCount, pagesize)):
            filters_ = filters.replace("{offset}", str(offset))
            htmlPage = getPage(baseUrl + relUrl_ + filters_)
            ids, imageLinks, prices = getItemDetails(htmlPage)
            articleIds.extend(ids)
            articleImageLinks.extend(imageLinks)
            articlePrices.extend(prices)

        # update the fireStore database
        print("Creating collection...")
        for id, imageLink, price in tqdm(
            zip(articleIds, articleImageLinks, articlePrices)
        ):
            # check if product id already exists

            if id in productIds:
                productIds[id]["category"].append(f"{category}/{subcategory}")
            else:
                productIds[id] = {
                    "productId": id,
                    "imageUrl": imageLink,
                    "price": price,
                    "category": [f"{category}/{subcategory}"],
                }

    return productIds


if __name__ == "__main__":
    getProductIds()
