# Import modules

try:
	from keyboard import write
except ImportError:
	raise SystemExit('Please run › pip install keyboard')


# Prints the specified text

def SendKeyPress(Text):
	write(Text, delay=0.1)