import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
import requests



baselink = "https://wol.jw.org"
variablelink = "/en/wol/h/r1/lp-e/2023/4/3"
link = baselink + variablelink
print(link)
#link = "https://wol.jw.org/en/wol/h/r1/lp-e"
result = requests.get(link)
linkResult = result.content
page = BeautifulSoup(linkResult, 'lxml')

dailyText = page.find('div', attrs = {'class':'articlePositioner'})

navigationlinks = page.find('div', attrs = {'class':'resultNavControls'})

#attrs{'class' : resultNavControls}

scripture = dailyText.find_all('p', attrs = {'class':'themeScrp'})
watchtowerComments = dailyText.find_all('p', attrs = {'class':'sb'})

previousDaylink = navigationlinks.find('a', attrs = {'aria-label':'previous day'}).get("href")
print(scripture[1].em.get_text())
#print(scripture[1].em.[1].get_text())
print ("\n")
print(watchtowerComments[1].get_text())

'''
for comments in watchtowerComments:
    print(comments.get_text())
    print("\n" + "end of comment" + "\n")
'''

#print(watchtowerComments[1].get_text())
print("\n\nspace \n\n")
print(dailyText)
