from bs4 import BeautifulSoup
import requests as req
import datetime
import pandas as pd


link = input('Enter link to scrape: ')
response = req.get(link)
soup = BeautifulSoup(response.text, 'html.parser')
lines = soup.find_all('span', class_="container__headline-text")
def cnn(lines):

    if lines:
    # If lines is not None, proceed with further processing
        headlines = [str(line).replace('<span class="container__headline-text" data-editable="headline">', '').replace('</span>', '') for line in lines]
        now = datetime.datetime.now()
        now = now.strftime('%A, %B %d, %Y  %I:%M %p')
        print(f'Headlines on {link} for \n{now}')
        print('='*100)
        for index, title in enumerate(headlines,1):
            print(f'{index}. {title.strip()}\n')
    else:
        fox()
def fox():
    # Define the URL of the Fox News homepage
    #url = 'https://www.foxnews.com/'

    # Send an HTTP request to the website
    response = req.get(link)

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the headlines (you may need to adjust the selector based on the website's structure)
    headlines = soup.find_all('h3', class_='title')
    now = datetime.datetime.now()
    now = now.strftime('%A, %B %d, %Y  %I:%M %p')
    print(f'Headlines on {link} for \n{now}')
    print('='*100)
    # Print the headlines
    for index, headline in enumerate(headlines, 1):
        print(f"{index}. {headline.text.strip()}\n")

    # If no headlines are found, handle the case gracefully
    if not headlines:
        print("No headlines found")


def gnews(link):
    # Define the Google News URL you want to scrape
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
        sources.append(item.source.text)
        descriptions.append(item.description.text)
        links.append(item.link.text)

    # Create a DataFrame to store the scraped data
    news_df = pd.DataFrame({
        "Title": titles,
        "Published Date": published_dates,
        "Source": sources,
        "Description": descriptions,
        "Link": links
    })
    print(news_df)
    # Export data to a CSV file with a timestamped filename
    #news_df.to_csv("google_news_headlines.csv", index=False)

    print("Scraping complete! Headlines saved to 'google_news_headlines.csv'.")

cnn(lines)
    