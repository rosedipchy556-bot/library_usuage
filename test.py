import requests

url = "https://httpbin.org/get"

response = requests.get(url, timeout=10)

print("Status Code:", response.status_code)
print("Response data:", response.json())