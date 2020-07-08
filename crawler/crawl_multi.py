#!/usr/bin/python

import sys
import requests
from bs4 import BeautifulSoup as bs

# gibt html code der gewünschten url zurück
def get_url_content(url):
    return requests.get(url).text

def crawl_tune_by_id(tune_id):
	url = 'https://www.folktunefinder.com/tunes/' + tune_id
	content = get_url_content(url)
	soup = bs(content, "html.parser")
	abc = soup.find('pre')

	if abc:
		fname = '../data/raw/' + tune_id + '.abc'
		with open(fname,"w") as out:
			out.write(soup.find('pre').text)
	else:
		print('No tune found for Id', tune_id)

tuid_from, tuid_to = 1, 1

if len(sys.argv)>1:
	tuid_from = sys.argv[1] if sys.argv[1] else '1'
	if len(sys.argv)>2:
		tuid_to = sys.argv[2] if sys.argv[2] else tuid_from	
else:
	print('no tune_ids passed as parameter')

for tuid in range(int(tuid_from), int(tuid_to)):
	crawl_tune_by_id(str(tuid))


