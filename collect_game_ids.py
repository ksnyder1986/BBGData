import re
import csv
import time

import requests
from bs4 import BeautifulSoup


base = 'https://www.legis.state.pa.us/cfdocs/billinfo/bill_history.cfm?syear=2019&sind=0&body=H&type=B&bn={}'
f = open('pers.csv', 'w')
writer = csv.writer(f)
writer.writerow(('id','1'))
i = 462

for i in range(1):
   url = base.format(''.join(str(i+1))) 
   print('Requesting {}'.format(url))
   req = requests.get(url)
   soup = BeautifulSoup(req.content, 'html.parser')
   rows = soup.find_all("div", {"class":"BillInfo-Section-Data"})[0]
   a = str(rows).replace('and',',')
   a = str(rows).split(',')
   a
   rows

   time.sleep(5)

f.close()
