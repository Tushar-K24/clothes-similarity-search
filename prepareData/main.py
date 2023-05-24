from extractClothingArticleIds import extractClothingArticleIds
from extractItemDescriptions import extractItemDescriptions
from preprocessData import generateProductDescription

if __name__ == "__main__":
    clothingArticleIds = extractClothingArticleIds()
    productDetails = extractItemDescriptions(
        clothingArticleIds, save=True, fileName="../productDetails.csv"
    )

    # replace null values, if any, with empty strings
    productDetails.fillna("", inplace=True)

    productDetails["cleaned_text"] = generateProductDescription(productDetails)

    # save product details
    productDetails.to_csv("../productDetailsCleaned.csv", index=False)
