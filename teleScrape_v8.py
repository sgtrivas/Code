#import urllib.request
import requests as req
#from pprint import pprint
from html_table_parser.parser import HTMLTableParser
import pandas as pd
from bs4 import BeautifulSoup
import datetime


def contents(link):

    #  opens website and reads it
    #  binary contents (http Response Body)

    # making request to site

    #response = req.
    #global response
    response = req.get(link)
    # f = urllib.request.urlopen(response)
    # print(f)
    soup = BeautifulSoup(response.content, "html.parser")
    #print(soup)
    global ans
    ans = hyper_links(soup)
    return soup

def hyper_links(soup):
    #soup = BeautifulSoup(content, "html.parser")
    tables = soup.find_all("table")  # Find all tables on the page
    hyper = []
    for table in tables:
        rows = table.find_all("tr")  # Find all rows in the table
        for row in rows:
            link = row.find("a")  # Find the first link in the row
            if link:
                global channel_name, channel_url
                channel_name = link.text
                channel_url = link["href"]
                hype = channel_name + ' = '+ f'https://telemetr.io{channel_url}'
                hyper.append(hype)
                
                #global ans
                #print(f"{channel_name} - {channel_url}")
                #print(hyper)
    hyper.append(' ')        
    return hyper               
    
linkScrape = 'https://telemetr.io/en/channels'
xhtml = contents(linkScrape).decode('utf-8')
#print(xhtml)
p = HTMLTableParser()

p.feed(xhtml)

#pprint(p.tables)
now = datetime.datetime.now()
now = now.strftime('%A, %B %d, %Y  %I:%M %p')
# print(f'Headlines on {linkScrape} for \n{now}')
# print('='*100)
#date = pd.to_datetime("%Y")
dtable = pd.DataFrame(p.tables[0])

empty_row = pd.DataFrame([{0:'***************',
               1:'****************',
               2:'****************',
               3:'****************',
               4:'****************',
               5:'****************',
               6:'****************',
               7:'****************',
               8:'****************'
               }])




column_dict = {0:f'Scrape Date {now}',
               1:'Page Name',
               2:'Subscribers/Followers',
               3:'Page Growth',
               4:'Post Views',
               5:'Post to Sub Ratio',
               6:'Page Mentions',
               7:'Geo',
               8:'Category'}
dtable.drop(0,axis=0,inplace=True)
dtable= pd.concat([dtable,empty_row])
dtable.rename(columns=column_dict,inplace=True)
dtable.insert(9, "Channel Link", ans, True)

print(dtable)
dtable.to_csv('~/telemeterio.csv',index=None,header=True, mode='a')