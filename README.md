# Personal_Assistant
# Author Indu Thakur

     import pyttsx3
   
  pyttsx3 is a text-to-speech conversion library in Python.
• It works offline and is compatible with both Python 2 and 3.

• The pyttsx3 module supports two voices first is female and the second is male 
which is provided by “sapi5” for windows.

• It supports three TTS engines:

  Sapi5 – sapi5 on Windows 

     import speech_recognition as sr
  
• Speech recognition is a machine's ability to listen to spoken words and identify them.

• Speech recognition in Python to convert the spoken words into text, make a query or give a 
reply.

• You can do speech recognition in python with the help of computer programs that take in 
input from the microphone, process it, and convert it into a suitable form.

        import datetime
        
• The module named datetime can be imported to work with the date as well as time.

• Python Datetime module comes built into Python, so there is no need to install it 
externally.

• Python Datetime module supplies classes to work with date and time. These classes 
provide a number of functions to deal with dates, times and time intervals.
  
    import wikipedia

• Wikipedia module in python is used to retrieve data from wikipedia pages.

• for this you should install wikipedia module.


    pip install wikipedia
    
    import webbrowse

  • webbrowser module is a convenient web browser controller. It provides a high-level 
interface that allows displaying Web-based documents to users.

• We can call the open () function from the webbrowser module to perform the right thing.

import os
    
• The OS module in Python provides functions for interacting with the operating system.

• OS comes under Python’s standard utility modules. This module provides a portable way 
of using operating system-dependent functionality.

• The *os* and *os.path* modules include many functions to interact with the file system.

• To work with the OS module, we need to import the OS module.

    import os
 
    import smtplib
    
• Simple Mail Transfer Protocol (SMTP) is a communication protocol for electronic mail 
transmission.

• The smtplib is a Python library for sending emails using the Simple Mail Transfer Protocol 
(SMTP).

    import sys
    
• The sys module is a built-in module in python.

• It provides several functions and variables to manipulate the python runtime environment.

• To use its functions, we have to import it.

• The commonly used functions and variables of sys module are as follows:

i. exit (): This function is used to terminate a program when needed.
ii. platform: This variable is used to identify the host operating system which we are 
using.
iii. executable: This specifies the path of python executable file.


ef sendEmail(to, content):
server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
10
server.starttls()
server.login('youremail@gmail.com', 'your-password')
server.sendmail('youremail@gmail.com', to, content) server.close()
• The smtplib is a built-in module; we do not need to install it. It abstracts away all the 
complexities of SMTP.
  import pyttsx3
  engine = pyttsx3.init('sapi5')
  voices= engine.getProperty('voices')
  engine.setProperty('voice', voice[0].id)

### What is sapi5?

• Microsoft developed speech API.
• Helps in synthesis and recognition of voice.

### What is VoiceId?
• Voice id helps us to select different voices.

• Voice [0].id = Male voice

• Voice [1].id = Female voice

    def speak(audio):
    
    engine.say(audio)
    
    engine.runAndWait()

  Speak () Function?
   
• We made a function called speak () at the starting of this program. It is used to convert our 
text to speech.

• Without this command, speech will not be audible to us.

   
  engine.runAndWait()
• This function keeps track when the engine starts converting text to speech and waits for that 
much time, and does not allow the engine to close.
   
    def wishme():
    hour = int(datetime.datetime.now().hour):

• Now, let's start defining the wishme () function

• Here, we have stored the current hour or time integer value into a variable named hour. 
Now, we will use this hour value inside an if-else loop.

     def takeCommand()
  
     r = sr.Recognizer()
  
     with sr.Microphone() as source: 
  
     print("Listening...")
  
     r.pause_threshold = 1
  
     audio = r.listen(source)
  
  Let's start the takeCommand () function

• It takes microphone input from the user and returns string output
  try:
  
    print("Recognizing...")
  
    query = r.recognize_google(audio, language='en-in')
  
    print(f"User said: {query}\n")
  
    except Exception as e:
  
    print(e)
  
    print("Say that again please")
  
    return "None"
  
    return query
 
