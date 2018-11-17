# -*- coding: utf-8 -*-
from urllib.request import urlopen, urlretrieve, quote
from urllib.parse import urljoin
from bs4 import BeautifulSoup

url = 'https://archive.org/details/EnglishPod/DailyLife-CoinsAndMoneyC0356Fl.mp3'
urlretrieve(url, "1.mp3")
#u = urlopen(url)


#try:
#    html = u.read().decode('utf-8')
#finally:
#    u.close()

