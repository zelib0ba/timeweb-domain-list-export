from bs4 import BeautifulSoup
import pandas as Pd
import datetime
import xlsxwriter
today = datetime.datetime.today() 
curdate = today.strftime('%d.%m.%y')
import punycode

wb = xlsxwriter.Workbook('./twDomains.xlsx')
ws = wb.add_worksheet(f'Timeweb Domain List')
autorenowal_none = wb.add_format({'bold': True, 'font_color': 'red'})
date_format = wb.add_format({'num_format':'dd-mm-yyyy'})

ws.write(0,0,'Имя домена')
ws.write(0,1,'оплачен до')
ws.write(0,2,'автоплатеж')
ws.write(0,3,'примечание')
html = open ('./dom1.html', 'r', encoding='utf-8')

htmlTag = 'td'
htmlTagClass = 'domain-list-table__description'

soup = BeautifulSoup(html, 'lxml')
head = soup.findAll(htmlTag, class_= htmlTagClass)

def month_converter(month):
    months = ['янв.', 'февр.', 'мар.', 'апр.', 'май.', 'июн.', 'июл.', 'авг.', 'сент.', 'окт.', 'нояб.', 'дек.']
    return months.index(month) + 1

for z, i in enumerate(head):
    domain_name = i.find ('a', class_ = 'cpS-lk-simple-one-line js-fqdn')['data-puny']
    pending_date = i.find ('p', class_ = 'cpS-tx-add-accent js-domain-info')
    date =  pending_date.text.replace('\n','').split(' ')[4:]
    domain = punycode.convert(domain_name)

    if date[0] == 'Оплачен':
        day = date[2]
        month = date[3]
        year = date[4]
        
        if date[-2] == 'нет':
            autorenowal = date[-3].replace('\xa0—','')
        else:
            autorenowal = date[-2].replace('\xa0—','')
        if len(str(month_converter(month))) == 1:
            month = f'0{month_converter(month)}'
        else:
            month = month_converter(month)
        ws.write(z+1, 0, domain)
        ws.write(z+1, 1, f'{day}.{month}.{year[0:4]}',date_format)
        if autorenowal == 'выкл.':
            ws.write(z+1, 2, autorenowal,autorenowal_none)
        else:
            ws.write(z+1, 2, autorenowal)
        print (f'{z} - {domain} - {day}.{month}.{year[0:4]} автоплатеж - {autorenowal}')
    elif date[1] == 'закончится':
        day = date[2]
        month = date[3]
        year = date[4]
        
        if date[-2] == 'нет':
            autorenowal = date[-3].replace('\xa0—','')
        else:
            autorenowal = date[-2].replace('\xa0—','')
        if len(str(month_converter(month))) == 1:
            month = f'0{month_converter(month)}'
        else:
            month = month_converter(month)
        ws.write(z+1, 0, domain)
        ws.write(z+1, 1, f'{day}.{month}.{year[0:4]}',date_format)
        if autorenowal == 'выкл.':
            ws.write(z+1, 2, autorenowal,autorenowal_none)
        else:
            ws.write(z+1, 2, autorenowal)
    else:
        ws.write(z+1, 0, domain)
        ws.write(z+1, 3, f'{" ".join(date)}')
        print (f'{z} - {domain} {date}')
        # cell_index+=1
wb.close()