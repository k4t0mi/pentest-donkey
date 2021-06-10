# Import modules

try:
	import mss
except ImportError:
	raise SystemExit('Please run › pip install mss')


# Takes a screenshot

def Screenshot(File):
	with mss.mss() as sct:
		sct.shot(output=File)