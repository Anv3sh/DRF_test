import requests


# endpoint = "http://httpbin.org/anything"
# endpoint = "https://www.github.com"
endpoint = "http://127.0.0.1:8000/api/"


response = requests.post(endpoint,json={"title":"Hello world"})
print(response.json())
print(response.status_code)