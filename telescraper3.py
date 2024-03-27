import requests
from bs4 import BeautifulSoup
import csv

def scrape_telegram_channel(url):
  """
  Scrapes a Telegram channel using web scraping and outputs data to a CSV file.

  Args:
    url: The URL of the public Telegram channel (e.g., https://t.me/yourchannel).
  """
  response = requests.get(url)
  soup = BeautifulSoup(response.content, 'html.parser')

  # Extract data (replace selectors as needed based on Telegram's website structure)
  posts = []
  subscriber_count_element = soup.find('span', class_='tgme_channel_info_participants')
  if subscriber_count_element:
    subscriber_count = subscriber_count_element.text.strip()
  else:
    subscriber_count = "N/A"
  is_active = any(element.text.strip() == "Online" for element in soup.find_all('span', class_='tgme_chat_online'))

  for post_element in soup.find_all('div', class_='tgme_widget_message'):
    post_text = post_element.find('div', class_='message-body').text.strip()
    posts.append(post_text)

  # Write data to CSV
  with open('telegram_channel_data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Post', 'Subscriber Count', 'Is Active'])
    for post in posts:
      writer.writerow([post, subscriber_count, is_active])

# Example usage
channel_url = "https://t.me/telemetr.io/en/channels"
scrape_telegram_channel(channel_url)
