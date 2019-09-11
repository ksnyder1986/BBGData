import csv
import time

import requests
from bs4 import BeautifulSoup


base = 'http://www.boardgamegeek.com/xmlapi2/collection?username={}&stats=1'
#with open('ids.txt') as f:
#    ids = [line.strip() for line in f.readlines()]
usernames = ["ksnyder86"]
split = 30
f = open('usergames.csv', 'w')
writer = csv.writer(f)
writer.writerow(( 'playerid'
                 , 'gameid'
                # , 'name'
                 , 'rating'
                 , 'owned'
                 , 'prevowned'
                 , 'fortrade'
                 , 'want'
                 , 'wanttoplay'
                 , 'wanttobuy'
                 , 'wishlist'
                 , 'preordered'
                # , 'numplays'
                 ))

for i in range(0, len(usernames), split):
    url = base.format(','.join(usernames[i:i+split]))
    print('Requesting {}'.format(url))
    req = requests.get(url)
    soup = BeautifulSoup(req.content, 'xml')
    items = soup.find_all('item')
    for item in items:
        playerid    = usernames[i:i+split]
        gameid      = item["objectid"].encode('ascii', 'ignore')
        rating      = item.stats.rating["value"].encode('ascii', 'ignore')
        owned       = item.status["own"].encode('ascii', 'ignore')
        prevowned   = item.status["prevowned"].encode('ascii', 'ignore')
        fortrade    = item.status["fortrade"].encode('ascii', 'ignore')
        want        = item.status["want"].encode('ascii', 'ignore')
        wanttoplay  = item.status["wanttoplay"].encode('ascii', 'ignore')
        wanttobuy   = item.status["wanttobuy"].encode('ascii', 'ignore')
        wishlist    = item.status["wishlist"].encode('ascii', 'ignore')
        preordered  = item.status["preordered"].encode('ascii', 'ignore')
        
        writer.writerow((  playerid
                          , gameid
                          , rating
                          , owned
                          , prevowned
                          , fortrade
                          , want
                          , wanttoplay
                          , wanttobuy
                          , wishlist
                          , preordered
                          ))
    time.sleep(2)
f.close()
