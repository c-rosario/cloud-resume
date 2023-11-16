import requests

url = "https://jhln209u2i.execute-api.us-east-1.amazonaws.com/default/visitors"
response = requests.get(url)
print(response.text)
