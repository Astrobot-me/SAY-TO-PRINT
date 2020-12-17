import speech_recognition as sp
import time
# initialize the recognition
rec = sp.Recognizer()

# my device index 
my_micro = sp.Microphone(device_index=1)

with my_micro as source:
    print("Say something ...")
    audio = rec.listen(source) # get voice input from your micro
    
    
to_text = rec.recognize_google(audio) # convert audio to text

delay(10)
print(to_text) # print speech recorded from microphone


import pyttsx3
speaker = pyttsx3.init()
rate = speaker.getProperty('rate')   # getting details of current speaking rate
print (rate)                        #printing current voice rate
speaker.setProperty('rate', 170)     # setting up new voice rate


"""VOLUME
volume = speaker.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
print (volume)                          #printing current volume level
speaker.setProperty('volume',1.0)    # setting up volume level  between 0 and 1
"""
"""VOICE"""
voices = speaker.getProperty('voices')       #getting details of current voice
#speaker.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
speaker.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female
"""engine.say("Hello World!")
engine.say('My current speaking rate is ' + str(rate))
engine.runAndWait()
engine.stop()"""
#speaker.say('My current speaking rate is ' + str(rate))
#speaker.say('audiobook on pslv and invite or warning')
speaker.say(to_text)
#speaker.save_to_file(str(x),'ab2.mp3')
speaker.runAndWait()



