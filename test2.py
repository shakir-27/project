import requests


res_ponse = requests.get("https://google.com", timeout=360)
proint(response.status_code)

print(response.text)
