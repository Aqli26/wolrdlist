import requests

api_key= 'c855cfc8-6378-40e4-8de9-39a4215be420'
word = 'potato'
url = f'https://www.dictionaryapi.com/api/v3/references/collegiate/json/{word}?key={api_key}'

r = requests.get(url)
result = r.json()
print(result)