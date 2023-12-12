# url extractor using 'usrlib' module and 'urllib.parse.urlparse'
from urllib.parse import urlparse as url_get
#  sorry the urls are not in order

urls = ["http://github.com/carbonfive/raygun", \
        'https://a0vdjojkul.info/warez/',\
            'https://if1249lbbv2f6wy.it',\
                'http://go6aahvddmx4lm.info/users',\
                    "http://www.xakep.ru",\
                        'https://5dixizwbbu66npr9.us/img/',\
                            "https://www.cnet.com",\
                                "http://www.zombie-bites.com"]
for u in urls:
    #  urllib.parse.urlparse returns a information 
    #  about the url i.e. (scheme='https', netloc='www.cnet.com', 
    #  path=''etc...)
    ans = url_get(u)
    #print(ans)
    print(ans.netloc.replace('www.', '').replace('.com','')  
           .replace('.it','').replace('.info','')
    .replace('.ru', '').replace('.us',''))
    
    




    
