import pyttsx3 #pip install pyttsx3(if not installed)
import datetime
import speech_recognition as sr #pip install SpeechRecognition
import wikipedia #pip install wikipedia
import smtplib #build in function of python
import webbrowser as wb
import os
import pyautogui #pip install pyautogui
import psutil #pip install psutil
import pyjokes #pip install pyjokes


#--Text To Speech--
engine=pyttsx3.init()
#engine.say("This is JARVIS")
#engine.runAndWait() 


#--Speak Function--
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
#speak("This is Jarvis AI Assistant")


#--Time Function--
    #import pyttsx3
    #import datetime
def time():
    Time=datetime.datetime.now().strftime("%I:%M:%S")
    speak("The current time is")
    speak(Time)
#time()


#--Date Function--
def date():
    year=int(datetime.datetime.now().year)
    month=int(datetime.datetime.now().month)
    date=int(datetime.datetime.now().day)
    speak("the current date is")
    speak(date)
    speak(month)
    speak(year)
#date()


#--Greeting function--
def wishme():
    speak("Welcome Back sir!")
    #speak("The current time is")
    #time()
    #speak("the current date is")
    #date()
    hour=datetime.datetime.now().hour
    if hour>=6 and hour<12:
        speak("Good morning sir!")
    elif hour>=12 and hour<18:
        speak("Good afternoon sir")
    elif hour>=18 and hour<24:
        speak("Good evening sir")
    else:
        speak("Good night")
    speak("Jarvis at your service. Please tell me how can i help you?")    
#wishme()


#--take command--
    #import speech_recognition
def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio=r.listen(source)
        
    try:
        print("Recognizing...")
        query=r.recognize_google(audio, language='en-in')
        print(query)
    except Exception as e:
        print(e)
        speak("Say that again please...")
        return "None"
    return query
#takeCommand()


#--to Send Email--
def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('your_email_id@gmail.com','password')
    server.sendmail('your_email_id@gmail.com', to, content) #to=Receiver_email_id
    server.close()

    
#--this took Screenshot--
def screenshot():
    img=pyautogui.screenshot()
    #Provide address of an folder where you want to save Screenshot.
    img.save("C:\\Users\\Provide_Address_of_folder")
    
    
#--this tell about cpu usage and battery--    
def cpu():
    usage=str(psutil.cpu_percent())
    speak('CPU is at'+usage)
    battery=psutil.sensors_battery()
    speak("Battery is at")
    speak(battery.percent)
    
    
#--this function tell us jokes from internet--    
def jokes():
    speak(pyjokes.get_joke())
    
    
#--Its a main code from where code will start executing--
if __name__=="__main__":
    wishme()
    while True:
        query=takeCommand().lower()
        
        if 'time' in query:
            time()    
            
        elif 'date' in query:
            date()
        
        #--Search on wikipedia--
        elif 'wikipedia' in query:
            speak("Searching...")
            query=query.replace("wikipedia","")
            result=wikipedia.summary(query, sentences=2)
            print(result)
            speak(result)
            
        #--Send email--    
        elif 'send email' in query:
            try:
                speak("What should i say?")
                content=takeCommand()
                to= 'receiver_email_id@gmail.com'
                #sendEmail(to,content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Unable to send the email")
        
        #--Search on chrome--
        elif 'search in chrome' in query:
                speak("What should i search?")
                chromepath='C:/program Files (x86)/Google/Chrome/Application/chrome.exe %s'
                #if this path does not work in your system change it accordingly
                search=takeCommand().lower()
                wb.get(chromepath).open_new_tab(search+'.com')

            
        #This section is commented out to avoid potential risks associated with executing system commands such as shutdown, restart, or logout.
        # Uncommenting and using these commands might result in unintended consequences, such as shutting down the system.
        # It's recommended to be cautious and ensure proper handling and permissions before enabling such functionalities.
        '''elif 'logout' in query:
            os.system("shutdown -1")
        elif 'shutdown' in query:
            os.system("shutdown /s /t 1")
        elif 'restart' in query:
            os.system("shutdown /r /t 1")
        '''
                
        #--this will play songs from your system--
        elif 'play songs' in query:
            songs_dir='D:\\Music'
            songs=os.listdir(songs_dir)
            os.startfile(os.path.join(songs_dir, songs[0]))
        
        #This section handles remembering information provided by the user.
        #To implement this functionality, ensure you have an empty file named "data.txt" created beforehand.
        elif 'remember that' in query:
            speak("What should i remember?")
            data=takeCommand()
            speak("you said to remeber that "+data)
            remember=open('data.txt','w')
            remember.write(data)
            remember.close()
        elif 'do you know anything' in query:
            remember=open('data.txt','r')
            speak("you said me to remeber that "+remember.read())
         
        elif 'screenshot' in query:
            screenshot()
            speak("Done!")
        
        elif 'cpu' in query:
            cpu()
        
        elif 'joke' in query:
            jokes()
        
        #--Jarvis quit--
        elif 'offline' in query:
            speak("Going offline. Goodbye!")
            break  # Break out of the loop when 'offline' is detected