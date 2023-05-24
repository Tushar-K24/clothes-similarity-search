import requests

################## Request Parameters ##############################################################

payload = {}
headers = {
    "authority": "www2.hm.com",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
    "accept-language": "en-US,en;q=0.6",
    "cache-control": "max-age=0",
    "cookie": 'uuidCookie=eyJhbGciOiJkaXIiLCJlbmMiOiJBMTI4Q0JDLUhTMjU2In0..G1pSJczZuecv0ydDjLgfSQ.loBHj4hpflgB0jj8Ve_G9AdUzZoHyhVWQ5OE3Pbjo0M7XA84glEWl5todqF_fj0jwgmL6mMA-p9CR63mT2ogps7HB6oRtdj1pbf_nkOXPWCabwohDADPuQ8MJY0uASJTXuFHQMKPvydik28guuue4dCSV8__GNbEgW-r-_5844bix-KCNb1sEuBzZmE-GL8ZqAJk2IKXI9hPB_CJBmgt4fcVAmZ7GR0RDqpkITyQoS596pM5Io8PgD2jjnr36C4mq8_WjFMHMMA6_qX2QrlPS7Cg4LjhrnVB-H1z5EUMoWM.B97ux3-2k7UyAtDiKzMdsQ; agCookie=21a2c61b-fc2c-41f5-b0e0-b0e346fdaa14; hm-india-cart=ae596a8b-0467-4b09-9f98-0a7c3cbb8bf0; hm-india-favourites=""; akainst=APAC; AKA_A2=A; bm_sz=6C93CD4F0DC1F02463ABE9524B4C8328~YAAQrW0/F2yBwQiIAQAAUShzOBMKoIeARfIbaHlWhuTUaWgdIFbcavgcVb0MjhvEslYBl59/OlLWsilMc5wjfEeh+40g2jfaLd+HN28pt3l5jaPe8ThWMGMFw1X8G4eRcuoqHhUw0ISM+8XpftsuXPK6YWua0UY1ZuJdhjs9gVaoU2EuYgU2tFJ2h2ogkT7HN7ovIU/q4UdfTvRF4S1i9z0vHeWgJY+N13fiq7Q3tEWBFpBIiB1MsL0gfP6QoKSuNMsE3Q0qtkEXXcyLeMR1olgufBnVhyEXJeuW9XATXw==~3159602~3683376; _abck=A4B4D6A5E4E1ED07152935892634A9C0~0~YAAQrW0/F8uBwQiIAQAAMS1zOAmRAw6a5itiDs2zd6u/xGXvjtIp8g5jC1WrxOYqnUaQ93F5ZmRRUdUVnvu64vALWH/HrUdN3MIkoLokHndDA0v5ti9S530Ze0hnUNSpydo9KZg2CAqGCt682vmsSGuYeBT9bjky972qu+ah+g2Nmd4ObjHJCNXvhC6XPp5XCHfBATqU4aNbb5qMgTeCorlS2ClbirL8TVtKi7BeZuuV8uxN3G1gYlTfkURS7ATqkYhTYvbjwmXsp2wnRH0y6UgG3AOm1GJTMxOqITEttSs5uopGGjEFYXv5GMj8WiB3QUvwI6mFssGph30WgGx9FiB5Sm4JmZ/ZcOJC0KH4uC/DyoPXOZc/y8+jq5hs2qOseg7RDrMJaMmH8Zabt0/5Wv+mlU4=~-1~-1~1684577779; INGRESSCOOKIE=1684574253.302.515586.109677|7bbf721d92a09b08c42eb8596390c8cc; JSESSIONID=82A0831528532AEE26E163038483027B78A84A7AFE27C709E0AAD998E3892C53302BC1064BF1368E7B46CB3E9EA5A056461D93F1F2F66973499AABA4D1B09B6E.hybris-ecm-web-7bbd6ddd9-gcbnl; userCookie=##eyJjYXJ0Q291bnQiOjB9##; ak_bmsc=A57A6FB0F7EE48B505AB9493CC1F63A3~000000000000000000000000000000~YAAQrW0/F/OBwQiIAQAAFi9zOBOFWBA5TuB97TuVC10shAANeY39drKQE/qfkqa+KIG/h6EkudAgSFdKIh3ZiHXHZGKpzLthH/e+pH/ZYpba6kkoQqlyloYvfwVqA3OjbqDTcseTHsF2Kz3XsFcvu6RsY3GxjFNQtp1rgMkBh0UrSan/dyYpoNF4AYy12PBebDNWsLPqQUflZCvzHHGl/xUskOlwxp/08qxxIPG/d4SHXLd/HrsCzYGgrGR6CZZ8K1HOqtnKeQjggRb3n92Tn0zZJNhZXx5VMtsM0e5oi7We5w4i6FE+v0DDXvsVh5RJZNLN7lnVt2Ef4smN95gmZlFBSBTUNfvPLWkbLYOy2dCmaUDSvud82QUeG7tOR2BUezgXFKhjSiYs4dMWdMNAQBwk9zYPI003nR++6Vc7RUg59PAk75fQJto6AsdWY/cGzoFbRALqNruabP/JxbcuU9VxJnJ+3/z40AG1J7h8w7ksvQTRWOmsgA==; akamforef=en_in; akamfoneterror=18.8c6d3f17.1684576232.d7def68; utag_main=v_id:01883594658c0017567e9456a11a0406f002406700911$_sn:2$_se:119$_ss:0$_st:1684578070351$c_consent:groups%3DC0001%3A1%2CC0002%3A0%2CC0003%3A0%2CC0004%3A0$ses_id:1684574251600%3Bexp-session$_pn:14%3Bexp-session$ses_id_r:s_4703477004266732.1684574251600%3Bexp-session$segment:normal%3Bexp-session$cart_active:No%3Bexp-session$prevpage:%2FLADIES%2FSHOPBYPRODUCT%20%3A%20VIEWALL%2FVIEWALL%20%3A%20VIEWALL%2FVIEW_ALL%2FLadies%20%3A%20Shopbyproduct%20%3A%20Viewall%20%3A%20Viewall%3Bexp-1684579867955; akamref=en_in; akavpau_www2_en_in=1684576571~id=968c35115182eaad3bd61411c5076f57; bm_sv=1781052149CD8C5240D30CB4CCB32FA8~YAAQjG0/FzWxVR2IAQAAHRKSOBO+rpGa6TXTgEZG5T3QZQKNMyX3gBy4bjJNM5ab7EoqQhPHtVa5d331+jGGSTL3NZ188dB63xQ/F24gnSr7vWGA4cmB4PnjTcBdb3g97NP+S0sRfZLP14Dvpr2i9/wbaVeD42WxIO52sbJDBf6vI41r0pnNGjKUNi0yf3L9RKGwRklOxj4fZNgezHAZ/g08I9vJV4C5mrl06bj56yWgWHUQl2Qt5wTi+Cdw~1; _abck=A4B4D6A5E4E1ED07152935892634A9C0~-1~YAAQrW0/F6SUxQiIAQAA/NyUOAnTQc7yaTo4pRnf/JjGr5X9wPfC/eJOpf/HS8q4ZcK5nP+7iktXJXAmHqiLNbWbG0hZfgVcCVfh6gy8lKHlEXiRe+9sm5BcjjH9Uc7bIT3wdDwjQ5sztaNJ8wWJf6e1T+Q0qyStTlwNNDkQ4EhVyq5BpSPu02EUepEnbarFGc6QadVzkeWgS8IVZtiFL8FoFCfA7gY7SjfE+rEyd0sEMGvvfq9N1JbUsEKfBlgPLlzXr+DylChv8IrG8V/m/SOG7FJsrLZTWjIby7ImbOxTJ/rzZ7Wr72AavDqKAJvokZPZP9NjxFiuZ4ni0jEkaJ9QrZIjBQCvXQYls7U4yPSv/CuaOqtbpBxIvEU/NL3/Q6Zf7/cM+SFJ0yvHUSsRBfAzYrA=~0~-1~1684577779; bm_sv=1781052149CD8C5240D30CB4CCB32FA8~YAAQrW0/F6WUxQiIAQAA/NyUOBN+ndf2cBJOoZDrPhoolR+ORZsqZ3pqYL7MoSpqyq41USkl+sU3SGgMDWrvJmbDFjb/RkVnlsk58S+YexTlazD4QfecM9pM/VXmU23tpxoiLfuFWyVGppWn4wAOXtyBlBeXa7YQ99NTlWKU38aTt5CG2LcmQ0sBPFaJI5lfca3AZZaNwmZ2NR70uCC3Gdtz0PljjBEGfxiEx7tVfvAutmQ1UR95jX4Mc9zV~1; agCookie=21a2c61b-fc2c-41f5-b0e0-b0e346fdaa14; akainst=APAC; akamref=en_in; akavpau_www2_en_in=1684576760~id=fd337f804b88526d3b99ff9f28520b3b',
    "referer": "https://www2.hm.com/en_in/index.html",
    "sec-ch-ua": '"Brave";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "same-origin",
    "sec-fetch-user": "?1",
    "sec-gpc": "1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
}


def getPage(pageUrl):
    """
    returns HTML page for url->pageUrl
    """
    response = requests.request("GET", pageUrl, headers=headers, data=payload)
    html = response.text
    return html
