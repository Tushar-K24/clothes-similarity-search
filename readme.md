# Clothing Similarity Search

Clothes similarity search provides ranked recommendations based on the description of the clothing provided from the database. This repository contains the source code for:

- Data Scraper
- Sentence Encoder
- Similarity Function

### Data Scraper

**Data scraper** makes use of the data available on [H&M website](https://www2.hm.com/en_in/index.html).

The scraped data is further feature-engineered and preprocessed to generate a wordSoup for representational encoding and is stored in the column _cleaned_text_

### Encoder

**Encoder** uses Tfidf-Vectorizer to generate sentence embeddings for every product description of size _1 x MAX_FEATURES_ _(default = 1000)_.

The tf-idf encoded data is hosted on a cloud bucket for public access at

***https://storage.googleapis.com/product-encodings/encodings.csv***

### Similarity Function

**Similarity Function** utilizes cosine similarity by _scikit-learn_ to generate a similarity measure between the **product description** and the **database** and provide n-ranked results to the user.

## Function Description

The **similarity function** takes 2 arguments as parameters:

- description(required): _description of the clothing article_
- limit(optional): _no. of clothing articles to return, default = 10_.

Returns a json in the following format:

```
{
    "similarItems": ["List of urls"]
}
```

## Installation

To use util functions and scripts such as _the scraper_ and _the encoders_, clone this repository to your local environment to get started:

```
git clone https://github.com/Tushar-K24/clothes-similarity-search.git
```

After creating a virtual environment in the cloned repository, install the dependencies as:

```
pip install -r requirements-script.txt
```

## Cloud Function Testing

- ![image](https://github.com/Tushar-K24/clothes-similarity-search/assets/62638544/2ae6651b-5a43-4878-ab3e-bc34dd9484c9)

- ![image](https://github.com/Tushar-K24/clothes-similarity-search/assets/62638544/783926ba-2840-4eb8-911f-52a93920b9f5)
