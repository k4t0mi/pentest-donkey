# Import modules

import re
import json
import subprocess
import urllib.request


# MAC address regex

macRegex = re.compile('[0-9a-f]{2}([-:]?)[0-9a-f]{2}(\\1[0-9a-f]{2}){4}$')


# Get router ip address

Command = 'chcp 65001 && ipconfig | findstr /i \"Default Gateway\"'

subprocess.check_output(Command,
	shell=True, stderr=subprocess.DEVNULL, stdin=subprocess.DEVNULL)


# Get mac by local ip

def GetMacByIP():
	a = subprocess.check_output('arp -a',
		shell=True, stderr=subprocess.DEVNULL, stdin=subprocess.DEVNULL)
	b = a.decode(encoding='cp866')
	c = b.find('')
	d = b[c:].split(' ')
	for b in d:
		if macRegex.match(b):
			return b.replace('-', ':')


# Locate by BSSID

def GetLocationByBSSID(BSSID):
	try:
		Result = urllib.request.urlopen(f'http://api.mylnikov.org/geolocation/wifi?bssid={BSSID}').read().decode('utf8')
	except:
		return None
	else:
		Result = json.loads(Result)
		return Result['data']