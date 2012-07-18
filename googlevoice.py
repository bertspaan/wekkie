import pysox
import urllib
import requests

#import logging
#requests_log = logging.getLogger("requests")
#requests_log.setLevel(logging.WARNING)

from subprocess import call

rate = "44100"

headers = {
	"Content-Type": "audio/x-flac; rate=" + rate
}

url = "http://www.google.com/speech-api/v1/recognize"

def wav_to_flac(filename, flac_filename, pysox=False):
	if pysox:
		wav = pysox.CSoxStream(filename)
		flac = pysox.CSoxStream(flac_filename, 'w', wav.get_signal())	
		chain = pysox.CEffectsChain(wav, flac)
		chain.flow_effects()
		flac.close()
	else:
		call(["sox", filename, flac_filename, "rate", rate])

def recognize(filename, lang="nl-nl"):
	flac_filename = filename.replace(".wav", ".flac")
	wav_to_flac(filename, flac_filename)
	
	params = {
		"lang": lang,
		"client": "chromium"
	}
	
	url_with_params = "%s?%s" % (url, urllib.urlencode(params))
	print url_with_params
	r = requests.post(url_with_params, files={'file': open(flac_filename,'rb')}, headers=headers)

	json = r.json
	print json
	if json and len(json["hypotheses"]):
		return json["hypotheses"][0]["utterance"]

	return None