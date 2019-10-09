import re
import csv
import time

import requests
from bs4 import BeautifulSoup


base = 'https://www.boardgamegeek.com/boardgame/13/catan/ratings?rated=1&pageid={}'
#with open('ids.txt') as f:
#    ids = [line.strip() for line in f.readlines()]
f = open('users.csv', 'w')
writer = csv.writer(f)
writer.writerow(('id','1'))

#for i in range(0, len(usernames), split):
 #   url = base.format(','.join(usernames[i:i+split]))
for i in range(1):
   url = base.format(''.join(str(i+1))) 
   print('Requesting {}'.format(url))
   req = requests.get(url)
   soup = BeautifulSoup(req.content, 'html.parser')
   print(soup)
   rows = soup.select('div.comment-header')
   for row in rows:
            print(row)
            a = row.find_all('a', href=re.compile('^/user'))
            for r in a:
                if r.text:
                    g = r.get('href').split('/')[2]
                    writer.writerow((g,''))
   time.sleep(5)

f.close()
