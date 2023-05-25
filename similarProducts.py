import ast
import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# from encoders.bert import BERT
from encode.encoders.tfidf import TFIDF


# initialize product encodings
print("reading encodings...")
df = pd.read_csv("encodings.csv", dtype=str)
encoded_products = df["encoded"].apply(ast.literal_eval)

print("generating encoding matrix...")
encoding_matrix = np.array(list(encoded_products))

# initialize encoder
# encoder = BERT()
print("loading encoder...")
encoder = TFIDF()


def findSimilarity(description):
    """
    Output:
    returns similarity measure for every product in the database with the description

    Input:
    description(str) -> product description
    """

    encoding = encoder.encode(description)
    similarity = cosine_similarity(encoding, encoding_matrix)

    # sort similarity indices from high to low
    similarity = similarity[0].argsort()[::-1]

    return similarity


def findSimilarItems(description, num=10):
    """
    Output:
    return url for top "num" most relevent products that matches the description

    Input:
    description(str) -> product description
    num(int) -> number of links to be returned
    """
    base_url = "https://www2.hm.com/en_in/productpage.{productId}.html"

    # url generator from productId
    generateUrl = lambda productId: base_url.replace("{productId}", str(productId))

    # similarity vector
    indices = findSimilarity(description)

    added_product = set()

    url_list = []

    productIds = df["productId"].iloc[indices]

    for productId in productIds:
        if len(url_list) == num:
            break
        if productId not in added_product:
            added_product.add(productId)
            url_list.append(generateUrl(productId))

    return {"similarItems": url_list}


print("function is ready!")
