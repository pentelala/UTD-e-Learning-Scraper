from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen('https://en.wikipedia.org/wiki/Osamu_Dazai#Works')
bs = BeautifulSoup(html, 'html.parser')

def class_mod(tag):
    return tag.name=='td' and not tag.has_attr("rowspan")

for child in bs.find('table', {'wikitable'}).find('tr').next_siblings:
    if child.find('td')!=-1:
        print(child.find(class_mod))
