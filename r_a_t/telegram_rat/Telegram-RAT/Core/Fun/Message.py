# Import modules

import ctypes


# Displays a message on the screen

def SendMessageBox(Message):
	ctypes.windll.user32.MessageBoxW(0, Message, u'', 0x40)