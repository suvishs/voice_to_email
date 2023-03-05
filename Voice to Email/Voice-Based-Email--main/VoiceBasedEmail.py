import speech_recognition as sr
import easyimap as e
import pyttsx3
import smtplib
import pyaudio
from email.message import EmailMessage
import ssl

unm = "protechcodelife3@gmail.com"
pwd = "cftpnpvmwhcieaxn"

r = sr.Recognizer()

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice' ,voices[1].id)
engine.setProperty('rate', 150)

def speak(str):
    print(str)
    engine.say(str)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        str = 'Speak Now:'
        speak(str)
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            return text
        except:
            str = "Sorry could not recognize what you said"
            speak(str)


def sendemail():
    rec = {
        'ramanan' : 'suvishsnair@gmail.com',
        'Ramanan' : 'suvishsnair@gmail.com',
        'Ramanand' : 'suvishsnair@gmail.com',
        'first' : 'protechcodelife@gmail.com',
        'second' : 'protechcodelife@gmail.com',
        'third' : 'suvishs967@gmail.com',
    }
    str = 'Please say the recipient name'
    speak(str)

    while True:
        name = listen()

        if name in rec:
            recname = rec[name]
            break
        else:
            str = "This name is not in our list. Please say the recipient name again"
            speak(str)

    str = 'Say your subject of the email'
    speak(str)
    subject = listen()

    str = 'Say your body of the email'
    speak(str)
    body = listen()

    em = EmailMessage()
    em['From'] = unm
    em['To'] = recname
    em['subject'] = subject
    em.set_content(body)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(unm,pwd)
        smtp.sendmail(unm, recname, em.as_string())
    
    str = "Your Mail has been sent"
    speak(str)


def readmail():
    try:
        server = e.connect("imap.gmail.com",unm,pwd)
        server.listids()

        str = "Please say the serial number of the email you wanna read starting from latest"
        speak(str)
        a = listen()

        if(a == "first"):
            a = "1"

        elif(a == "second"):
            a = "2"

        elif(a == "third"):
            a = "3"

        elif(a == "fourth"):
            a = "4"

        elif(a == "fifth"):
            a = "5"

        else:
            str = "You say a invalid command"

        b = int(a)

    except:
        str = "You say a invalid command"
        return

    try:
        email = server.mail(server.listids()[b])

    except:
        str = "Sorry didn't find the corresponding mail"
        return

    str = "The mail is from: "
    speak(str)
    speak(email.from_addr)
    str = "The object of the email is"
    speak(str)
    speak(email.title)
    str = "The body of email is: "
    speak(str)
    speak(email.body)


# str = "Welcome to voice controlled email service"
# speak(str)
keyword1 = "start"

str = 'Waiting for the key word START to on the system'
speak(str)

def listenkeyword():
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        
        str = 'Speak Now:'
        speak(str)
        audio = r.listen(source)
        try:
            global textkey
            textkey = r.recognize_google(audio)
            
            while True:
                if textkey == keyword1:
                    str = "Welcome to voice controlled email service"
                    speak(str)

                    while(1):
                        # str = "What do you want to do?"
                        # speak(str)

                        str = "Speak SEND to send email Speak READ to Read Inbox Speak EXIT to exit"
                        speak(str)

                        ch = listen()

                        if(ch == 'send'):
                            str = "You have choosen to send an email"
                            speak(str)
                            sendemail()

                        elif(ch=='read'):
                            str = "You have choosen to read email"
                            readmail()

                        elif(ch == 'exit'):
                            str = "You have choosen to exit, bye bye"
                            speak(str)
                            listenkeyword()
                        
                        else:
                            str = "Invalid choice, You said:"
                            speak(str)
                            speak(ch)
                else:
                    listenkeyword()
        except:
            listenkeyword()
            print("Sorry could not recognize what you said")
            # str = "Sorry could not recognize what you said"
            # speak(str)
listenkeyword()