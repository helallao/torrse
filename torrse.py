import requests as _requests
from bs4 import BeautifulSoup as _BeautifulSoup
from multiprocessing.dummy import Pool as _Pool
import re as _re
from urllib.parse import quote as _quote, unquote as _unquote



categories = ['movie', 'tv', 'music', 'software', 'game', 'anime', 'other']



#regex
_reg_itorrent2hash = _re.compile('itorrents.org/torrent/(.*).torrent')
_reg_bt4g2hash = _re.compile('bt4g.org/magnet/(.*)')




#functions
_soup = lambda x: _BeautifulSoup(x, 'lxml')
_hash2magnet = lambda x: f'magnet:?xt=urn:btih:{x}'
_magnet2hash = lambda x: x.split('&')[0].split(':')[-1].lower()
_itorrent2hash = lambda x: _reg_itorrent2hash.search(x).group(1).lower()
_bt4g2hash = lambda x: _reg_bt4g2hash.search(x).group(1).lower()
_hashlower = lambda x: x[0:20] + x[20:60].lower() + x[60:]


def get_magnet(link):
	matchmake = {
		'1337xx.to': lambda x: _hashlower(magnet[0].get('href')) if (magnet := _soup(_session.get(x).text).select('a[href^="magnet"]')) else None,
		'solidtorrents.net': lambda x: None,
		'bt4g.org': lambda x: _hashlower(_hash2magnet(_bt4g2hash(x))),
		'itorrents': lambda x: _hashlower(_hash2magnet(_itorrent2hash(x))),
		'zooqle.com': lambda x: None,
		'knaben.ru': lambda x: None,
		'torrentdownload.info': lambda x: None,
		'nyaa.si': lambda x: None,
		'magnetdl': lambda x: None,
		'uniondht.org': lambda x: _hashlower(magnet[0].get('href')) if (magnet := _soup(_session.get(x).text).select('a[href^="magnet"]')) else None,
		'torlock.com': lambda x: _hashlower(magnet[0].get('href')) if (magnet := _soup(_session.get(x).text).select('a[href^="magnet"]')) else None,
		'torrentdownloads.pro': lambda x: _hashlower(magnet[0].get('href')) if (magnet := _soup(_session.get(x).text).select('a[href^="magnet"]')) else None,
		'kickass.onl': lambda x: None
	}
	
	link = link.replace('https://', '').replace('http://', '')
	
	for i in matchmake:
		if link.startswith(i):
			return matchmake[i]('http://' + link)
	






