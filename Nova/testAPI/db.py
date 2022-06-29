# import numpy as np
# import pandas as pd
# import requests
# import json

# url = "https://zillow-com1.p.rapidapi.com/propertyExtendedSearch"

# querystring = {"location":"Whitby, Ontario, Canada","home_type":"Houses"}

# headers = {
# 	"X-RapidAPI-Key": "f859287662msh12f0d41ffd8368ap12a4bfjsn1b8661a3169f",
# 	"X-RapidAPI-Host": "zillow-com1.p.rapidapi.com"
# }

# response = requests.request("GET", url, headers=headers, params=querystring)

# response = response.json()
# pd.json_normalize(data=response['props'])


# print(response)


# # with open("save.txt", "r") as f:
# # 	props = f.readline()

# # props = props.split('"address":"')

# # print(props[0], "\n")
# # print(props[1], "\n")
# # print(props[2], "\n")


# # properties = pd.DataFrame(props)
# # print(properties)


