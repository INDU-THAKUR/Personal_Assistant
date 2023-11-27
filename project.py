
import pyttsx3 # text-to-speech conversion library in Python
import speech_recognition as sr
import datetime
import openai
#from playsound import playsound
import wikipedia
import webbrowser
import os
#import smtplib
import sys
import requests
from bs4 import BeautifulSoup
engine = pyttsx3.init('sapi5') #sapi5 is Microsoft developed speech API help to recognition of voice
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate',180)
def speak(audio):
    engine.say(audio)
    print(f":{audio}")
    print("")
    engine.runAndWait()
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Mam, how are you !")
    elif hour>=12 and hour<16:
        speak("Good Afternoon Mam!how are you")   
    else:
        speak("Good Evening  mam!How are you") 
    speak("I am jarvis. Please tell me how may I help you")   
def takeCommand():
    #It takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source,0,3) 
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        # print(e)    
        print("Please Say that again please...")  
        return "None"
    return query
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('indu.82.it@gmail.com', 'IThakur@88')
    server.sendmail('pritirajput560@gmail.com', to, content)
    server.close()
if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()
        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'hello jarvis' in query:
            speak('hii mam,how may i help you')
        elif 'how are you jarvis'in query:
            speak('I am good mam! what about you')
        elif 'open youtube' in query:
            webbrowser.open("www.youtube.com")
            cm = takeCommand().lower()
            webbrowser.open(f"{cm}")
        elif 'open google' in query:
            speak("Mam,what should i search on google")
            cm = takeCommand().lower()
            webbrowser.open(f"{cm}")
        elif 'open amazon' in query:
            webbrowser.open("www.amazon.com ")
        elif 'open myntra' in query:
            webbrowser.open("www.myntra.com")    
        elif 'open stackoverflow' in query:
            webbrowser.open("www.myntra.com")
        elif 'temperature' in query:
            search = ("temperature in solan")
            url = f"https://www.google.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text,"html.parser")
            temperature = data.find("div",class_= "BNeawe").text
            speak(f"Mam the temperatur outside is: {temperature}")
        elif 'play music' in query:
            music_dir ="C:\\Users\\indu\\Downloads\\Music"
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))
        elif ' the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Mam, the time is {strTime}")
        elif ' the date today' in query:
            strTime = datetime.datetime.now().strftime("%D:%m:%Y")
            speak(f"mam, the date is {strTime}")
        elif 'open python IDE' in query:
            codePath ="C:\\Users\\indu\\AppData\\Local\\Programs\\Python\\Python311\\python.exe"
            os.startfile(codePath)
        elif 'open ms word'in query:
            codePath ="C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\word"
            os.startfile(codePath)
        elif 'open PowerPoint'in query:
            codePath ="C:\\Users\\indu\\Desktop\\Introduction.ppt"
            os.startfile(codePath)
        elif 'open vs code' in query:
            codePath ="D:\\Software\\Microsoft VS Code\\Code.exe"
            #elif 'open vs code'in query:
            #speak("mam,what should i open on vs")
            #cm = takeCommand().lower()
            #os.startfile("D:\\project.py","{cm}")
        elif "close" in query:
            speak("thanks for using me mam,have a good day.")
            sys.exit()
        elif "shut down the system" in query:
            os.system("shutdown /s /t 5")
        elif "restart the system" in query:
            os.system("shutdown /r /t 5")    
        elif 'email to himanshi' in query:
            try:
                speak("What should i send ?")
                content = takeCommand()
                to = "pritirajput560@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend . I am not able to send this email")
                query = takeCommand().lower()
                speak("mam,do you have any other work")
            except Exception as e:
                print(e)
                speck("Sorry my friend . I am not able to send this email")
                query = takeCommand().lower()
                speak("mam do you have any other work")
            
            
