from .getProductIds import getProductIds
from .getProductDescriptions import getProductDescriptions


def getProducts():
    productIds = getProductIds()

    productDetails = getProductDescriptions(productIds)
    return productDetails
