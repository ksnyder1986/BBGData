import re
import csv
import time

import requests
from bs4 import BeautifulSoup


base = 'https://www.legis.state.pa.us/cfdocs/billinfo/bill_history.cfm?syear=2019&sind=0&body=H&type=B&bn={}'
f = open('pers.csv', 'w')
writer = csv.writer(f)
writer.writerow(('Bill','Member_ID','Member_Name'))
i = 461

for i in range(462,463): #You will want to replace this range with a list of the bill numbers you care about
   url = base.format(''.join(str(i+1))) 
   print('Requesting {}'.format(url))
   req = requests.get(url)
   soup = BeautifulSoup(req.content, 'html.parser')
   rows = soup.find_all("div", {"class":"BillInfo-Section-Data"})[0]
   a = str(rows).replace(' and',',').replace('<div class="BillInfo-Section-Data">',' ')
   b = a.split(',')

   for val in b:
       id_loc = val.find('id=',0)
       lt_loc = val.find('">',0)
       id = val[id_loc+3:lt_loc]
       #print(val)
       print(id)
       gt_loc = val.find('<',lt_loc)
       #print(gt_loc)
       name = val[lt_loc+2:gt_loc]
       print(name)
       writer.writerow((i+1,id,name))
       
   time.sleep(2)
rows
f.close()
