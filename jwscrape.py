import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
import requests



baselink = "https://wol.jw.org/"
link = "https://wol.jw.org/en/wol/h/r1/lp-e"
result = requests.get(link)
linkResult = result.content
page = BeautifulSoup(linkResult, 'lxml')

wrapper = page.find('div')
#attrs{'class' : resultNavControls}

previousDaylink = page.find('a', attrs = {'caria-label':'previous day'})

print(previousDaylink)
