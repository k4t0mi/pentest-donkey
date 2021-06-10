# Import modules

import ctypes


# Open cdrom

def OpenCD():
	return ctypes.windll.WINMM.mciSendStringW(u'set cdaudio door open', None, 0, None)


# Close cdrom

def CloseCD():
	return ctypes.windll.WINMM.mciSendStringW(u'set cdaudio door closed', None, 0, None)