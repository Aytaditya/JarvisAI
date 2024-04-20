import pyttsx3
import speech_recognition as sr
import os
import webbrowser

def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


# sometimes it is not able to understand the command given by user and hence throw a error so we need to handle it by wrapping it try and catch 

#take command from user using micrphone
def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold=1
        audio=r.listen(source)  #listening to microphone
        try:
            query=r.recognize_google(audio,language='en-in')
            print(f"User said: {query}")
            return(query)
        except Exception as e:
            print("I beg your pardon Sir...")
            return "I beg your pardon Sir..."

if __name__ == "__main__":
    print("Hello, I am Jarvis. How can I help you today?")
    say("Hello Sir, I am Jarvis. How can I help you today?")
    while True:
        print("Listening Sir...")
        query=takeCommand() #ruuning takeCommand function
        if "Open Youtube".lower() in query.lower():
            say("Opening youtube Sir")
            webbrowser.open("https://www.youtube.com/")
            
        say(query)
