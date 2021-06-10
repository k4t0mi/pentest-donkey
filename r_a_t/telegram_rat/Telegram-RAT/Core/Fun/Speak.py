# Import modules

try:
	import pyttsx3
except ImportError:
	raise SystemExit('Please run › pip install pyttsx3')

# Speaks text.

def SpeakText(Text):
	engine = pyttsx3.init()
	engine.setProperty('rate', 120) 
	engine.say(Text)
	engine.runAndWait()
