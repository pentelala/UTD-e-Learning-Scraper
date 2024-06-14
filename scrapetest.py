from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen('https://en.wikipedia.org/wiki/Osamu_Dazai#Works')
bs = BeautifulSoup(html, 'lxml')

def class_mod(tag):
    return tag.name=='td' and not tag.has_attr("rowspan")

for child in bs.find('table', {'wikitable'}).find('tr').next_siblings:
    onlyText = child.get_text()
    if child.find('td')!=-1:
        textStrip = re.sub('<[^<]+?>', '', onlyText)
        print(child.find(class_mod))
