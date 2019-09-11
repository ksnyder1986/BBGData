import csv
import time

import requests
from bs4 import BeautifulSoup


def get_val(tag, term):
    try:
        val = tag.find(term)['value'].encode('ascii', 'ignore')
    except:
        val = 'NaN'
    return val


base = 'http://www.boardgamegeek.com/xmlapi2/thing?id={}&stats=1'
with open('ids.txt') as f:
    ids = [line.strip() for line in f.readlines()]
#ids = ["161936"]
split = 1
f = open('games.csv', 'w')
writer = csv.writer(f)
writer.writerow((  'id'
                 , 'type'
                 , 'name'
                 , 'yearpublished'
                 , 'minplayers'
                 , 'maxplayers'
                 , 'playingtime'
                 , 'minplaytime'
                 , 'maxplaytime'
                 , 'minage'
                 , 'users_rated'
                 , 'average_rating'
                 , 'bayes_average_rating'
                 , 'total_owners'
                 , 'total_traders'
                 , 'total_wanters'
                 , 'total_wishers'
                 , 'total_comments'
                 , 'total_weights'
                 , 'average_weight'
                 #, 'play1best'
                 #, 'play1recd' 
                 #, 'play1notrecd'
                 #, 'play2best'
                 #, 'play2recd' 
                 #, 'play2notrecd'
                 #, 'play3best'
                 #, 'play3recd' 
                 #, 'play3notrecd'
                 #, 'play4best'
                 #, 'play4recd' 
                 #, 'play4notrecd'
                 #, 'play5best'
                 #, 'play5recd' 
                 #, 'play5notrecd'
                 , 'catlist'
                 , 'mechlist'
                 , 'familylist'
                 , 'designerlist'))

