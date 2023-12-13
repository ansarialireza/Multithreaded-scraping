import re
import requests
from bs4 import BeautifulSoup
import mysql.connector

def useRegex(input):
    pattern = re.compile(r"(\d*,*\d* miles)", re.IGNORECASE)
    return pattern.match(input)

price_list = []
mile_list = []

model = input("Enter model example( bmw , jeep ,ford,...) : ")
url = 'https://www.truecar.com/used-cars-for-sale/listings/%s/location-new-york-ny/' % model
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
price = soup.find_all('div', attrs={'class': 'heading-3 my-1 font-bold'})
mile = soup.find_all('div', attrs={'class': 'truncate text-xs'})

for item in mile:
    if useRegex(item.text):
        mile_list.append(item.text)
for item in price:
    price_list.append(item.text)

# Add print statements to debug
print("Length of mile_list:", len(mile_list))
print("Length of price_list:", len(price_list))

cars = {}
for i in range(min(20, len(mile_list), len(price_list))):
    cars.update({mile_list[i]: price_list[i]})

for k, v in cars.items():
    print(v, k)

# mydb = mysql.connector.connect(host='127.0.0.1', user='root', password='8569')
# mycursor = mydb.cursor()
# mycursor.execute('DROP DATABASE IF EXISTS CARS')
# mycursor.execute('CREATE DATABASE CARS')
# mycursor.execute('USE CARS')
# mycursor.execute('CREATE TABLE selers (price text, mileage text)')
# SQL = 'INSERT INTO selers (price, mileage) VALUES (%s, %s)'

# for k, v in cars.items():
#     mycursor.execute(SQL, (v, k))

# mydb.commit()
