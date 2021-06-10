# Import modules

import json
import datetime
import platform
import subprocess
import urllib.request


# Windows Version

def Windows():
	System = platform.system()
	Release = platform.release()
	Version = System + ' ' + Release
	return Version


# System Information

def Computer(Win32, Value):
	a = subprocess.check_output('wmic ' + Win32 + ' get ' + Value,
		shell=True, stderr=subprocess.DEVNULL, stdin=subprocess.DEVNULL)
	b = a.decode('utf-8')
	c = b.split('\n')
	return c[1]


# Computer RAM

def RAM():
	Size = Computer('ComputerSystem', 'TotalPhysicalMemory')
	intSize = int(Size) / 1024 / 1024 / 1024
	return intSize


# Getting the set computer time

def SystemTime():
	Today = datetime.datetime.today()
	SystemTime = str(Today.hour) + ':'+str(Today.minute) + ':' + str(Today.second)
	return SystemTime


# Getting location via IP Address

def Geolocation(Value, Ip=''):
	try:
		Result = urllib.request.urlopen(f'http://ip-api.com/json/{Ip}').read().decode('utf-8')
	except:
		return None
	else:
		Result = json.loads(Result)
		return Result[Value]