from telethon import TelegramClient as tc

    #  Api ID and Hash for Pixel 7a
api_id = 
api_hash = ''
client = tc('Jim Smith', api_id, api_hash)
    
#  phone just in case its requested 
#  phone = +1
#  bot_token = ''

async def main():
    me = await client.get_me()
    #print(me.stringify())

    username = me.username
    usersName = me.first_name + ' ' + me.last_name
    print(f'Telegram Username: {username}\n')
    print(f'Phone associated: {me.phone}\n')
    print(f'{usersName}\n')

    async for dialog in client.iter_dialogs():
        if usersName == dialog.name:
            print(f"{dialog.name}, 'has ID', {dialog}")
        else:
            continue
        #print(f"{dialog.name}, 'has ID', {dialog.message.id}\nLast Post: {dialog.message.message}\nTotal Views: {dialog.message.views}\nDate: {dialog.message.date}\n")


with client:
    client.loop.run_until_complete(main())







    
    