_session = _requests.Session()
_session.headers.update({'user-agent': 'Mozilla/5.0 (Windows NT 5.1; rv:41.0) Gecko/20100101', 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8', 'accept-language': 'en-US,en;q=0.5', 'upgrade-insecure-requests': '1'})








class engine_1337x:
	def __init__(self):
		self._movie = 'https://1337xx.to/category-search/{query}/Movies/{page}/'
		self._tv = 'https://1337xx.to/category-search/{query}/TV/{page}/'
		self._music = 'https://1337xx.to/category-search/{query}/Music/{page}/'
		self._anime = 'https://1337xx.to/category-search/{query}/Anime/{page}/'
		self._game = 'https://1337xx.to/category-search/{query}/Games/{page}/'
		self._software = 'https://1337xx.to/category-search/{query}/Apps/{page}/'
		self._other = 'https://1337xx.to/category-search/{query}/Other/{page}/'
		
		self._normal = 'https://1337xx.to/search/{query}/{page}/'
		
		
		
		self._categories = {
			'movie': self._movie, 
			'tv': self._tv, 
			'music': self._music, 
			'software': self._software, 
			'game': self._game, 
			'anime': self._anime, 
			'other': self._other, 
			None: self._normal
		    }
	
	
	
	def search(self, query, category=None, limit=15, magnet=False, add_engine_name=False):
		query = query.replace(' ', '%20')
		
		
		last = 1
		found = 0
		results = []
		
		
		
		while found < limit:
			resp = _session.get(self._categories[category].format(query=query, page=last))
			
			if not resp.ok and resp.status_code not in [404]:
				return
			
			soup = _soup(resp.text)
			
			
			torrentList = soup.select('a[href*="/torrent/"]')
			self._seedersList = soup.select('td.coll-2')
			self._leechersList = soup.select('td.coll-3')
			self._sizeList = soup.select('td.coll-4')
			self._timeList = soup.select('td.coll-date')
			
			
			if torrentList:
				for count, torrent in enumerate(torrentList):
					name = torrent.getText().strip()
					link = 'https://1337xx.to/' + torrent['href']
					seeders = self._seedersList[count].getText()
					leechers = self._leechersList[count].getText()
					size = self._sizeList[count].contents[0]
					time = self._timeList[count].getText()
					
					results.append({'name': name, 'link': link, 'seeders': seeders, 'leechers': leechers, 'size': size, 'time': time})
					
					
					if magnet == True:
						results[-1].update({'magnet': get_magnet(link)})
					
					if add_engine_name:
						results[-1].update({'engine': '1337x'})
					
					
					found += 1
					
					if found >= limit:
						break
					
				last += 1
			
							
			else:
				break
		
		return results[:limit]








class engine_solidtorrents:
	def __init__(self):
		self._movie = 'https://solidtorrents.net/search?q={query}&page={page}&category=1&subcat=2'
		self._music = 'https://solidtorrents.net/search?q={query}&page={page}&category=7&subcat='
		self._game = 'https://solidtorrents.net/search?q={query}&page={page}&category=6&subcat=1'
		self._software = 'https://solidtorrents.net/search?q={query}&page={page}&category=5&subcat=1'
		
		self._normal = 'https://solidtorrents.net/search?q={query}&page={page}'
		
		
		
		self._categories = {
			'movie': self._movie, 
			'tv': self._movie, 
			'music': self._music, 
			'software': self._software, 
			'game': self._game, 
			'anime': self._movie, 
			'other': self._normal, 
			None: self._normal
		    }
	
	
	
	def search(self, query, category=None, limit=15, magnet=False, add_engine_name=False):
		query = query.replace(' ', '+')
		
		
		last = 1
		found = 0
		results = []
		
		
		
		while found < limit:
			resp = _session.get(self._categories[category].format(query=query, page=last))
			
			if not resp.ok and resp.status_code not in [404]:
				return
			
			soup = _soup(resp.text)
			
			
			torrentList = soup.select('div[class="search-result view-box"]')
			
			
			
			if torrentList:
				for torrent in torrentList:
					name = torrent.select('h5')[0].select('a')[0].getText().strip()
					link, name = ('https://solidtorrents.net' + _i.get('href'), _i.getText()) if (_i := torrent.select('a')[0]) else (None, None)
					size, seeders, leechers, time = (_i[1].getText().strip(), _i[2].getText().strip(), _i[3].getText().strip(), _i[4].getText().strip()) if (_i := torrent.select('div[class="stats"]')[0].select('div')) else (None, None, None, None)
					
					magnet = torrent.select('a[href^="magnet"]')[0].get('href')
					
					
					results.append({'name': name, 'link': link, 'seeders': seeders, 'leechers': leechers, 'size': size, 'time': time, 'magnet': magnet})
					
					
					if add_engine_name:
						results[-1].update({'engine': 'solidtorrents'})
					
					found += 1
					
					if found >= limit:
						break
				
				last += 1
			
							
			else:
				break
		
		return results[:limit]











class engine_bt4g:
	def __init__(self):
		self._movie = 'https://bt4g.org/movie/search/{query}/{page}/'
		self._music = 'https://bt4g.org/audio/search/{query}/{page}/'
		self._software = 'https://bt4g.org/app/search/{query}/{page}/'
		self._other = 'https://bt4g.org/other/search/{query}/{page}/'
		
		self._normal = 'https://bt4g.org/search/{query}/{page}/'
		
		
		
		self._categories = {
			'movie': self._movie, 
			'tv': self._normal, 
			'music': self._music, 
			'software': self._software, 
			'game': self._normal, 
			'anime': self._normal, 
			'other': self._other, 
			None: self._normal
		    }
	
	
	
	def search(self, query, category=None, limit=15, magnet=False, add_engine_name=False):
		query = query.replace(' ', '%20')
		
		
		last = 1
		found = 0
		results = []
		
		
		
		while found < limit:
			resp = _session.get(self._categories[category].format(query=query, page=last))
			
			if not resp.ok and resp.status_code not in [404]:
				return
			
			soup = _soup(resp.text)
			
			
			torrentList = [x.parent for x in soup.select('h5')]
			
			
			
			if torrentList:
				for torrent in torrentList:
					link, name = ('https://bt4g.org' + _i.get('href'), _i.getText()) if (_i := torrent.select('a')[0]) else (None, None)
					leechers, seeders, size, time = (_i[-1].select('b')[0].getText(), _i[-2].select('b')[0].getText(), _i[-3].select('b')[0].getText(), _i[-5].select('b')[0].getText()) if (_i := torrent.select('span')) else (None, None, None, None)
					
					
					results.append({'name': name, 'link': link, 'seeders': seeders, 'leechers': leechers, 'size': size, 'time': time, 'magnet': get_magnet(link)})
					
					
					if add_engine_name:
						results[-1].update({'engine': 'bt4g'})
					
					found += 1
					
					if found >= limit:
						break
				
				last += 1
			
							
			else:
				break
		
		return results[:limit]














class engine_limetorrents:
	def __init__(self):
		self._movie = 'https://limetorrents.pro/search/movies/{query}/{page}/'
		self._tv = 'https://limetorrents.pro/search/tv/{query}/{page}/'
		self._music = 'https://limetorrents.pro/search/music/{query}/{page}/'
		self._anime = 'https://limetorrents.pro/search/anime/{query}/{page}/'
		self._game = 'https://limetorrents.pro/search/games/{query}/{page}/'
		self._software = 'https://limetorrents.pro/search/applications/{query}/{page}/'
		self._other = 'https://limetorrents.pro/search/other/{query}/{page}/'
		
		self._normal = 'https://limetorrents.pro/search/all/{query}/{page}/'
		
		
		
		self._categories = {
			'movie': self._movie, 
			'tv': self._tv, 
			'music': self._music, 
			'software': self._software, 
			'game': self._game, 
			'anime': self._anime, 
			'other': self._other, 
			None: self._normal
		    }
	
	
	
	def search(self, query, category=None, limit=15, magnet=False, add_engine_name=False):
		query = query.replace(' ', '-')
		
		
		last = 1
		found = 0
		results = []
		
		
		
		while found < limit:
			resp = _session.get(self._categories[category].format(query=query, page=last))
			
			if not resp.ok and resp.status_code not in [404]:
				return
			
			soup = _soup(resp.text)
			
			
			torrentList = soup.select('tr')[5:]
			
			
			
			if torrentList:
				for torrent in torrentList:
					link, name = (_i[0].get('href'), _i[1].getText().strip()) if (_i := torrent.select('a')) else (None, None)
					
					time, size, seeders, leechers = (_i[1].getText().strip(), _i[2].getText().strip(), _i[3].getText().strip(), _i[4].getText().strip()) if (_i := torrent.select('td')) else (None, None, None, None)
					
					
					
					results.append({'name': name, 'link': link, 'seeders': seeders, 'leechers': leechers, 'size': size, 'time': time, 'magnet': get_magnet(link)})
					
					
					if add_engine_name:
						results[-1].update({'engine': 'limetorrents'})
					
					found += 1
					
					if found >= limit:
						break
				
				last += 1
			
							
			else:
				break
		
		return results[:limit]

















class engine_zooqle:
	def __init__(self):
		self._normal = 'https://zooqle.com/search?pg={page}&q={query}&v=t'
		
		
		
		self._categories = {
			'movie': self._normal, 
			'tv': self._normal, 
			'music': self._normal, 
			'software': self._normal, 
			'game': self._normal, 
			'anime': self._normal, 
			'other': self._normal, 
			None: self._normal
		    }
	
	
	
	def search(self, query, category=None, limit=15, magnet=False, add_engine_name=False):
		query = query.replace(' ', '+')
		
		
		last = 1
		found = 0
		results = []
		
		
		
		while found < limit:
			resp = _session.get(self._categories[category].format(query=query, page=last))
			
			if not resp.ok and resp.status_code not in [404]:
				return
			
			soup = _soup(resp.text)
			
			
			torrentList = soup.select('tr')[1:]
			categories_matchmake = {
				'movie': 'movie', 
				'tv': 'tv', 
				'music': 'audio', 
				'software': 'app', 
				'game': 'game', 
				'anime': 'anime', 
				'other': '', 
				None: ''
				    }
			
			
			
			if torrentList:
				for torrent in torrentList:
					right_category = None
					
					try:
							right_category = True if categories_matchmake[category] in torrent.select('i')[0].get('class')[1].split('-')[1] else False
					
					except:
						right_category = False
						
						if str(torrent) == '<tr><td class="text-muted small" colspan="7">No torrents found.</td></tr>':
							return results
						
						
					
					
					if right_category:
						link, name = ('https://zooqle.com' + _i.get('href'), _i.getText()) if (_i := torrent.select('a')[0]) else (None, None)
						
						
						seeders, leechers = (sl_[0].strip().split()[1], sl_[1].strip().split()[1]) if (sl_ := torrent.select('div[title^="Seeders"]')[0].get('title').split('|')) else (None, None)
						size = size_[0].getText() if (size_ := torrent.select('div[class^="progress-bar prog-blue prog-l"]')) else None
						time = torrent.select('td[class="text-nowrap text-muted smaller"]')[0].getText()
						magnet = torrent.select('a[href^="magnet"]')[0].get('href')
						
						results.append({'name': name, 'link': link, 'seeders': seeders, 'leechers': leechers, 'size': size, 'time': time, 'magnet': magnet})
						
						
						if add_engine_name:
							results[-1].update({'engine': 'zooqle'})
						
						found += 1
					
						if found >= limit:
							break
				
				last += 1
			
							
			else:
				break
		
		return results[:limit]


















class engine_piratebay:
	def __init__(self):
		self._movie = 'https://knaben.ru/s/?search/{query}/{page}/99/200'
		self._music = 'https://knaben.ru/s/?search/{query}/{page}/99/100'
		self._game = 'https://knaben.ru/s/?search/{query}/{page}/99/400'
		self._software = 'https://knaben.ru/s/?search/{query}/{page}/99/300'
		self._other = 'https://knaben.ru/s/?search/{query}/{page}/99/600'
		
		self._normal = 'https://knaben.ru/s/?search/{query}/{page}/99/0'
		
		
		
		self._categories = {
			'movie': self._movie, 
			'tv': self._movie, 
			'music': self._music, 
			'software': self._software, 
			'game': self._game, 
			'anime': self._movie, 
			'other': self._other, 
			None: self._normal
		    }
	
	
	
	def search(self, query, category=None, limit=15, magnet=False, add_engine_name=False):
		query = query.replace(' ', '%20')
		
		
		last = 1
		found = 0
		results = []
		
		
		
		while found < limit:
			resp = _session.get(self._categories[category].format(query=query, page=last))
			
			if not resp.ok and resp.status_code not in [404]:
				return
			
			soup = _soup(resp.text)
			
			
			torrentList = soup.select('tr')[1:-1]
			
			
			if torrentList:
				for count, torrent in enumerate(torrentList):
					link, name = ('https://knaben.ru' + _i.get('href'), _i.getText()) if (_i := torrent.select('a')[2]) else (None, None)
					time, size = (_i.group(1).replace(' ', ' '), _i.group(2).replace(' ', ' ')) if (_i := _re.match('Uploaded (.*), Size (.*),', torrent.select('font')[0].getText())) else (None, None)
					seeders, leechers = (_i[2].getText(), _i[3].getText()) if (_i := torrent.select('td')) else (None, None)
					magnet = torrent.select('a[href^="magnet"]')[0].get('href')
					
					
					results.append({'name': name, 'link': link, 'seeders': seeders, 'leechers': leechers, 'size': size, 'time': time, 'magnet': magnet})
					
					
					if add_engine_name:
						results[-1].update({'engine': 'piratebay'})
					
					
					found += 1
					
					if found >= limit:
						break
					
				last += 1
			
							
			else:
				break
		
		return results[:limit]

















class engine_torrentdownload:
	def __init__(self):
		self._normal = 'https://torrentdownload.info/search?q={query}&p={page}'
		
		
		
		self._categories = {
			'movie': self._normal, 
			'tv': self._normal, 
			'music': self._normal, 
			'software': self._normal, 
			'game': self._normal, 
			'anime': self._normal, 
			'other': self._normal, 
			None: self._normal
		    }
	
	
	
	def search(self, query, category=None, limit=15, magnet=False, add_engine_name=False):
		query = query.replace(' ', '%20')
		
		
		last = 1
		found = 0
		results = []
		
		
		
		while found < limit:
			resp = _session.get(self._categories[category].format(query=query, page=last))
			
			if not resp.ok and resp.status_code not in [404]:
				return
			
			soup = _soup(resp.text)
			
			
			torrentList = soup.select('tr')[5:]
			
			
			if torrentList:
				for count, torrent in enumerate(torrentList):
					link, name = ('https://torrentdownload.info' + _i.get('href'), _i.getText()) if (_i := torrent.select('a')[0]) else (None, None)
					time, size, seeders, leechers = (_i[1].getText(), _i[2].getText(), _i[3].getText(), _i[4].getText()) if (_i := torrent.select('td')) else (None, None, None, None)
					magnet = torrent.select('a')[0].get('href').split('/')[1]
					
					
					results.append({'name': name, 'link': link, 'seeders': seeders, 'leechers': leechers, 'size': size, 'time': time, 'magnet': _hash2magnet(magnet)})
					
					
					
					if add_engine_name:
						results[-1].update({'engine': 'torrentdownload'})
					
					
					found += 1
					
					if found >= limit:
						break
					
				last += 1
			
							
			else:
				break
		
		return results[:limit]


















class engine_nyaa:
	def __init__(self):
		self._music = 'https://nyaa.si/?q={query}&f=0&c=2_0&p={page}'
		self._anime = 'https://nyaa.si/?q={query}&f=0&c=1_0&p={page}'
		self._game = 'https://nyaa.si/?q={query}&f=0&c=6_2&p={page}'
		self._software = 'https://nyaa.si/?q={query}&f=0&c=6_1&p={page}'
		
		
		self._normal = 'https://nyaa.si/?q={query}&f=0&c=0_0&p={page}'
		
		
		
		self._categories = {
			'movie': self._normal, 
			'tv': self._normal, 
			'music': self._music, 
			'software': self._software, 
			'game': self._game, 
			'anime': self._anime, 
			'other': self._normal, 
			None: self._normal
		    }
	
	
	
	def search(self, query, category=None, limit=15, magnet=False, add_engine_name=False):
		query = query.replace(' ', '+')
		
		
		last = 1
		found = 0
		results = []
		
		
		
		while found < limit:
			resp = _session.get(self._categories[category].format(query=query, page=last))
			
			if not resp.ok and resp.status_code not in [404]:
				return
			
			soup = _soup(resp.text)
			
			
			torrentList = soup.select('tr')[1:]
			
			
			
			if torrentList:
				for torrent in torrentList:
					link, name = ('https://nyaa.si' + _i.get('href').replace('#comments', ''), _i.get('title')) if (_i := torrent.select('a')[1]) else (None, None)
					size, time, seeders, leechers = (_i[3].getText(), _i[4].getText(), _i[5].getText(), _i[6].getText()) if (_i := torrent.select('td')) else (None, None, None, None)
					magnet = torrent.select('a[href^="magnet"]')[0].get('href')
					
					
					results.append({'name': name, 'link': link, 'seeders': seeders, 'leechers': leechers, 'size': size, 'time': time, 'magnet': magnet})
					
					
					if add_engine_name:
						results[-1].update({'engine': 'nyaa'})
					
					found += 1
					
					if found >= limit:
						break
				
				last += 1
			
							
			else:
				break
		
		return results[:limit]




















class engine_magnetdl:
	def __init__(self):
		self._normal = 'https://magnetdl.com/{query:.1}/{query}/{page}/'
		
		
		
		self._categories = {
			'movie': self._normal, 
			'tv': self._normal, 
			'music': self._normal, 
			'software': self._normal, 
			'game': self._normal, 
			'anime': self._normal, 
			'other': self._normal, 
			None: self._normal
		    }
	
	
	
	def search(self, query, category=None, limit=15, magnet=False, add_engine_name=False):
		query = query.replace(' ', '-')
		
		
		last = 1
		found = 0
		results = []
		
		
		
		while found < limit:
			resp = _session.get(self._categories[category].format(query=query, page=last))
			
			if not resp.ok and resp.status_code not in [404]:
				return
			
			soup = _soup(resp.text)
			
			
			torrentList = [x.parent for x in soup.select('td[class="m"]')]
			categories_matchmake = {
				'movie': 'movie', 
				'tv': 'tv', 
				'music': 'music', 
				'software': 'software', 
				'game': 'game', 
				'anime': 'tv', 
				'other': 'other', 
				None: ''
				    }
			
			
			
			if torrentList:
				for torrent in torrentList:
					right_category = None
					
					try:
							right_category = True if categories_matchmake[category] in torrent.select('td')[3].getText().lower() else False
					
					except:
						right_category = False
					
					
					
					
					if right_category:
						link, name = ('https://magnetdl.com' + _i.get('href'), _i.get('title')) if (_i := torrent.select('a')[1]) else (None, None)
						time, size, seeders, leechers = (_i[2].getText(), _i[5].getText(), _i[6].getText(), _i[7].getText()) if (_i := torrent.select('td')) else (None, None, None, None)
						magnet = torrent.select('a[href^="magnet"]')[0].get('href')
						
						
						results.append({'name': name, 'link': link, 'seeders': seeders, 'leechers': leechers, 'size': size, 'time': time, 'magnet': magnet})
						
						
						if add_engine_name:
							results[-1].update({'engine': 'magnetdl'})
						
						found += 1
					
						if found >= limit:
							break
				
				last += 1
			
							
			else:
				break
		
		
		return results[:limit]


















class engine_uniondht:
	def __init__(self):
		self._normal = 'http://uniondht.org/tracker.php?nm={query}&start={page}'
		
		
		
		self._categories = {
			'movie': self._normal, 
			'tv': self._normal, 
			'music': self._normal, 
			'software': self._normal, 
			'game': self._normal, 
			'anime': self._normal, 
			'other': self._normal, 
			None: self._normal
		    }
	
	
	
	def search(self, query, category=None, limit=15, magnet=False, add_engine_name=False):
		query = query.replace(' ', '+')
		
		
		last = 0
		found = 0
		results = []
		
		
		
		while found < limit:
			resp = _session.get(self._categories[category].format(query=query, page=last))
			
			if not resp.ok and resp.status_code not in [404]:
				return
			
			soup = _soup(resp.text)
			
			
			torrentList = soup.select('tr[class="tCenter hl-tr"]')
			
			
			
			if torrentList:
				for torrent in torrentList:
					link, name = ('http://uniondht.org' + _i.get('href'), _i.parent.getText().strip()) if (_i := torrent.select('a[class="genmed2 tLink"]')[0]) else (None, None)
					seeders = torrent.select('td[class^="row4 seedmed"]')[0].getText()
					leechers = torrent.select('td[class^="row4 leechmed"]')[0].getText()
					size = torrent.select('a[class="small tr-dl"]')[0].getText().replace(' ', ' ')
					
					
					time = torrent.select('td[class="row4 small nowrap"]')[1]
					time.select('u')[0].replace_with('')
					time = time.getText().replace('\n', ' ').strip()
					
					
					
					results.append({'name': name, 'link': link, 'seeders': seeders, 'leechers': leechers, 'size': size, 'time': time})
					
					
					if magnet == True:
						results[-1].update({'magnet': get_magnet(link)})
					
					if add_engine_name:
						results[-1].update({'engine': 'uniondht'})
					
					found += 1
					
					if found >= limit:
						break
				
				last += 50
			
							
			else:
				break
		
		return results[:limit]




















class engine_torlock:
	def __init__(self):
		self._movie = 'https://torlock.com/movie/torrents/{query}.html'
		self._tv = 'https://torlock.com/television/torrents/{query}.html'
		self._music = 'https://torlock.com/music/torrents/{query}.html'
		self._anime = 'https://torlock.com/anime/torrents/{query}.html'
		self._game = 'https://torlock.com/game/torrents/{query}.html'
		self._software = 'https://torlock.com/software/torrents/{query}.html'
		self._other = 'https://torlock.com/unknown/torrents/{query}.html'
		
		self._normal = 'https://torlock.com/all/torrents/{query}.html'
		
		
		
		self._categories = {
			'movie': self._movie, 
			'tv': self._tv, 
			'music': self._music, 
			'software': self._software, 
			'game': self._game, 
			'anime': self._anime, 
			'other': self._other, 
			None: self._normal
		    }
	
	
	
	def search(self, query, category=None, limit=15, magnet=False, add_engine_name=False):
		query = query.replace(' ', '%20')
		
		
		found = 0
		results = []
		
		
		
		while found < limit:
			resp = _session.get(self._categories[category].format(query=query))
			
			if not resp.ok and resp.status_code not in [404]:
				return
			
			soup = _soup(resp.text)
			
			
			torrentList = soup.select('tr')[5:]
			
			
			
			
			if torrentList:
				for count, torrent in enumerate(torrentList):
					link, name = ('https://torlock.com' + _i.get('href'), _i.getText()) if (_i := torrent.select('a')[0]) else (None, None)
					time, size, seeders, leechers = (_i[1].getText(), _i[2].getText(), _i[3].getText(), _i[4].getText()) if (_i := torrent.select('td')) else (None, None, None, None)
					
					
					results.append({'name': name, 'link': link, 'seeders': seeders, 'leechers': leechers, 'size': size, 'time': time})
					
					
					if magnet == True:
						results[-1].update({'magnet': get_magnet(link)})
					
					if add_engine_name:
						results[-1].update({'engine': 'torlock'})
					
					
					found += 1
					
					if found >= limit:
						break
					
				break
			
							
			else:
				break
		
		return results[:limit]




















class engine_torrentdownloads:
	def __init__(self):
		self._normal = 'https://torrentdownloads.pro/search/?page={page}&search={query}'
		
		
		
		self._categories = {
			'movie': self._normal, 
			'tv': self._normal, 
			'music': self._normal, 
			'software': self._normal, 
			'game': self._normal, 
			'anime': self._normal, 
			'other': self._normal, 
			None: self._normal
		    }
	
	
	
	def search(self, query, category=None, limit=15, magnet=False, add_engine_name=False):
		query = query.replace(' ', '+')
		
		
		last = 1
		found = 0
		results = []
		
		
		
		while found < limit:
			resp = _session.get(self._categories[category].format(query=query, page=last))
			
			if not resp.ok and resp.status_code not in [404]:
				return
			
			soup = _soup(resp.text)
			
			
			torrentList = [_i for x in soup.select('a[href^="/torrent"]') if (_i := x.parent).name == 'div'] if (last > 1) else [_i for x in soup.select('a[href^="/torrent"]') if (_i := x.parent).name == 'div'][1:]
			
			
			
			
			if torrentList:
				for count, torrent in enumerate(torrentList):
					link, name = ('https://torrentdownloads.pro' + _i.get('href'), _i.getText()) if (_i := torrent.select('a[href^="/torrent"]')[0]) else (None, None)
					leechers, seeders, size, time = (_i[1].getText(), _i[2].getText(), _i[3].getText().replace(' ', ' '), None) if (_i := torrent.select('span')) else (None, None, None, None)
					
					
					results.append({'name': name, 'link': link, 'seeders': seeders, 'leechers': leechers, 'size': size, 'time': time})
					
					
					if magnet == True:
						results[-1].update({'magnet': get_magnet(link)})
					
					if add_engine_name:
						results[-1].update({'engine': 'torrentdownloads'})
					
					
					found += 1
					
					if found >= limit:
						break
					
				last += 1
			
							
			else:
				break
		
		return results[:limit]


















class engine_kickasstorrents:
	def __init__(self):
		self._movie = 'https://kickass.onl/usearch/{query}%20category:movies/{page}'
		self._tv = 'https://kickass.onl/usearch/{query}%20category:tv/{page}'
		self._music = 'https://kickass.onl/usearch/{query}%20category:music/{page}'
		self._game = 'https://kickass.onl/usearch/{query}%20category:games/{page}'
		self._software = 'https://kickass.onl/usearch/{query}%20category:applications/{page}'
		
		self._normal = 'https://kickass.onl/usearch/{query}/{page}'
		
		
		
		self._categories = {
			'movie': self._movie, 
			'tv': self._tv, 
			'music': self._music, 
			'software': self._software, 
			'game': self._game, 
			'anime': self._normal, 
			'other': self._normal, 
			None: self._normal
		    }
	
	
	
	def search(self, query, category=None, limit=15, magnet=False, add_engine_name=False):
		query = query.replace(' ', '%20')
		
		
		last = 1
		found = 0
		results = []
		
		
		
		while found < limit:
			resp = _session.get(self._categories[category].format(query=query, page=last))
			
			if not resp.ok and resp.status_code not in [404]:
				return
			
			soup = _soup(resp.text)
			
			
			torrentList = soup.select('tr[id="torrent_latest_torrents"]')
			
			
			
			if torrentList:
				for count, torrent in enumerate(torrentList):
					link, name = ('https://kickass.onl' + _i.get('href'), _i.getText()) if (_i := torrent.select('a[class="cellMainLink"]')[0]) else (None, None)
					size, time, seeders, leechers = (_i[1].getText(), _i[2].getText(), _i[3].getText(), _i[4].getText()) if (_i := torrent.select('td')) else (None, None, None, None)
					magnet = _hash2magnet(_magnet2hash(_unquote(torrent.select('a[title="Download torrent file"]')[0].get('href')).split('https://mylink.cx/?url=')[1]))
					
					
					results.append({'name': name, 'link': link, 'seeders': seeders, 'leechers': leechers, 'size': size, 'time': time, 'magnet': magnet})
					
					
					
					if add_engine_name:
						results[-1].update({'engine': 'kickasstorrents'})
					
					
					found += 1
					
					if found >= limit:
						break
					
				last += 1
			
							
			else:
				break
		
		return results[:limit]




















Engines = [engine_1337x, 
engine_solidtorrents, 
engine_bt4g, 
engine_limetorrents, 
engine_zooqle, 
engine_piratebay, 
engine_torrentdownload, 
engine_nyaa, 
engine_magnetdl, 
engine_uniondht, 
engine_torlock, 
engine_torrentdownloads, 
engine_kickasstorrents]




def search(query, category=None, limit=15, magnet=False, exclude_same=True, engines=Engines):
	pool = _Pool(len(engines))
	processes = []
	
	
	for engine in engines:
		x = engine()
		
		processes.append(pool.apply_async(x.search, kwds={'query': query, 'category': category, 'limit': limit, 'magnet': magnet, 'add_engine_name': True}))
	
	
	responses = []
	for process in processes:
		responses.append(process.get())
	
	
	results = []
	hash_found = [] 
	
	
	if exclude_same:
		for x in responses:
			try:
				for torrent in x:
					magnet = torrent.get('magnet', None)
					
					if magnet:
						hash = _magnet2hash(magnet)
						
						if hash not in hash_found:
							hash_found.append(hash)
							results.append(torrent)
					
					else:
						results.append(torrent)
			
			except:
				pass
		
		
		return results
	
	
	else:
		for x in responses:
			for torrent in x:
				results.append(torrent)
		
		return results