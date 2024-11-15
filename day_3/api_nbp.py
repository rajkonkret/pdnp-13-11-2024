import requests

# pip install requests - instalacja w terminalu
url = 'https://api.nbp.pl/api/exchangerates/rates/A/usd/'

# HTTP GET
response = requests.get(url)
print(response)
# <Response [200]> 200 ok
# 3xx - przekierowania, warningi
# 4xx - 404 - braak strony, 400 Bad Request błedne dane w zapytaniu
# 5xx - błędy po stronie serwera

print(response.text)
print(type(response.text))  # <class 'str'>
data = response.json()
print(type(data))  # <class 'dict'>
print(data)
# {'table': 'A', 'currency': 'dolar amerykański', 'code': 'USD',
# 'rates': [{'no': '222/A/NBP/2024', 'effectiveDate': '2024-11-15', 'mid': 4.0898}]}
print(data['currency'])  # dolar amerykański
print(data['rates'][0]['mid'])  # 4.0898
