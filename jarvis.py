
import pyttsx3
import speech_recognition as sr
import os
import webbrowser
import datetime
from openai import OpenAI
from config import apikey
import random

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


def get_current_time():
    return datetime.datetime.now().strftime("%H:%M:%S")


def check_time():
    current_time = datetime.datetime.now().time()
    return current_time >= datetime.time(0, 0) and current_time <= datetime.time(5, 59)

def tell_joke():
    jokes = [
        "Why don't scientists trust atoms?..... Because they make up everything!",
        "What do you get when you cross a snowman and a vampire?...... Frostbite!",
        "Why did the scarecrow win an award?..... Because he was outstanding in his field!",
        "What did one plate say to the other plate?..... Dinner is on me!",
        "Why did the math book look sad?..... Because it had too many problems!",
        "What do you call cheese that isn't yours?..... Nacho cheese!",
        "Why couldn't the bicycle stand up by itself?..... It was two tired!",
        "What did one wall say to the other wall?..... I'll meet you at the corner!",
        "What did the grape do when he got stepped on?..... He let out a little wine!",
        "To the guy who invented zero: Thanks for nothing!",
        "Why is it always hot in the corner of a room?...... Because a corner is 90 degrees."
        
    ]
    random_joke = random.choice(jokes)
    return random_joke

def open_calculator():
    os.system("start calc")

#writing in output.txt
def write_text(text):
    file_path = "output.txt"  # Define the file path where you want to write the text
    with open(file_path, "a") as file:  # Open the file in append mode
        file.write(text + "\n")  # Write the text to the file

#reading output.txt
def read_text(file_path):
    try:
        with open(file_path, "r") as file:
            text = file.read()
        return text
    except FileNotFoundError:
        return "The file does not exist."
    except Exception as e:
        return f"An error occurred: {str(e)}"

def ai(prompt):
    client = OpenAI(api_key=apikey)
    text=f"OpenAi response for Prompt: {prompt}"

    response = client.completions.create(
    model="gpt-3.5-turbo-instruct",
    prompt="write a mail to my boss for resigning",
    temperature=1,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
)
    print(response["choices"][0]["text"])
    text+=response["choices"][0]["text"]
    if not os.path.exists("openai"):
        os.mkdir("openai")
    
    with open(f"prompt{prompt[0:30]}", "w") as f:
        f.write("text")
    



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
        
        if "open playlist".lower() in query.lower():
            say("Opening Your Favourite Song Sir and playlist of Eminem for you on Youtube")
            webbrowser.open("https://www.youtube.com/watch?v=_WYO5EGTY-o&list=PL7E436F1EC114B001&index=11")

        if "play song" in query:
            musicpath="C:Users/ADITI-PC/Downloads/Without-Me---Eminem(musicdownload.cc).mp3"
            say("Starting Song Sir")
            os.startfile(musicpath)
        
        if "the time" in query:
            if check_time():
                say("Sir, it's late. You should not be awake at this time.")
                current_time = get_current_time()
                say(f"Sir, the time is {current_time}")

            else:
                current_time = get_current_time()
                say(f"Sir, the time is {current_time}")

        if "open VS code".lower() in query.lower():
            say("Opening Visual Studio Code Sir")
            codepath="C:\\Users\\ADITI-PC\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)

        if "Using artifical intelligence".lower() in query.lower():
            say("Using OpenAI Sir")
            ai(prompt=query)

        if "Jarvis How are you".lower() in query.lower():
            say("I am fine Sir, How can I help you today?")

        if "What is your name".lower() in query.lower():
            say("I am Jarvis Sir,your virtual assistant designed by you. How can I help you today?")

        if "jarvis i am stressed".lower() in query.lower():
            say("I am here for you Sir, I can play your favourite song or open a playlist for you on youtube")

        if "Tell me a joke".lower() in query.lower():
             joke = tell_joke()
             say(f"Here is a joke sir, {joke}")

        if "open calculator".lower() in query.lower():
            say("Opening Calculator Sir")
            open_calculator()

        if "text for me".lower() in query.lower():
            say("What should I write Sir?")
            text = takeCommand()
            say("Writing in output.txt")
            write_text(text)
            say("I have written the text Sir")
        
        if "read output file".lower() in query.lower():
            say("Reading the content from output.txt Sir")
            text = read_text("output.txt")
            say(text)

        
        
        if "Shutdown".lower() in query.lower():
            say("Thank you Sir, Have a nice day")
            break

        

        

        
      
       
