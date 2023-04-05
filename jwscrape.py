import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
import requests
from datetime import datetime, timedelta, date

#global variables
dfDailyText = pd.DataFrame(columns=['date','scripture','comments'])
baseLink = "https://wol.jw.org/en/wol/h/r1/lp-e/"

# function or method that takes the date and dataframe to append it fetches and appends for tthe date given
def getDailyText(getDate, dfDailyText):
    linkDate = '{dt.year}/{dt.month}/{dt.day}'.format(dt = getDate) #converts the date to the link format removing zeros
    link = baseLink + linkDate
    #The actual request
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

    dailyText = page.find('div', attrs = {'class':'articlePositioner'}) #locating the actual dailytext

    scripture = dailyText.find_all('p', attrs = {'class':'themeScrp'}) 
    watchtowerComments = dailyText.find_all('p', attrs = {'class':'sb'})
    #scripture has 2 parts the scripture text and quotation
    scriptureem = scripture[1].find_all('em')
    
    scriptureString = ""
    for comments in scriptureem:
        scriptureString += str(comments.get_text())
    #picking comments for the day        
    wComments = watchtowerComments[1].get_text()
    #appending the data for the day on the dataframe using append() causes warning
    row = pd.Series([getDate, scriptureString, wComments], index=dfDailyText.columns)
    dfDailyText = dfDailyText.append(row, ignore_index=True)
    print("Finished date " + getDate.strftime('%Y/%m/%d')) #alert that date has been parsed
    return (dfDailyText)


#code starts running from below
#date range is defined here
fromDate = datetime.strptime("2023/04/01",'%Y/%m/%d')
toDate = datetime.strptime("2023/04/04",'%Y/%m/%d')

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


