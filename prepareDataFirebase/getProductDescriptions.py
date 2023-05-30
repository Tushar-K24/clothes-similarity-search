import re
import json
from tqdm import tqdm
import js2py
from bs4 import BeautifulSoup
from .utils.getPage import getPage

baseUrl = "https://www2.hm.com/en_in/productpage.{productId}.html"
generalAttributes = ["alternate", "ageGender"]
specificAttributes = [
    "compositions",
    "description",
    "materialDetails",
    "detailedDescriptions",
]


def convertJS2JSON(jsObject):
    code = f"var isDesktop = true;\nvar productArticleDetails = {jsObject}\nJSON.stringify(productArticleDetails)"
    jsonString = js2py.eval_js(code)
    return jsonString


def extractProductDetail(productId):
    url = baseUrl.replace("{productId}", str(productId))
    htmlPage = getPage(url)
    soup = BeautifulSoup(htmlPage, "html.parser")
    product = soup.find(class_="product")

    # accessing javascript inside product
    script_tag = product.find("script")

    product_article_details = None

    if script_tag:
        # Get the JavaScript code within the script tag
        js_code = script_tag.string

        # Search for the variable assignment using regex
        pattern = r"var productArticleDetails = ({.*?});"
        match = re.search(pattern, js_code, re.DOTALL)

        if match:
            product_article_details = match.group(1)

    if product_article_details:
        # Convert the JavaScript variable to a Python dictionary
        product_article_details = convertJS2JSON(product_article_details)
        python_dict = json.loads(product_article_details)
        # print(python_dict)
        python_dict_refined = {"url": url}

        for att in generalAttributes:
            python_dict_refined[att] = python_dict[att] if att in python_dict else None

        for att in specificAttributes:
            python_dict_refined[att] = (
                python_dict[str(productId)][att]
                if att in python_dict[str(productId)]
                else None
            )

        return python_dict_refined

    return None


def getProductDescriptions(productIds):
    for id in tqdm(productIds.keys()):
        itemDesc = extractProductDetail(id)
        for key, value in itemDesc.items():
            productIds[id][key] = value

    return productIds


if __name__ == "__main__":
    getProductDescriptions()
