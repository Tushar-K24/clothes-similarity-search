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

### Similarity Function

**Similarity Function** utilizes cosine similarity by _scikit-learn_ to generate a similarity measure between the **product description** and the **database** and provide n-ranked results to the user.

The similarity function can be accessed by making a post request

Node.js

```
const axios = require('axios');
let data = JSON.stringify({
  "description": "a white hat made of cotton",
  "limit": 5
});

let config = {
  method: 'post',
  maxBodyLength: Infinity,
  url: 'https://asia-south1-clothes-similarity.cloudfunctions.net/clothes-similarity-noauth',
  headers: {
    'Content-Type': 'application/json'
  },
  data : data
};

axios.request(config)
.then((response) => {
  console.log(JSON.stringify(response.data));
})
.catch((error) => {
  console.log(error);
});
```

## Function Description

The **similarity function** takes 2 arguments as parameters:

- description(required): _description of the clothing article_
- limit(optional): _no. of clothing articles to return, default = 10_.

Returns a json in the following format:

```
{
    "similarItems": ["list of product descriptions(in json)"]
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

## Product Recommendation UI

A simple interactive user-interface for the same function can be accessed from this [link](https://hm-product-recommendations.netlify.app/)
