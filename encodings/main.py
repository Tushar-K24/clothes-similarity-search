import pandas as pd
from tqdm import tqdm

from encoders import tfidf

# load encoder
encoder = tfidf.TFIDF()

# define filePath
filePath = "../productDetailsCleaned.csv"


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


if __name__ == "__main__":
    df = pd.read_csv(filePath, dtype=str)
    generateEncodings(df, save=True, fileName="../encodings.csv")
