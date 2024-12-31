#What is an API? It can be a safer way to get ahold of data. The data is already packaged somewhat for you to retrieve.
#
# Requests module is not an API but lets you retrieve web data through html requests

import requests

url = "https://wwww.rutgers.edu/"
response = requests.get(url)
print(response.text)

# JSON is a popular format to send/retrieve data through APIs

# load command converts JSON string to Python object
# dump command does the exact opposite

url = "http://api.open-notify.org/astros.json"

response = requests.get(url)
content = response.json()
print(f"The number of people in space is {content['number']}")

# usually APIs require you to enter an API key to access the information in your code
# NYT has a lot of APIs you can choose from for the final project

# Final project will have you use the API to answer a researc question using ETL
# Extraction: Extract data relevant to research question
# Transformation: Analyze data that was extracted to answer question
# Loading: Upload or save the newly transformed data in a readable format (txt, csv, image, pdf)
url = "path to api url"
API_KEY = "jfdfdfjjdfdjfjdfdfdfj"  # since this is a constant variable, we put it in all caps.
params = {"query":"programming", "api-key":API_KEY}
response = requests.get(url, params=params)
content = response.json()
print(f"{content['response']['meta']['hits']}") # or content.keys()



