# Sorry for english
## Supported Trackers
* [1337x](https://1337xx.to)
* [solidtorrents](https://solidtorrents.net)
* [bt4g](https://bt4g.org)
* [limetorrents](https://limetorrents.pro)
* [zooqle](https://zooqle.com)
* [piratebay](https://knaben.ru)
* [torrentdownload](https://torrentdownload.info)
* [nyaa](https://nyaa.si)
* [magnetdl](https://magnetdl.com)
* [uniondht](http://uniondht.org)
* [torlock](https://torlock.com)
* [torrentdownloads](https://torrentdownloads.pro)


## How to Use
```python
import torrse

#print(torrse.Engines)
engine = torrse.engine_1337x()

#all of the engines got same parameters

#query = your query
# category = category of torrent --> print(torrse.categories)
#limit = limit of torrents
#magnet = extract magnet for each torrent if True, it may be slow when you use it, also you can extract magnet after search --> engine.get_magnet(link)

#default parameters
#search(query, category=None, limit=15, magnet=False)
results = engine.search('dragon nest', 'movie', 30)

for i in results:
    print(i, '\n'*3)
    #in some engines magnet links in query page so i also added it in search results (see engine_nyaa)


#also there is a function to make search in all engines

#NOTE: limit parameter for each engine
#exclude_same = exclude torrents that got same magnets
#engines = list of engines that you want to make search, ALL if you do not set parameter

#default parameters
#search(query, category=None, limit=15, magnet=False, exclude_same=True, engines=Engines)
results = torrse.search('dear esther', 'game', 30)
results = torrse.search('dear esther', 'game', 30, engines=[engine_1337x, engine_piratebay, engine_nyaa]) 
```

## requirements
* requests
* bs4 (BeautifulSoup)
* lxml
