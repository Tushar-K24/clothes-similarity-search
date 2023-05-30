import pandas as pd
from tqdm import tqdm
from prepareData.preprocessData import cleanText, selected_features
from .encoders import tfidf

# load encoder
encoder = tfidf.TFIDF()

# define filePath
filePath = "../productDetailsCleaned.csv"


def generateEncodingsFireStore(docs):
    """
    generates encodings and adds it to the fireStore db
    """
    productIds, corpus = [], []

    for doc in tqdm(docs.values()):
        productIds.append(doc["productId"])
        sent = ""
        for feature in selected_features:
            if isinstance(doc[feature], str):
                sent += doc[feature] + " "
            elif isinstance(doc[feature], list):
                sent += " ".join(doc[feature]) + " "
        corpus.append(cleanText(sent))

    # uncomment for bert
    # encoded = []
    # for sent in tqdm(corpus):
    #     encoded.append(encoder.encode(sent))

    # uncomment for tfidf
    encoded = encoder.fit(corpus)
    return encoded


def generateEncodings(df, save=False, fileName="encodings.csv"):
    """
    returns a pandas dataframe with encodings mapped to productIds

    input:

    df (DataFrame) -> contains productId and description text
    save (bool) -> if save = true, save the dataframe
    fileName (str) -> name of file if save = true

    """

    encoded_df = pd.DataFrame(columns=["productId", "encoded"])

    print("Generating encodings...")
    # uncomment for bert
    # for i in tqdm(range(len(df))):
    #     row = df.iloc[i]
    #     encoded = encoder.encode(row["cleaned_text"])
    #     encoded_df = encoded_df._append(
    #         {"productId": row["productId"], "encoded": encoded}, ignore_index=True
    #     )

    # uncomment for tfidf
    encoded = encoder.fit(list(df["cleaned_text"]))
    encoded_df = pd.DataFrame({"productId": df["productId"], "encoded": encoded})

    if save:
        print("Saving encodings...")
        encoded_df.to_csv(fileName, index=False)

    return encoded_df
