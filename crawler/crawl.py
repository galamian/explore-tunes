#!/usr/bin/python

import sys
import requests
from bs4 import BeautifulSoup as bs

# gibt html code der gewünschten url zurück
def get_url_content(url):
    return requests.get(url).text

if len(sys.argv)>1:
	tune_id = sys.argv[1] if sys.argv[1] else '1'
else:
	print('no tune_id passed as parameter')
	tune_id = '1'

url = 'https://www.folktunefinder.com/tunes/' + tune_id



content = get_url_content(url)

soup = bs(content, "html.parser")

abc = soup.find('pre')

if abc:
	fname = tune_id + '.abc'
	with open(fname,"w") as out:
		#try:
            		out.write(soup.find('pre').text)
        	#except Exception:
            	#	pass
		#print(soup.find('pre').text)
else:
	print('No tune found for Id', tune_id)

#for s in soup.find_all('pre'):
#	print(s.text)
