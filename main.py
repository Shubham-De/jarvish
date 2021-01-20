import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import weather_forecast as wf #pip install weather_forecast 
import random

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am Jarvis. Sir, Please tell me how may I help")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

def joke():
    jokes = ["Can a kangaroo jump higher than a house? . Of course, a house doesn’t jump at all.", "Doctor: You're obese. Patient: For that I definitely want a second opinion. Doctor: You’re quite ugly, too."
    , "What did one traffic light say to the other?. Stop looking! I am changing!", "What do you call bears with no ears?, B."
    , "Why do French people eat snails? They don't like fast food!", "What's red and moves up and down? A tomato in an elevator!"
    , "I have many jokes about unemployed people, sadly none of them work.", "What do you call a singing laptop? A Dell!"
    , "Why was six afraid of seven? Because seven ate nine.", "Why are skeletons so calm? Because nothing gets under their skin."
    , "How do trees get online? They just log on!"]

    rand_jokes = random.choice(jokes)
    print(rand_jokes)
    speak(rand_jokes)

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

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   


        elif 'play music' in query:
            music_dir = 'path\\to\\the\\music\\you\\want\\to\\open\\'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open chrome' in query:
            codePath = "path\\to\\the\\app(Chrome)\\you\\want\\to\\open\\chrome.exe"
            os.startfile(codePath)

        elif 'email to harry' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "example@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry the email wasn't send")

        elif 'weather' in query:
            a = datetime.datetime.now().strftime("%H:%M:%S") 
            print(f"Current Time: {a}\n")

            b = wf.forecast(place = "Kathmandu" , time=a , date="2021-01-20" , forecast="daily")
            speak(f"Sir, the weather forcast of current time {b} is listed below")
            print(b)

        elif 'tell me a joke' in query:
            joke()
            
                
               
      
