# Import modules

import win32api
import win32con


# Audio volume control

def VolumeControl(Level):
	for i in range(int(Level)):
		win32api.keybd_event(win32con.VK_VOLUME_UP, 0)