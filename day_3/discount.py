from datetime import date, datetime, timedelta

today = date.today()
print(today)
print(type(today))
# 2024-11-15
# <class 'datetime.date'>

time = datetime.now()
print("Aktualny czas:", time)  # Aktualny czas: 2024-11-15 09:40:45.780544

# tomorrow = today + 1 # TypeError: unsupported operand type(s) for +: 'datetime.date' and 'int'
#  days=0, seconds=0, microseconds=0,
#                 milliseconds=0, minutes=0, hours=0, weeks=0
tomorrow = today + timedelta(days=1)
print("Jutro będzie", tomorrow)  # Jutro będzie 2024-11-16

formatted_date = datetime.now().strftime("%d/%m/%Y")
print(formatted_date)  # 15/11/2024
print(type(formatted_date))  # <class 'str'>

formatted_time = datetime.now().strftime("%H:%M")
print(formatted_time)  # 09:45

# wypisac w formacie 12 h do domu

# zamiana stringa na obiekt datatime.data
data_object = datetime.strptime("15/11/2024", "%d/%m/%Y")
print(data_object)  # 2024-11-15 00:00:00
print(type(data_object))  # <class 'datetime.datetime'>

products = [
    {'sku': 1, 'exp_date': today, 'price': 100},
    {'sku': 2, 'exp_date': today, 'price': 200},
    {'sku': 3, 'exp_date': tomorrow, 'price': 500},
    {'sku': 4, 'exp_date': today, 'price': 100.00},
]

# print(products)
for i in products:
    # print(i)  # {'sku': 1, 'exp_date': datetime.date(2024, 11, 15), 'price': 100}
    # print(i['exp_date'])
    if i['exp_date'] != today:
        continue  # wraca na początek pętli, bierze kolejny element

    i['price'] *= 0.8  # price = price * 0.8
    print(f"""Price for sku {i['sku']}
is now {i['price']}""")
# Price for sku 1
# is now 80.0
# Price for sku 2
# is now 160.0
# Price for sku 4
# is now 80.0
