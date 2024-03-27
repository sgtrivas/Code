#import urllib.request
import requests as req
from pprint import pprint
from html_table_parser.parser import HTMLTableParser
import pandas as pd
from bs4 import BeautifulSoup


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

xhtml = contents('https://telemetr.io/en/channels').decode('utf-8')
#print(xhtml)
p = HTMLTableParser()

p.feed(xhtml)

#pprint(p.tables)

dtable = pd.DataFrame(p.tables[0])

print(dtable)