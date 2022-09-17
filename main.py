import speech_recognition as sp_rec
import pyttsx3
import datetime
import pywhatkit
import wikipedia
import pyjokes
from datetime import date

listener = sp_rec.Recognizer()

alexa = pyttsx3.init()

voices=alexa.getProperty('voices')
alexa.setProperty('voice',voices[1].id)

def talk(text):
    alexa.say(text)
    alexa.runAndWait()

def take_command():
    try:
        with sp_rec.Microphone() as mic:
            print('Listening...')
            voice=listener.listen(mic, None, 10)
            command=listener.recognize_google(voice)
            command=command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
    except:
        pass
    return command


def alexa_reply():
    command = take_command()

    if 'time' in command:
        time=datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current time is ' + time)
    elif 'date' in command:
        d = date.today()
        print(d)
        talk(d)

    elif 'play' in command:
        song = command.replace('play', '')

        talk('playing' + song)
        pywhatkit.playonyt(song)

    elif 'tell me about' in command:
        result = command.replace('tell me about','')
        information = wikipedia.summary(result,2)
        print(information)
        talk(information)


    elif 'tell me a joke' in command:
        print(pyjokes.get_jokes())
        talk(pyjokes.get_jokes())


    elif 'search for' in command:
        result= command.replace("search for",'')
        pywhatkit.search(result)
        talk('OK, I am searching' )


    elif 'did you have done your lunch' in command:
        talk("Yes, i have done")
        print("Yes, i have done")
    elif 'how are you' in command:
        talk("I am fine")
        print("I am fine")
    elif 'have a nice day' in command:
        talk('Thank you, same to you')
        print("Thank you, same to you")
    elif 'i love you' in command:
        talk('I Love You too')
        print("I Love You too!")
    elif 'are you boy or girl' in command:
        talk('I am a girl')
        print('I am a girl')

    else:
        talk("I didn't understand! Maybe you are searching for this?")
        pywhatkit.search(command)


alexa_reply()