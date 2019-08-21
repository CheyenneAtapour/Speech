# adapted from 
# https://github.com/Uberi/speech_recognition/blob/master/examples/microphone_recognition.py

import speech_recognition as sr
import win32com.client as wincl

# obtain audio from the microphone

speak = wincl.Dispatch("SAPI.SpVoice")

while True:

	r = sr.Recognizer()
	with sr.Microphone() as source:
		print("Hello World, I am Dr. Luke. What do you need?")
		speak.Speak("Hello World, I am Dr. Luke. What do you need?")
		audio = r.listen(source)

	s = ""

	try:
	    # for testing purposes, we're just using the default API key
	    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
	    # instead of `r.recognize_google(audio)`
	    s = r.recognize_google(audio)
	    print("I think you said " + s)
	    speak.Speak("I think you said " + s)

	    # Scenario 1
	    if s == "quiz me on acute pancreatitis":
	    	print("What are the common causes of pancreatitis?")
	    	speak.Speak("What are the common causes of pancreatitis?")
	    	with sr.Microphone() as source:
	    		audio = r.listen(source)
	    	s = r.recognize_google(audio)
	    	print("I think you said " + s)
	    	speak.Speak("I think you said " + s)
	    	if s == "gallstones alcohol and trauma":
	    		print("You are correct")
	    		speak.Speak("You are correct")
	    	else:
	    		print("You are incorrect. The most common causes of pancreatitis are gallstones, alcohol and trauma")
	    		speak.Speak("You are incorrect. The most common causes of pancreatitis are gallstones, alcohol and trauma")

	    # Scenario 2
	    elif s == "quiz me on post-op causes of fever":
	    	print("What is the most likely cause of fever 2 days after surgery?")
	    	speak.Speak("What is the most likely cause of fever 2 days after surgery?")
	    	with sr.Microphone() as source:
	    		audio = r.listen(source)
	    	s = r.recognize_google(audio)
	    	print("I think you said " + s)
	    	speak.Speak("I think you said " + s)
	    	if s == "atelectasis or pneumonia":
	    		print("You are correct")
	    		speak.Speak("You are correct")
	    	else:
	    		print("Incorrect, the most likely cause is Atelectasis or Pneumonia")
	    		speak.Speak("Incorrect, the most likely cause is Atelectasis or Pneumonia")
	    
	    # catch all
	    else:
	    	print("I have not learned how to respond to that yet")
	    	speak.Speak("I have not learned how to respond to that yet")

	except sr.UnknownValueError:
	    print("Google Speech Recognition could not understand audio")
	except sr.RequestError as e:
	    print("Could not request results from Google Speech Recognition service; {0}".format(e))

