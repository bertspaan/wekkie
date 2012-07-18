import re
import pyPEG
from pyPEG import parse, parseLine
from pyPEG import keyword, _and, _not, ignore

import datetime

min_words = 1
max_words = 4
numbers = [
	"nul",
	"een",
	"twee",
	"drie",
	"vier",
	"vijf",
	"zes",
	"zeven",
	"acht",
	"negen",
	"tien",
	"elf",
	"twaalf",
	"dertien",
	"veertien",
	"vijftien",
	"zestien",
	"zeventien",
	"achttien",
	"negentien",
	"twintig",
	"eenentwintig",
	"tweeentwintig",
	"drieentwintig",
	"vierentwintig",
	"vijfentwintig",
	"zesentwintig",
	"zevenentwintig",
	"achtentwintig",
	"negenentwintig",
	"dertig",
	"eenendertig",
	"tweeendertig",
	"drieendertig",
	"vierendertig",
	"vijfendertig",
	"zesendertig",
	"zevenendertig",
	"achtendertig",
	"negenendertig",
	"veertig",
	"eenenveertig",
	"tweeenveertig",
	"drieenveertig",
	"vierenveertig",
	"vijfenveertig",
	"zesenveertig",
	"zevenenveertig",
	"achtenveertig",
	"negenenveertig",
	"vijftig",
	"eenenvijftig",
	"tweeenvijftig",
	"drieenvijftig",
	"vierenvijftig",
	"vijfenvijftig",
	"zesenvijftig",
	"zevenenvijftig",
	"achtenvijftig",
	"negenenvijftig",	
	"zestig"	
]

QUARTER = "kwart"

def number():	return re.compile(r"\w+")
def half():		return re.compile(r"half")
def hours():	return -1, half, number, -1, keyword("uur")
def sign():		return [re.compile(r"voor"), re.compile(r"over")]
def minutes():	return number
def time():		return [		
					(minutes, sign, hours),
					(hours, -1, ":", minutes),
					hours
				]

def string_to_int(str):
	if str == QUARTER:
		return 15		
	for i in range(0, 60):
		if str == numbers[i]:
			return i
	
	try:
		return int(str)
	except ValueError:
		return None

def to_time(ast):
	minutes_str = ""
	hours_str = ""
	half = False
	sign = 1
	
	# ast is tuple (ast, ''). skip weird '' part:
	ast = ast[0]

	for symbol in ast:
		name = symbol[0]
		value = symbol[1]
		if name == "hours":
			if len(value) == 2:
				# Has 'half'
				half = True
				hours_str = value[1][1]
			else:
				hours_str = value[0][1]
		elif name == "minutes":
			minutes_str = value[0][1]
		elif name == "sign":
			if value[0] == "voor":
				sign = -1

	minutes = 0

	try:
		if len(hours_str) > 0:
			minutes = string_to_int(hours_str) * 60

		if half:
			minutes -= 30
		
		if len(minutes_str) > 0:
			minutes += sign * string_to_int(minutes_str)

		hours = minutes // 60
		minutes = minutes - (60 * hours)
		
		#hours_now
		#minutes_now
	
		today = datetime.date.today() #+ datetime.timedelta(days=1)
		return datetime.datetime.combine(today, datetime.time(hours, minutes))
		
	except TypeError:
		return None

def parse_time(time_str):
	ast = parseLine(textline=time_str, pattern=time(), resultSoFar=[])	
	return to_time(ast) 

def parse(text, try_substrings=True):
	if try_substrings:
		split = text.split(" ")
		substrings = []
		for i in range(0, len(split)):
			for j in range(min_words, max_words + 1):
				start = i
				end = i + j
				if end <= len(split):
					substrings.append(split[start:end])
		substrings.sort(lambda x,y: cmp(len(y), len(x)))
		
		time = None
		substrings = [" ".join(words) for words in substrings]
		for substring in substrings:
			time = parse_time(substring)
			if time:
				break
		return time
	else:
		return parse_time(text)