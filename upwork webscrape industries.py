from urllib.request import urlopen, Request
from bs4 import BeautifulSoup as bs
import string
import re
import pandas as pd

alp = list(string.ascii_uppercase)
l = []
for a in alp:
    header = {'User-Agent':'Chrome'}
    req = Request(f'https://www.plimsoll.co.uk/uk-industries-list-a-to-z/{a}', headers=header)
    html = urlopen(req)
    obj = bs(html)
    table = obj.findAll('div', {'class' : 'c-search__results--item'})
    for x in table:
        l.append(x.find('p').text)


def remove(list):
    pattern = '[0-9]'
    list = [re.sub(pattern, '', i) for i in list]
    return list
    
l1 = remove(l)
df = pd.DataFrame(l1)
df.to_csv(r"Industries.csv",index=False,header=False)

