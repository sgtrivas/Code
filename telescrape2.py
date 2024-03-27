from telethon import TelegramClient, utils

async def scrape_telegram_channel(api_id, api_hash, channel_username):
  """
  Scrapes a Telegram channel using Telethon library and outputs data to a CSV file.

  Args:
    api_id: Your Telegram API ID.
    api_hash: Your Telegram API hash.
    channel_username: Username of the public channel (e.g., 'yourchannel').
  """
  async with TelegramClient(None, api_id, api_hash) as client:
    channel = await client.get_entity(channel_username)
    messages = await client.get_messages(channel, limit=100)  # Adjust limit as needed

    posts = []
    subscriber_count = await client.get_participants_count(channel)
    is_active = any(message.entities for message in messages)  # Check for message entities

    for message in messages:
      post_text = message.message

      # Extract relevant data from message object (text, media, etc.)
      posts.append(post_text)

    # Write data to CSV
    with open('telegram_channel_data.csv', 'w', newline='') as csvfile:
      writer = csv.writer(csvfile)
      writer.writerow(['Post', 'Subscriber Count', 'Is Active'])
      for post in posts:
        writer.writerow([post, subscriber_count, is_active])

# Example usage (replace with your API credentials and channel username)
api_id =   # Replace with your API ID
api_hash = '' 
channel_username = 'linuxgram'
