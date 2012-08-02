import time
from hotqueue import HotQueue
#queue = HotQueue("wekkie:play")
#queue.put("spotify:track:5sfZIwTZ9yyRVbmA8wBkm8")

queue_time = HotQueue("wekkie:time")
queue_uri  = HotQueue("wekkie:uri")

def main():

	while True:
		print "VIS!!!"
		print queue_time.get()
		print queue_uri.get()
		time.sleep(1);
		
if __name__ == '__main__':
	main()