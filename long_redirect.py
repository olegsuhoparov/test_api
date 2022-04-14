import requests

payload = {"login": "secret_login", "password": "secret_pass"}


res = requests.get("https://playground.learnqa.ru/api/long_redirect")
redirects = res.history
last_url = res.url
print(len(redirects), last_url)
