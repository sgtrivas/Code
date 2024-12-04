from __future__ import with_statement                                                        
 
import contextlib
 
try:
    from urllib.parse import urlencode          
 
except ImportError:
    from urllib import urlencode
 
try:
    from urllib.request import urlopen
 
except ImportError:
    from urllib2 import urlopen
 
import sys

try:
    import pyinputplus as pyip
except ImportError:
    print("Module not installed")

def make_tiny(url):
    request_url = ('http://tinyurl.com/api-create.php?' + urlencode({'url':url}))   
    with contextlib.closing(urlopen(request_url)) as response:                      
        return response.read().decode('utf-8 ')
    
 
def main(urls):     

    print(f'Here is a shortened version of {urls} = {make_tiny(urls)}')


if __name__ == '__main__':
    
    urls = pyip.inputURL('Please enter the URL you wish to shorten: ')
    main(urls)
