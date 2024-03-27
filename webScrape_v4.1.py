from bs4 import BeautifulSoup
import requests as req
import datetime
import pandas as pd
import pyinputplus as pyip


def cnn(link):
    # fetch raw html content
    response = req.get(link)
    soup = BeautifulSoup(response.content, "xml")

    # Initialize lists to store data
    titles = []
    published_dates = []
    #sources = []
    descriptions = []
    links = []
    
    for item in soup.find_all("item"):
        titles.append(item.title.text)
        published_dates.append(item.pubDate.text)
        #sources.append(item.source.text)
        descriptions.append(item.description.text)
        links.append(item.link.text)

    news_df = pd.DataFrame({
        "Title": titles,
        "Published Date": published_dates,
        #"Source": sources,
        "Description": str(descriptions).replace('<div>','').replace('<img src=\"','').replace('\" /><div>', '').replace('</div>',''),
        "Link": links
    })
    print(news_df)

    news_df.to_csv("cnn_news_headlines.csv", index=False)

    print("Scraping complete! Headlines saved to 'cnn_news_headlines.csv'.")
def fox(link):
    # Define the Google News URL you want to scrape RSS feeds
    #url = "https://news.google.com/rss"

    # Fetch the raw HTML content
    response = req.get(link)
    soup = BeautifulSoup(response.content, "xml")

    # Initialize lists to store data
    titles = []
    published_dates = []
    sources = []
    descriptions = []
    links = []

    # Extract relevant data
    for item in soup.find_all("item"):
        titles.append(item.title.text)
        published_dates.append(item.pubDate.text)
        #sources.append(item.source.text)
        descriptions.append(item.description.text)
        links.append(item.link.text)

    # Create a DataFrame to store the scraped data
    news_df = pd.DataFrame({
        "Title": titles,
        "Published Date": published_dates,
        #"Source": sources,
        "Description": descriptions,
        "Link": links
    })
    print(news_df)
    #  Export data to a CSV file with a timestamped filename
    news_df.to_csv("fox_news_headlines.csv", index=False)

    print("Scraping complete! Headlines saved to 'fox_news_headlines.csv'.")


def gnews(link):
    # Define the Google News URL you want to scrape RSS feeds
    #url = "https://news.google.com/rss"

    # Fetch the raw HTML content
    response = req.get(link)
    soup = BeautifulSoup(response.content, "xml")
    print(soup)

    # # Initialize lists to store data
    # titles = []
    # published_dates = []
    # sources = []
    # descriptions = []
    # links = []

    # # Extract relevant data
    # for item in soup.find_all("item"):
    #     titles.append(item.title.text)
    #     published_dates.append(item.pubDate.text)
    #     sources.append(item.source.text)
    #     descriptions.append(item.description.text)
    #     links.append(item.link.text)

    # # Create a DataFrame to store the scraped data
    # news_df = pd.DataFrame({
    #     "Title": titles,
    #     "Published Date": published_dates,
    #     "Source": sources,
    #     #"Description": descriptions,
    #     "Link": links
    # })
    # print(news_df)
    # #  Export data to a CSV file with a timestamped filename
    # news_df.to_csv("google_news_headlines.csv", index=False)

    # print("Scraping complete! Headlines saved to 'google_news_headlines.csv'.")


if __name__ == '__main__':
    link = pyip.inputURL(prompt='Enter link to scrape: ')
    #response = req.get(link)
    #soup = BeautifulSoup(response.text, 'html.parser')
    #lines = soup.find_all('span', class_="container__headline-text")
    now = datetime.datetime.now()
    now = now.strftime('%A, %B %d, %Y  %I:%M %p')
    print(f'Headlines on {link} for \n{now}')
    print('='*100)
       
    if 'news.google.com' in link:
        gnews(link)
    elif 'foxnews.com' in link:
        fox(link)
    else:
        cnn(link)
    