for i in range(1, len(ids), split):
    url = base.format(','.join(ids[i:i+split]))
    print('Requesting {}'.format(url))
    req = requests.get(url)
    soup = BeautifulSoup(req.content, 'xml')
    items = soup.find_all('item')
    for item in items:
        gid          = item['id']
        gtype        = item['type']
        gname        = get_val(item, 'name')
        gyear        = get_val(item, 'yearpublished')
        gmin         = get_val(item, 'minplayers')
        gmax         = get_val(item, 'maxplayers')
        gplay        = get_val(item, 'playingtime')
        gminplay     = get_val(item, 'minplaytime')
        gmaxplay     = get_val(item, 'maxplaytime')
        gminage      = get_val(item, 'minage')
        usersrated   = get_val(item.statistics.ratings, 'usersrated')
        avg          = get_val(item.statistics.ratings, 'average')
        bayesavg     = get_val(item.statistics.ratings, 'bayesaverage')
        owners       = get_val(item.statistics.ratings, 'owned')
        traders      = get_val(item.statistics.ratings, 'trading')
        wanters      = get_val(item.statistics.ratings, 'wanting')
        wishers      = get_val(item.statistics.ratings, 'wishing')
        numcomments  = get_val(item.statistics.ratings, 'numcomments')
        numweights   = get_val(item.statistics.ratings, 'numweights')
        avgweight    = get_val(item.statistics.ratings, 'averageweight')
        # desc = item.description.text.encode('ascii', 'ignore')
        #play1best    = item.find(attrs={"name": "suggested_numplayers"}).find(attrs={"numplayers":"1"}).find(attrs={"value":"Best"})['numvotes'].encode('ascii', 'ignore')
        #play1recd    = item.find(attrs={"name": "suggested_numplayers"}).find(attrs={"numplayers":"1"}).find(attrs={"value":"Recommended"})['numvotes'].encode('ascii', 'ignore')
        #play1notrecd = item.find(attrs={"name": "suggested_numplayers"}).find(attrs={"numplayers":"1"}).find(attrs={"value":"Not Recommended"})['numvotes'].encode('ascii', 'ignore')
        #play2best    = item.find(attrs={"name": "suggested_numplayers"}).find(attrs={"numplayers":"2"}).find(attrs={"value":"Best"})['numvotes'].encode('ascii', 'ignore')
        #play2recd    = item.find(attrs={"name": "suggested_numplayers"}).find(attrs={"numplayers":"2"}).find(attrs={"value":"Recommended"})['numvotes'].encode('ascii', 'ignore')
        #play2notrecd = item.find(attrs={"name": "suggested_numplayers"}).find(attrs={"numplayers":"2"}).find(attrs={"value":"Not Recommended"})['numvotes'].encode('ascii', 'ignore')
        #play3best    = item.find(attrs={"name": "suggested_numplayers"}).find(attrs={"numplayers":"3"}).find(attrs={"value":"Best"})['numvotes'].encode('ascii', 'ignore')
        #play3recd    = item.find(attrs={"name": "suggested_numplayers"}).find(attrs={"numplayers":"3"}).find(attrs={"value":"Recommended"})['numvotes'].encode('ascii', 'ignore')
        #play3notrecd = item.find(attrs={"name": "suggested_numplayers"}).find(attrs={"numplayers":"3"}).find(attrs={"value":"Not Recommended"})['numvotes'].encode('ascii', 'ignore')
        #play4best    = item.find(attrs={"name": "suggested_numplayers"}).find(attrs={"numplayers":"4"}).find(attrs={"value":"Best"})['numvotes'].encode('ascii', 'ignore')
        #play4recd    = item.find(attrs={"name": "suggested_numplayers"}).find(attrs={"numplayers":"4"}).find(attrs={"value":"Recommended"})['numvotes'].encode('ascii', 'ignore')
        #play4notrecd = item.find(attrs={"name": "suggested_numplayers"}).find(attrs={"numplayers":"4"}).find(attrs={"value":"Not Recommended"})['numvotes'].encode('ascii', 'ignore')
        #play5best    = item.find(attrs={"name": "suggested_numplayers"}).find(attrs={"numplayers":"4+"}).find(attrs={"value":"Best"})['numvotes'].encode('ascii', 'ignore')
        #play5recd    = item.find(attrs={"name": "suggested_numplayers"}).find(attrs={"numplayers":"4+"}).find(attrs={"value":"Recommended"})['numvotes'].encode('ascii', 'ignore')
        #play5notrecd = item.find(attrs={"name": "suggested_numplayers"}).find(attrs={"numplayers":"4+"}).find(attrs={"value":"Not Recommended"})['numvotes'].encode('ascii', 'ignore')
        #langdeplvl1  = item.find(attrs={"name": "language_dependence"}).find(attrs={"value":"No necessary in-game text"})['numvotes'].encode('ascii', 'ignore')
        #langdeplvl2  = item.find(attrs={"name": "language_dependence"}).find(attrs={"value":"Some necessary text - easily memorized or small crib sheet"})['numvotes'].encode('ascii', 'ignore')
        #langdeplvl3  = item.find(attrs={"name": "language_dependence"}).find(attrs={"value":"Moderate in-game text - needs crib sheet or paste ups"})['numvotes'].encode('ascii', 'ignore')
        #langdeplvl4  = item.find(attrs={"name": "language_dependence"}).find(attrs={"value":"Extensive use of text - massive conversion needed to be playable"})['numvotes'].encode('ascii', 'ignore')
        #langdeplvl5  = item.find(attrs={"name": "language_dependence"}).find(attrs={"value":"Unplayable in another language"})['numvotes'].encode('ascii', 'ignore')
        catlist = ""
        for val in item.find_all(attrs={"type": "boardgamecategory"}):
            catlist += val["id"] + "|"
        mechlist = ""
        for val in item.find_all(attrs={"type": "boardgamemechanic"}):
            mechlist += val["id"] + "|"
        familylist = ""
        for val in item.find_all(attrs={"type": "boardgamefamily"}):
            familylist += val["id"] + "|"
        designerlist = ""
        for val in item.find_all(attrs={"type": "boardgamedesigner"}):
            designerlist += val["id"] + "|"
        
        
        writer.writerow((  gid
                         , gtype
                         , gname
                         , gyear
                         , gmin
                         , gmax
                         , gplay
                         , gminplay
                         , gmaxplay
                         , gminage
                         , usersrated
                         , avg
                         , bayesavg
                         , owners
                         , traders
                         , wanters
                         , wishers
                         , numcomments
                         , numweights
                         , avgweight
                         #, play1best
                         #, play1recd 
                         #, play1notrecd
                         #, play2best
                         #, play2recd 
                         #, play2notrecd
                         #, play3best
                         #, play3recd 
                         #, play3notrecd
                         #, play4best
                         #, play4recd 
                         #, play4notrecd
                         #, play5best
                         #, play5recd 
                         #, play5notrecd
                         , catlist
                         , mechlist
                         , familylist
                         , designerlist))
    time.sleep(2)
f.close()
