import pandas as pd
import requests
from bs4 import BeautifulSoup

#it give all the HTML codes in the URL
page = requests.get('https://forecast.weather.gov/MapClick.php?lat=42.8049&lon=-88.1716#.XvtvWigzZPY')
soup = BeautifulSoup(page.content ,'html.parser')
#print(soup)

#gives only that part of the HTML code
week = soup.find(id = 'seven-day-forecast')
#print(week)

#prints one week day's forecast
#print(week.find_all(class_='forecast-tombstone'))

#printing one tombstone container
items = week.find_all(class_='tombstone-container')
#print(items)
#print(items[0])

print(items[0].find(class_='period-name').get_text())
print(items[0].find(class_='short-desc').get_text())
print(items[0].find(class_='temp').get_text())

period_names = [items.find(class_='period-name').get_text() for items in items]
descriptions = [items.find(class_='short-desc').get_text() for items in items]
temperaturs =  [items.find(class_='temp').get_text() for items in items]
print(descriptions)
print(temperaturs)
print(period_names)

#using pandas

weather_stuff = pd.DataFrame(
    {
        'period': period_names,
        'descriptions': descriptions,
        'temperature': temperaturs,
    })
print(weather_stuff)

weather_stuff.to_csv('weather.csv')
