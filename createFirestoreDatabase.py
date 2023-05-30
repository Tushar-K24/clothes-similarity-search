import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("./prepareDataFirebase/ServiceAccountKey.json")
app = firebase_admin.initialize_app(cred)

db = firestore.client()


def find(collection, id=None):
    if id is None:
        return db.collection(collection).stream()
    return db.collection(collection).document(id).get().to_dict()


def create(collection, id, data):
    assert isinstance(data, dict)
    doc_ref = db.collection(collection).document(str(id))
    doc_ref.set(data)


def update(collection, id, data):
    assert isinstance(data, dict)
    doc_ref = db.collection(collection).document(str(id))
    doc_ref.update(data)
