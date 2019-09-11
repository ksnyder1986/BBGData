# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 08:12:29 2019

@author: Kris
"""
import re
import csv
import time

import requests
from bs4 import BeautifulSoup


base = 'http://www.boardgamegeek.com/browse/boardgame/page/{}'
#with open('ids.txt') as f:
#    ids = [line.strip() for line in f.readlines()]
f = open('ids.csv', 'w')
writer = csv.writer(f)
writer.writerow(('id','1'))

#for i in range(0, len(usernames), split):
 #   url = base.format(','.join(usernames[i:i+split]))
for i in range(1095):
   url = base.format(''.join(str(i+1))) 
   print('Requesting {}'.format(url))
   req = requests.get(url)
   soup = BeautifulSoup(req.content, 'lxml')
   rows = soup.select('tr#row_')
   for row in rows:
            a = row.find_all('a', href=re.compile('^/boardgame'))
            for r in a:
                if r.text:
                    g = r.get('href').split('/')[2]
                    writer.writerow((g,''))
   time.sleep(5)

f.close()
