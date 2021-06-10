# Import modules

import subprocess


# Opens a browser link

def OpenBrowser(URL):
	if not URL.startswith('http'):
		URL = 'http://' + URL
	subprocess.call('start ' + URL, shell=True)