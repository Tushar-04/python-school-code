# Python program to translate 
# speech to text and text to speech 


import speech_recognition as sr 
r = sr.Recognizer() 

try: 
		
	# use the microphone as source for input. 
	with sr.Microphone() as source2:
                
		# wait for a second to let the recognizer 
		# adjust the energy threshold based on 
		# the surrounding noise level
		print("Say something:")
		r.adjust_for_ambient_noise(source2, duration=0.2) 
		audio2 = r.listen(source2) 
		
		# Using ggogle to recognize audio 
		MyText = r.recognize_google(audio2) 
		MyText = MyText.lower() 
		print("Did you say "+MyText) 
			
except sr.RequestError as e: 
		print("Could not request results; {0}".format(e))
except sr.UnknownValueError: 
		print("unknown error occured") 
