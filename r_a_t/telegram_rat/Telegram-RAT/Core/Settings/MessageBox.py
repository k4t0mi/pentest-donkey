# Import modules

import ctypes


# MessageBox Output

def MessageBox(Message):
	ctypes.windll.user32.MessageBoxW(0, Message, u'', 0x10)