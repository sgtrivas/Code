# work in progress
import requests as req 

# replace with links imported from txt file.
link = f'https://codedamn.com'

res = req.get(link)
txt = res.text
status = res.status_code
#print(txt,status)
#  page response code, just in case it fails we can show it.
print(f'Page response: {res}')

from bs4 import BeautifulSoup

page = res
soup = BeautifulSoup(page.content, 'html.parser')
# get the title
page_title = soup.title.text
print(f'The Page Title for {link}:\n{page_title}\n')

page_body = soup.body.text

#print(type(page_body))

page_head = soup.head.text
#print(page_head)
all_h1_tags = []
try:
    first_h1 = soup.select('h1')
    for element in first_h1:
        all_h1_tags.append(element.text)
    print(all_h1_tags)
except AttributeError:
    print(f'The object is {type(first_h1)} you have to give it an index position')
    print(f'also ensure you are using the correct attribues for a list')
except IndexError:
    print(f'Start with index 0')

try:
    seventh_p_text = soup.select('p')[6].text
    if "butt" in seventh_p_text:
       print(seventh_p_text)
    else:
        print("Keyword not found")
except:
    pass
