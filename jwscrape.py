import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
import requests
import datetime



baseLink = "https://wol.jw.org/en/wol/h/r1/lp-e/"
def getDailyText(getDate):
    link = baseLink + getDate
#print(link)
#link = "https://wol.jw.org/en/wol/h/r1/lp-e"
    try:
        result = requests.get(link)
        linkResult = result.content
        page = BeautifulSoup(linkResult, 'lxml')
    except HTTPError as httperror:
        print(httperror)
    except URLError as ue:
        print("The Server Could Not be Found")
    else:
        print("Parsing for date " + getDate)

    dailyText = page.find('div', attrs = {'class':'articlePositioner'})

    #navigationlinks = page.find('div', attrs = {'class':'resultNavControls'})

    #attrs{'class' : resultNavControls}

    scripture = dailyText.find_all('p', attrs = {'class':'themeScrp'})
    watchtowerComments = dailyText.find_all('p', attrs = {'class':'sb'})

    #previousDaylink = navigationlinks.find('a', attrs = {'aria-label':'previous day'}).get("href")
    scriptureem = scripture[1].find_all('em')


    for comments in scriptureem:
        print(comments.get_text())
        print("\n" + "end of comment" + "\n")

    #print(scripture[1].em.get_text())
    #print(scripture[1].em.[1].get_text())
    print ("\n")
    #print(watchtowerComments[1].get_text())
#'{dt.year}/{dt.month}/{dt.day}'.format(dt = mydate)

def __init__(self,):
    fromDate = datetime.strptime(input("Please enter from date in yyyy/dd/mm : "),'%Y/%m/%d')
    toDate = datetime.strptime(input("Please enter to date in yyyy/dd/mm : "), '%Y/%m/%d')
    outputFile = input("Please Enter output file name : ")

    if( fromDate > toDate):
        print ("ERROR: From Date cannot be greater than to date")
        exit(1)
    else:
        scrapedate = fromDate
        dfDailyText = pd.Dataframe()
        while scrapedate <= toDate:
            getDailyText(scrapedate)


