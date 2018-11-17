# -*- coding: utf-8 -*-
"""
Created on Sun Oct 21 16:36:10 2018

@author: dell
"""

#-------------part1， send request and return http response-
#way 1 - request
import requests
p="https://www.realtor.ca/map.aspx#ZoomLevel=12&LatitudeMax=53.5558904&LongitudeMax=-113.3795541&LatitudeMin=53.4288452&LongitudeMin=-113.7026208&CurrentPage=1&Sort=1-A&RecordsPerPage=9&PropertyTypeGroupID=1&PropertySearchTypeId=1&TransactionTypeId=2&PriceMin=0&PriceMax=0&BedRange=0-0&BathRange=0-0&Center=53.49241541577527%2C-113.54108746797965"
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134'}
r=requests.get(p,  headers=headers)
print(r.status_code)
#print (type(r.text))
print (r.text)

#way2 - urlopen
from bs4 import BeautifulSoup
#from urllib.request import urlopen
#TODO - need header
#html = urlopen(p).read()
#print (html)


#------------------part 2, extract or parse the http response text
#soup = BeautifulSoup(html, features='lxml')

#from lxml import html
#tree = html.fromstring(r.content)
#tree.path=
#
#print (tree)

soup = BeautifulSoup(r.text,'html.parser')
mydivs = soup.find_all("div", class_="smallListingCardPrice")

for div in mydivs: 
    print(type(div))
    print(div)
#soup = BeautifulSoup(r.text,"lxml")
#price = soup.find_all('div', 'smallListingCardPrice')
#print(type(price))
##print(str(price.count))
##print(price.index[0])
#for x in price:
#    print(x)
