import requests
from .requestHeaderData import headers, payload

################## Request Parameters ##############################################################


def getPage(pageUrl):
    """
    returns HTML page for url->pageUrl
    """
    response = requests.request("GET", pageUrl, headers=headers, data=payload)
    html = response.text
    return html
