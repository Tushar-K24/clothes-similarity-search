from tqdm import tqdm
import pandas as pd
from bs4 import BeautifulSoup
from utils.getPage import getPage

#################### Global Variables #######################################################
categories = [
    {"category": "women", "subcategory": "shop-by-product"},
    {"category": "men", "subcategory": "shop-by-product"},
    {"category": "divided", "subcategory": "shop-by-product"},
    {"category": "baby", "subcategory": "newborn"},
    {"category": "baby", "subcategory": "girls"},
    {"category": "baby", "subcategory": "boys"},
    {"category": "baby", "subcategory": "products"},
    {"category": "sport", "subcategory": "women"},
    {"category": "sport", "subcategory": "men"},
    {"category": "sport", "subcategory": "kids"},
]
pagesize = 100

baseUrl = "https://www2.hm.com"
relUrl = "/en_in/{category}/{subcategory}/view-all.html"
filters = "?sort=stock&image-size=small&image=model&offset={offset}&page-size={pagesize}".replace(
    "{pagesize}", str(pagesize)
)


def getTotalArticles(htmlPage):
    """
    returns the total count of products
    """
    soup = BeautifulSoup(htmlPage, "html.parser")
    return int(soup.find(class_="load-more-heading")["data-total"])


def getItemDetails(htmlPage):
    """
    returns all the product ids and corresponding images available on htmlPage
    """
    Ids, imageLinks = [], []
    soup = BeautifulSoup(htmlPage, "html.parser")
    for product_item in soup.find_all(class_="hm-product-item"):
        itemLink = product_item.a.get("href")
        imageLink = product_item.img["data-src"]
        Ids.append(itemLink[19:-5])
        imageLinks.append(imageLink)
    return Ids, imageLinks


def extractClothingArticleIds(save=False, fileName="clothingArticleIds.csv"):
    """
    returns all clothing article ids after scraping from hm store and returns as a dataframe
    """
    # extract product links for every category
    clothingArticleIds = pd.DataFrame(
        columns=["category", "subcategory", "imgUrl", "productId"]
    )

    for categoryDict in categories:
        category = categoryDict["category"]
        subcategory = categoryDict["subcategory"]

        articleIds, articleImageLinks = [], []

        relUrl_ = relUrl.replace("{category}", category).replace(
            "{subcategory}", subcategory
        )

        # extract the total count of articles present in this category
        totalCount = getTotalArticles(getPage(baseUrl + relUrl_))

        print(f"Category: {category}, subcategory: {subcategory}, total: {totalCount}")

        # extract links in batches of pagesize
        for offset in tqdm(range(0, totalCount, pagesize)):
            filters_ = filters.replace("{offset}", str(offset))
            htmlPage = getPage(baseUrl + relUrl_ + filters_)
            ids, imageLinks = getItemDetails(htmlPage)
            articleIds.extend(ids)
            articleImageLinks.extend(imageLinks)

        # append to global dataframe
        clothingArticleIds = clothingArticleIds._append(
            pd.DataFrame(
                {
                    "category": category,
                    "subcategory": subcategory,
                    "productId": articleIds,
                    "imgUrl": articleImageLinks,
                }
            )
        )

    # Remove dupicate entries from table
    clothingArticleIds.drop_duplicates(inplace=True)

    if save:
        # save article links as csv
        clothingArticleIds.to_csv(fileName, index=False)

    return clothingArticleIds


if __name__ == "__main__":
    extractClothingArticleIds(save=True)
