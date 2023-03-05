# Voice-Based-Email-
In this project you can send email messages to your contact list with your Voice. 

# def sendemail():
#     rec = "protechcodelife@gmail.com"
#     str = "Please speak the body of your email"
#     speak(str)
#     msg = listen()

#     str = "You have spoken the message"
#     speak(str)
#     speak(msg)

#     server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
#     server.login(unm,pwd)
#     server.sendmail(unm,rec,msg)
#     server.quit()

#     str = "The mail has been sent"
#     speak(str)

# def sendemail():
#     rec = {
#         'ramanan' : 'suvishsnair@gmail.com',
#         'two' : 'protechcodelife@gmail.com',
#         'three' : 'protechcodelife@gmail.com',
#         'four' : 'suvishs967@gmail.com',
#     }
#     str = 'Pleace say a mail receiver name'
#     speak(str)
#     name = listen()

#     for i in rec:
#         if i == name:
#             recname = rec[i]
#             break
#         else:
#             str = "This name is not in our list"
#             speak(str)
#             sendemail()
            
    
#     str = 'Say your subject of the email'
#     speak(str)
#     subject = listen()

#     str = 'Say your body of the email'
#     speak(str)
#     body = listen()

#     em = EmailMessage()
#     em['From'] = unm
#     em['To'] = recname
#     em['subject'] = subject
#     em.set_content(body)

#     context = ssl.create_default_context()

#     with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
#         smtp.login(unm,pwd)
#         smtp.sendmail(unm, recname, em.as_string())





# import smtplib
# import speech_recognition as sr
# import pyttsx3
# from email.message import EmailMessage

# listener = sr.Recognizer()
# engine = pyttsx3.init()


# def talk(text):
#     engine.say(text)
#     engine.runAndWait()


# def get_info():
#     try:
#         with sr.Microphone() as source:
#             print('listening...')
#             voice = listener.listen(source)
#             info = listener.recognize_google(voice)
#             print(info)
#             return info.lower()
#     except:
#         pass


# def send_email(receiver, subject, message):
#     server = smtplib.SMTP('smtp.gmail.com', 587)
#     server.starttls()

#     server.login('protechcodelife@gmail.com', '@Suvish9061171046')
#     email = EmailMessage()
#     email['From'] = 'Sender_Email'
#     email['To'] = receiver
#     email['Subject'] = subject
#     email.set_content(message)
#     server.send_message(email)


# email_list = {
#     'suvish': 'protechcodelife3@gmail.com',
#     'suvi': 'protechcodelife2@gmail.com',

# }


# def get_email_info():
#     talk('Hi Sir I am your assistant for today, To Whom you want to send email')
#     name = get_info()
#     receiver = email_list[name]
#     print(receiver)
#     talk('What is the subject of your email?')
#     subject = get_info()
#     talk('Tell me the text in your email')
#     message = get_info()
#     send_email(receiver, subject, message)
#     talk('Thankyou sir for using me. Your email has been send')
#     talk('Do you want to send more email?')
#     send_more = get_info()
#     if 'yes' in send_more:
#         get_email_info()


# get_email_info()