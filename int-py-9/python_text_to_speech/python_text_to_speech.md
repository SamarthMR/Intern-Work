# python_text_to_speech

## What is pyttsx3 ?
- A python library that will help us to convert text to speech. In short, it is a text-to-speech library.
- It works offline, and it is compatible with Python 2 as well as Python 3.
- An application invokes the pyttsx3.init() factory function to get a reference to a pyttsx3.

Installation:

    pip install pyttsx3

In case you receive such errors: 
- No module named win32com.client
- No module named win32
- No module named win32api

Then, install pypiwin32 by typing the below command in the terminal :

    pip install pypiwin32

After successfully installing pyttsx3, import this module into your program.

Usage:

    import pyttsx3
    engine = pyttsx3.init('sapi5')

## Why use python text to speech and difference with others
- Text-to-speech(TTS) technology reads aloud digital text. It can take words on computers, smartphones, tablets and convert them into audio.
- All kinds of text files can be read aloud, including Word, pages document, online web pages can be read aloud.

## Why pyttsx?
It works offline, unlike other text-to-speech libraries. Rather than saving the text as audio file, pyttsx actually speaks it there. This makes it more reliable to use for voice-based projects. 
### What is sapi5?
- Microsoft developed speech API.
- Helps in synthesis and recognition of voice.
- The pyttsx3 module supports two voices first is female and the second is male which is provided by “sapi5” for windows.
    It supports three TTS engines :

    > sapi5 – SAPI5 on Windows

    > nsss – NSSpeechSynthesizer on Mac OS X

    > espeak – eSpeak on every other platform
   
- Function in pyttsx3

    > This function keeps track when the engine starts converting text to speech and waits for that much time, and do not allow the engine to close.

    > If we don't write this code, it may happen that the engine might not work properly as the processes will not be synchronized.

Let's take an example

    # Import the required module for text to speech conversion
    import pyttsx3

    # init function to get an engine instance for the speech synthesis
    engine = pyttsx3.init('sapi5')

    # say method on the engine that passing input text to be spoken
    engine.say('Hello sir, how may I help you, sir.')

    # run and wait method, it processes the voice commands.
    engine.runAndWait()

Another Example

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