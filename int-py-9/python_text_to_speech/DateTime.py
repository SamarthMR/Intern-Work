# Import the required module for text
# to speech conversion
import pyttsx3
import datetime
# init function to get an engine instance for the speech synthesis
engine = pyttsx3.init('sapi5')

hour = int(datetime.datetime.now().hour)
if hour >= 0 and hour < 12:
    engine.say("Good Morning")

elif hour >= 12 and hour < 18:
    engine.say("Good Afternoon")

else:
    engine.say("Good Evening")

engine.say("I am AI 2.0, Please tell me how may I help you")

# run and wait method, it processes the voice commands.
engine.runAndWait()