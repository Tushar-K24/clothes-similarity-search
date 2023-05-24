import re
import json
from tqdm import tqdm
import pandas as pd
import js2py
from bs4 import BeautifulSoup
from utils.getPage import getPage

baseUrl = "https://www2.hm.com/en_in/productpage.{productId}.html"
generalAttributes = ["alternate", "ageGender", "materialDetails"]
specificAttributes = ["compositions", "description", "detailedDescriptions"]


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
        python_dict_refined = {}

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


def extractItemDescriptions(df, save=False, fileName="productDetails.csv"):
    columns = generalAttributes + specificAttributes + list(df.columns)
    productDetails = pd.DataFrame(columns=columns)

    # extract item details for every product ID
    for i in tqdm(range(len(df))):
        try:
            item_dict = extractProductDetail(df.iloc[i]["productId"])
            item_dict["productId"] = df.iloc[i]["productId"]
            item_dict["category"] = df.iloc[i]["category"]
            item_dict["subcategory"] = df.iloc[i]["subcategory"]
            item_dict["imgUrl"] = df.iloc[i]["imgUrl"]

            productDetails = productDetails._append(item_dict, ignore_index=True)
        except:
            print(df.iloc[i]["productId"])

    if save:
        # Save produceDetails to csv
        productDetails.to_csv(fileName, index=False)

    return productDetails


if __name__ == "__main__":
    df = pd.read_csv("clothingArticleIds.csv", index=False, dtype=str)
    extractItemDescriptions(df, save=True)
