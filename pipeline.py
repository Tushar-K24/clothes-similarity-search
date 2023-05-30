from tqdm import tqdm
import pickle
from prepareDataFirebase.pipeline import getProducts
from encode.generateEncodings import generateEncodingsFireStore
from createFirestoreDatabase import create


if __name__ == "__main__":
    collection = "products"

    productDescriptions = getProducts()
    # with open("productDescriptionsScraped.pkl", "wb") as f:
    #     pickle.dump(productDescriptions, f)
    #     print("dictionary saved")

    with open("productDescriptionsScraped.pkl", "rb") as f:
        productDescriptions = pickle.load(f)

    encodings = generateEncodingsFireStore(productDescriptions)

    assert len(productDescriptions) == len(encodings)

    print("Adding encodings to the documents...")
    for idx, pid in tqdm(enumerate(productDescriptions.keys())):
        productDescriptions[pid]["encoded"] = encodings[idx]

    with open("productDescriptions.pkl", "wb") as f:
        pickle.dump(productDescriptions, f)
        print("dictionary saved")

    print("Creating fireStore Database")
    for pid in tqdm(productDescriptions.keys()):
        create(collection, pid, productDescriptions[pid])
