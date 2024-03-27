#  https://t.me/qawedfqwefawsdfqwefqw3ef_bot

import csv
from telethon.sync import TelegramClient

# Replace with your own API credentials
api_id = 
api_hash = ''
bot_token = ''

# Initialize the Telegram client
client = TelegramClient('my_session', api_id, api_hash).start(bot_token=bot_token)

async def get_channel_info(channel_name):
    try:
        # Get the channel entity
        entity = await client.get_entity(channel_name)
        if entity:
            # Check if the channel is active
            is_active = entity.megagroup or entity.broadcast
            # Get the number of subscribers
            subscribers_count = entity.participants_count
            # Get recent posts (you can adjust the limit)
            posts = await client.get_messages(entity, limit=10)

            return is_active, subscribers_count, posts
        else:
            return None
    except Exception as e:
        print(f"Error: {e}")
        return None

async def main():
    channel_name = 'Ha'
    channel_info = await get_channel_info(channel_name)

    if channel_info:
        is_active, subscribers_count, posts = channel_info
        print(f"Channel '{channel_name}' is active: {is_active}")
        print(f"Subscribers count: {subscribers_count}")

        # Export posts to a CSV file
        with open('channel_posts.csv', 'w', newline='') as csvfile:
            fieldnames = ['message_id', 'text', 'date']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for post in posts:
                writer.writerow({
                    'message_id': post.id,
                    'text': post.text,
                    'date': post.date
                })
        print("Posts exported to channel_posts.csv")
    else:
        print(f"Channel '{channel_name}' not found.")

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())
