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
        query=takeCommand() # running takeCommand function
        sites = [
            ["youtube", "https://youtube.com"],
            ["google", "https://google.com"],
            ["instagram", "https://instagram.com"],
            ["facebook", "https://facebook.com"],
            ["linkedin", "https://linkedin.com"],
            ["twitter", "https://twitter.com"],
            ["whatsapp", "https://web.whatsapp.com"],
            ["github", "https://github.com"],
            ["stackoverflow", "https://stackoverflow.com"],
            ["geeksforgeeks", "https://geeksforgeeks.com"],
            ["hackerrank", "https://hackerrank.com"],
            ["codechef", "https://codechef.com"],
            ["leetcode", "https://leetcode.com"],
            ["codeforces", "https://codeforces.com"],
            ["amazon", "https://amazon.com"],
            ["flipkart", "https://flipkart.com"],
            ["myntra", "https://myntra.com"],
            ["quora", "https://quora.com"],
            ["coursera", "https://coursera.com"],
            ["edx", "https://edx.com"],
            ["myntra", "https://myntra.com"],
            ["ebay", "https://ebay.com"],
            ["udemy", "https://udemy.com"]
        ]
        for site in sites:
            if f"{site[0]}".lower() in query.lower():
                say(f"Opening {site[0]} Sir")
                webbrowser.open(site[1])
        
        if "play playlist".lower() in query.lower():
            say("Opening Your Favourite Song Sir and playlist of Eminem for you on Youtube")
            webbrowser.open("https://www.youtube.com/watch?v=_WYO5EGTY-o&list=PL7E436F1EC114B001&index=11")

        if "play song" in query:
            musicpath="C:Users/ADITI-PC/Downloads/Without-Me---Eminem(musicdownload.cc).mp3"
            say("Starting Song Sir")
            os.startfile(musicpath)
                


        say(query)

        
      
       
