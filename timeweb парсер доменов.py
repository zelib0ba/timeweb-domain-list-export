from os import stat
from typing import Dict
import requests
from bs4 import BeautifulSoup
import pandas as Pd
# import openpyxl
import re
import time
from fake_useragent import UserAgent
import datetime
today = datetime.datetime.today() 
curdate = today.strftime('%d.%m.%y')
import punycode


html = open ('./dom1.html', 'r', encoding='utf-8')

htmlTag = 'td'
htmlTagClass = 'domain-list-table__description'

soup = BeautifulSoup(html, 'lxml')
head = soup.findAll(htmlTag, class_= htmlTagClass)

def month_converter(month):
    months = ['янв.', 'февр.', 'мар.', 'апр.', 'май.', 'июн.', 'июл.', 'авг.', 'сент.', 'окт.', 'нояб.', 'дек.']
    return months.index(month) + 1

for z, i in enumerate(head):
    # print (z, i)
    domain_name = i.find ('a', class_ = 'cpS-lk-simple-one-line js-fqdn')['data-puny']
    pending_date = i.find ('p', class_ = 'cpS-tx-add-accent js-domain-info')
    print (punycode.convert(domain_name))
    # print (pending_date.text.split(' '))
    # date  = pending_date.text.split(' ')
    # print (date[5])
    # if date[4] == 'Оплачен':
        # day = date[6]
        # month = date[7]
        # year = date[8]
        # if len(str(month_converter(month))) == 1:
            # month = f'0{month_converter(month)}'
        # else:
            # month = month_converter(month)
        # print (f'{punycode.convert(domain_name)} - {day}.{month}.{year[0:4]}')
    # else:
        # print (f'{punycode.convert(domain_name)} {date[-3:]}')

