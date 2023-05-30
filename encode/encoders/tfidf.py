from os.path import exists

import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
import nltk

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

nltk.download("stopwords")
nltk.download("punkt")
nltk.download("wordnet")
nltk.download("omw-1.4")


class TFIDF:
    def __init__(self, max_features=1000, ngram_range=(1, 1)):
        self.name = "tfidf.sav"
        self.tfidf = TfidfVectorizer(max_features=max_features, ngram_range=ngram_range)
        self.lemmatizer = WordNetLemmatizer()
        stop_words = stopwords.words("english")
        product_words = ["product", "shop"]
        self.stop_words = list(set(stop_words + product_words))

    def processText(self, txt):
        word_tokens = word_tokenize(txt)
        filtered_sent = [
            self.lemmatizer.lemmatize(word)
            for word in word_tokens
            if (word not in self.stop_words) and (len(word) > 2)
        ]
        return " ".join(filtered_sent)

    def fit(self, corpus):
        assert isinstance(corpus, list), "Entered corpus must be a list"

        cleaned_corpus = []
        for sent in corpus:
            assert isinstance(sent, str), "Entered sentence must be a sentence"
            sent = self.processText(sent)
            cleaned_corpus.append(sent)

        encodings = self.tfidf.fit_transform(cleaned_corpus)

        # save trained encoder
        pickle.dump(self.tfidf, open(self.name, "wb"))
        return encodings.todense().tolist()

    def encode(self, sent):
        # check if vectorizer exists
        assert exists(self.name), "You must fit the model first"

        # load the vectorizer
        self.tfidf = pickle.load(open(self.name, "rb"))

        # clean text for encoding
        assert isinstance(sent, str), "Entered sentence must be a sentence"
        sent = self.processText(sent)

        encoding = self.tfidf.transform([sent])

        return encoding.todense().tolist()
