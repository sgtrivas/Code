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
    response = req.get(link)
    # f = urllib.request.urlopen(response)
    # print(f)
    soup = BeautifulSoup(response.content, "html.parser")
    #print(soup)
    return soup
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
#df = pd.DataFrame()
empty_row = pd.DataFrame([{0:'***************',
               1:'****************',
               2:'****************',
               3:'****************',
               4:'****************',
               5:'****************',
               6:'****************',
               7:'****************',
               8:'****************'}])




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

print(dtable)
dtable.to_csv('/home/nrivas/Desktop/telemeterio.csv',index=None,header=True, mode='a')
