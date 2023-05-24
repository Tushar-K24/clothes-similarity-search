import re
from tqdm import tqdm


def cleanText(sent):
    sent = sent.lower()  # lowercase the sentence
    sent = re.sub("{alternatecolor}", " ", sent)
    # sent = re.sub(r"[^a-zA-Z0-9 ,.-|]", " ", sent)  # remove special characters
    sent = re.sub(r"[^a-zA-Z ]", " ", sent)  # remove special characters
    sent = re.sub(r"[\[\]\(\)\{\}]", " ", sent)  # remove patenthesis
    sent = re.sub(" +", " ", sent)  # remove additional spaces
    return sent


def generateProductDescription(df):
    # features to be selected for generating product encodings
    selected_features = [
        "description",
        "detailedDescriptions",
        "compositions",
        "category",
        "subcategory",
        "ageGender",
        "alternate",
        # "materialDetails",
    ]

    cleaned_corpus = []
    print("Cleaning text...")
    for i in tqdm(range(len(df))):
        row = df.iloc[i]
        txt = ""
        for feature in selected_features:
            txt += row[feature] + "."
        txt = cleanText(txt)
        cleaned_corpus.append(txt)

    return cleaned_corpus
