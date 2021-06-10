# Import modules

import time
import ctypes


# Blocks mouse and keyboard movements

def Block(Seconds):
	ctypes.windll.user32.BlockInput(True)
	time.sleep(Seconds)
	ctypes.windll.user32.BlockInput(False)