from bs4 import BeautifulSoup
import requests as req
import datetime
import pandas as pd
import pyinputplus as pyip
import xml.etree.ElementTree as ET

def teleMetr(link):
    # Define the Google News URL you want to scrape RSS feeds
    #url = "https://news.google.com/rss"

    # Fetch the raw HTML content
    response = req.get(link)
    soup = BeautifulSoup(response.content, "html.parser")
    print(soup)

    #with open('telemetrio.txt','a') as f:
     #   f.write()

    
    # Initialize lists to store data
    # Position = []
    # title = []
    # subs = []
    # growth = []
    # views = []
    # mentions = []
    # geo = []
    # category = []

    # # Extract relevant data
    # for item in soup.find_all("item"):
    #     titles.append(item.title.text)
    #     published_dates.append(item.pubDate.text)
    #     #sources.append(item.source.text)
    #     descriptions.append(item.description.text)
    #     links.append(item.link.text)

    # # Create a DataFrame to store the scraped data
    # news_df = pd.DataFrame({
    #     "Title": titles,
    #     "Published Date": published_dates,
    #     #"Source": sources,
    #     "Description": descriptions,
    #     "Link": links
    # })
    # print(news_df)
    # #  Export data to a CSV file with a timestamped filename
    # #news_df.to_csv("fox_news_headlines.csv", index=False)

    # #print("Scraping complete! Headlines saved to 'fox_news_headlines.csv'.")

link = 'https://telemetr.io/en/channels'
now = datetime.datetime.now()
now = now.strftime('%A, %B %d, %Y  %I:%M %p')
print(f'Headlines on {link} for \n{now}')
print('='*100)
teleMetr(link)