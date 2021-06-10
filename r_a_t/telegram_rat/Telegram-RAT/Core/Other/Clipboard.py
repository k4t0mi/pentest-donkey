# Import modules

try:
	from pyperclip import copy, paste
except ImportError:
	raise SystemExit('Please run › pip install pyperclip')


# Sets text to clipboard

def SetClipboard(Text):
	copy(Text)


# Get text from clipboard

def GetClipboard():
	return paste()