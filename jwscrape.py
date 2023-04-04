
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
import requests
#import datetime
from datetime import datetime, timedelta, date


dfDailyText = pd.DataFrame(columns=['date','scripture','comments'])
baseLink = "https://wol.jw.org/en/wol/h/r1/lp-e/"
def getDailyText(getDate, dfDailyText):
    linkDate = '{dt.year}/{dt.month}/{dt.day}'.format(dt = getDate)
    link = baseLink + linkDate
    try:
        result = requests.get(link)
        linkResult = result.content
        page = BeautifulSoup(linkResult, 'lxml')
    except HTTPError as httperror:
        print(httperror)
    except URLError as ue:
        print("The Server Could Not be Found")
    else:
        print("Parsing for date " + getDate.strftime('%Y/%m/%d'))

    dailyText = page.find('div', attrs = {'class':'articlePositioner'})

    scripture = dailyText.find_all('p', attrs = {'class':'themeScrp'})
    watchtowerComments = dailyText.find_all('p', attrs = {'class':'sb'})

    #previousDaylink = navigationlinks.find('a', attrs = {'aria-label':'previous day'}).get("href")
    scriptureem = scripture[1].find_all('em')

    scriptureString = ""
    #scriptureString
    for comments in scriptureem:
        scriptureString += str(comments.get_text())
        #print(comments.get_text())
    #print("\n scripture is " + scriptureString)    
    wComments = watchtowerComments[1].get_text()
    row = pd.Series([getDate, scriptureString, wComments], index=dfDailyText.columns)
    dfDailyText = dfDailyText.append(row, ignore_index=True)
    #dfDailyText = pd.concat([dfDailyText, row])
    print("Finished date " + getDate.strftime('%Y/%m/%d'))
    #print(dfDailyText.head())
    return (dfDailyText)


    #print(scripture[1].em.get_text())
    #print(scripture[1].em.[1].get_text())
    #print ("\n")
    #print(watchtowerComments[1].get_text())
#'{dt.year}/{dt.month}/{dt.day}'.format(dt = mydate)


#fromDate = datetime.strptime(input("Please enter from date in yyyy/mm/dd : "),'%Y/%m/%d')
#toDate = datetime.strptime(input("Please enter to date in yyyy/mm/dd : "), '%Y/%m/%d')
fromDate = datetime.strptime("2023/04/01",'%Y/%m/%d')
toDate = datetime.strptime("2023/04/04",'%Y/%m/%d')
#outputFile = input("Please Enter output file name : ")
#toDate =+ timedelta(days=1)
if( fromDate > toDate):
    print ("ERROR: From Date cannot be greater than to date")
    exit(1)
else:
    scrapedate = fromDate
    
    i = 0
    while scrapedate <= toDate:
        dfDailyText = getDailyText(scrapedate, dfDailyText)
        scrapedate += timedelta(days=1)
        # write to file after every 30 iterations
        if ((i % 30) == 0):
            dfDailyText.to_excel("dailytxt.xlsx",index = False)
        i += 1
    
    dfDailyText.to_excel("dailytxt.xlsx",index = False)
    print(str(i)+ " records collected.")
    exit(0)


