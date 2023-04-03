import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
import requests



baselink = "https://wol.jw.org/"
link = "https://wol.jw.org/en/wol/h/r1/lp-e"
result = requests.get(link)
linkResult = result.content
page = BeautifulSoup(linkResult, 'lxml')

dayTag = page.find('div', attrs = {'class':'articlePositioner'})

navigationlinks = page.find('div', attrs = {'class':'resultNavControls'})

#attrs{'class' : resultNavControls}

previousDaylink = navigationlinks.find('a', attrs = {'aria-label':'previous day'}).get("href")
print(previousDaylink)
print("\n\nspace \n\n")
print(dayTag)
