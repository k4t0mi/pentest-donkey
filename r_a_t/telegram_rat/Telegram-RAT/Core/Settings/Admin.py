# Import modules

import ctypes


# Is user administrator

def Admin():
	return ctypes.windll.shell32.IsUserAnAdmin() != 0