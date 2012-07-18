import pyaudio
import wave
import sys

chunk = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
RECORD_SECONDS = 7

p = pyaudio.PyAudio()

def record(filename):
	stream = p.open(format = FORMAT,
                	channels = CHANNELS,
                	rate = RATE,
                	input = True,
                	frames_per_buffer = chunk)

	print "* recording"
	all = []
	for i in range(0, RATE / chunk * RECORD_SECONDS):
	    data = stream.read(chunk)
	    all.append(data)
	print "* done recording"

	stream.close()
	p.terminate()

	# write data to WAVE file
	data = ''.join(all)
	wf = wave.open(filename, 'wb')
	wf.setnchannels(CHANNELS)
	wf.setsampwidth(p.get_sample_size(FORMAT))
	wf.setframerate(RATE)
	wf.writeframes(data)
	wf.close()
