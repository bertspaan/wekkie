import sys
from pyechonest import artist
from pyechonest import config

# Documentation:
# http://developer.echonest.com/docs/v4/artist.html#extract-beta

config.ECHO_NEST_API_KEY="L378WBLE4UNJTEU7Z"

def parse(text):
	# TODO: Return only hotttest artist? Or list of artists?
	# TODO: Remove text containing time string  
	results = artist.extract(text=text, limit=False, buckets="id:spotify-WW")
	artist_uri = None
	hotttnesss_max = 0
	for result in results:		
		hotttnesss = result.get_hotttnesss()
		if hotttnesss > hotttnesss_max:
			hotttnesss_max = hotttnesss
			spotify_ww = result.get_foreign_id(idspace="spotify-WW")
			if spotify_ww:
				artist_uri = spotify_ww.replace("spotify-WW", "spotify")
	return artist_uri