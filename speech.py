import speech_recognition as sr

r = sr.Recognizer()
mic = sr.Microphone()

def record_and_recognize():
	try:
		with mic as source:
			r.adjust_for_ambient_noise(source)
			audio = r.listen(source)
		return r.recognize_google(audio)
	except:
		return ""
