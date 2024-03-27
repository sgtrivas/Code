import os

try:
    import requests as req
    from bs4 import BeautifulSoup
    import pandas as pd
except ImportError:
    print("Stand by installing missing modules")
    os.system('pip3 install requests beautifulsoup4')
position = []
published_dates = []
sources = []
descriptions = []
links = []

# Make a request to the desired URL
link = f'https://telemetr.io/en/channels'

res = req.get(link)
#print(res.cookies)
txt = res.text
status = res.status_code
#print(txt,status)
#  page response code, just in case it fails we can show it.
print(f'Page response: {res}')

page = res
soup = BeautifulSoup(page.content, 'html.parser')
# get the title
page_title = soup.title.text


print(f'The Page Title for :\n {page_title}')


# Create a BeautifulSoup object
soup = BeautifulSoup(res.content, 'html.parser')



#print(soup)
# Find all <h1> tags and store them in a list
body = []
#soup.find_all('tr',class_='hover:bg-bg-base-secondary')



for table_list in soup.find_all('tr',class_='hover:bg-bg-base-secondary'):
        body.append(table_list.get_text())

print(body[0], end=' ')
# name = soup.find_all('a', class_="channel-name__title short-text cursor-pointer font-semibold text-text-base-primary first-letter:uppercase hover:text-text-accent")
# views = soup.find_all('td',class_='px-1 py-2.5 text-left text-xs text-text-base-secondary')

#subscribers = soup.find_all('td', class_='px-1 py-2.5',limit=100)

# news_df = pd.DataFrame ({
#          "Position": body,
#          #"Title": body,
#         #  "Subs": body,
#         #  "Views": body,
#         #  "Description": body,
#         #  "Link": links 
#          })
# print(news_df)
#  page rank
# for position in rank:
#     print(position.get_text())

# for position,name_list in rank,name:
#     print(f'{position.get_text()} , {name_list.get_text()}')




# # Print the text content of each <h1> tag
# for tag in all_h1_tags:
#     print(tag.get_text())
