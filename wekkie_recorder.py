#!/usr/bin/python

import sys
import parsetime, parseartist, googlevoice, soundrecorder
import os, base64
from hotqueue import HotQueue
from optparse import OptionParser

test_times = [
	"12 56",
	"12:56",
	"twaalf dertig",
	"negen vijftien",
	"kwart voor twee",
	"tien voor twee",
	"drie over half tien",
	"13 uur 52",
	"half drie",
	"zevenenveertig over tien",
	"zeven voor half vier",
	"achttien vijftien",
	"zeven",
	"negen uur",
	"8 uur",
	"achttien uur vijftien"
]

def main():
	parser = OptionParser(usage="usage: %prog [options]",
                          version="%prog 1.0")
	parser.add_option("-f", "--filename",
                      dest="filename",
                      help="Use prerecorded audio file")
	parser.add_option("-s", "--string",
                      dest="string",
                      help="Use custom string",)
    
	(options, args) = parser.parse_args()

	text = None
	if options.string:
		text = options.string
	elif options.filename:
		text = googlevoice.recognize(options.filename)
	else:
		# Record audio:
		var = raw_input("Druk <Enter> om de opname te starten: ")
		filename = "tmp/recordings/%s.wav" % base64.b64encode(os.urandom(6)).replace("/", "")
		soundrecorder.record(filename)
		text = googlevoice.recognize(filename)
	
	if text:
		text = text.lower()
		time = parsetime.parse(text)
		artist_uri = parseartist.parse(text)

		# TODO: read Spotify user from properties
		default_uri = "spotify:user:bertspaan:starred"
		if not artist_uri:			
			artist_uri = default_uri

		print "Alarm:", time, "with", artist_uri

		if time:
			queue_time = HotQueue("wekkie:time")
			queue_time.put(time)
		if artist_uri:			
			queue_spotify_uri = HotQueue("wekkie:uri")
			queue_spotify_uri.put(artist_uri)

if __name__ == '__main__':
    main()
