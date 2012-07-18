#!/usr/bin/python

import sys
import os, base64
import time
import datetime
from hotqueue import HotQueue

queue_time = HotQueue("wekkie:time")
queue_uri  = HotQueue("wekkie:uri")
queue_play = HotQueue("wekkie:play")

def main():
	alarm_time = None
	alarm_uri  = None

	while True:
		alarm_time_new = queue_time.get()
		alarm_uri_new  = queue_uri.get()
		
		if alarm_uri_new and alarm_uri_new != alarm_uri:
			alarm_uri = alarm_uri_new

		now = datetime.datetime.now()
		if alarm_time_new and alarm_time_new != alarm_time and alarm_time_new > now:
			alarm_time = alarm_time_new
			print "Alarm gaat op", alarm_time, "met", alarm_uri
		
		if alarm_time and now >= alarm_time:
			print "Nu dus afgaan!!"
			queue_play.put(alarm_uri)
			alarm_time = None
			
		print now.strftime("%d-%m-%y %H:%M:%S")
		time.sleep(1)

if __name__ == '__main__':
	main()