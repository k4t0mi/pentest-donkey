# Import modules

try:
	import wave
	import pyaudio
except ImportError:
	raise SystemExit('Please run › pip install pyaudio')


# Records audio from a microphone

def Microphone(File, Seconds):
	CHUNK = 1024
	FORMAT = pyaudio.paInt16
	CHANNELS = 2
	RATE = 44100
	RECORD_SECONDS = float(Seconds)
	WAVE_OUTPUT_FILENAME = File
	p = pyaudio.PyAudio()
	stream = p.open(format=FORMAT,
					channels=CHANNELS,
					rate=RATE,
					input=True,
					frames_per_buffer=CHUNK)
	frames = []
	for i in range(0, int(RATE/CHUNK * RECORD_SECONDS)):
		data = stream.read(CHUNK)
		frames.append(data)
	stream.stop_stream()
	stream.close()
	p.terminate()
	wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
	wf.setnchannels(CHANNELS)
	wf.setsampwidth(p.get_sample_size(FORMAT))
	wf.setframerate(RATE)
	wf.writeframes(b''.join(frames))
	wf.close()