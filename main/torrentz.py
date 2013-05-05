import requests
import re
import json
import itertools

torrent_api_url = "http://apify.ifc0nfig.com/tpb/search/"

def get_links(title):
	try:
		data = requests.get(torrent_api_url + title)
	except Exception, e:
		raise e
	episodes = []
	for item in data.json:
		m = re.search(r'^([\w\s]+)S([\d]+)E([\d]+)', item.get("name"))
		if m:
			episodes.append({"title":m.group(1), "season":m.group(2), "episode":m.group(3), \
				"magnet":item.get("magnet"), "size":item.get("size"), "seeders":item.get("seeders"), "leechers":item.get("leechers")})
			#print "name: " + m.group(1) + "  season: " + m.group(2) + " episode: " + m.group(3)
	seen_episodes = set()
	new_list = []
	for obj in episodes:
		if obj.get("episode") not in seen_episodes:
			new_list.append(obj)
			seen_episodes.add(obj.get("episode"))
	return json.dumps(sorted(new_list, key=lambda x: x.get("episode"), reverse=True)[:10], sort_keys=True)