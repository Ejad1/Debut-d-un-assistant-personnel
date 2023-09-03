import speech_recognition as sr
import pyttsx3 as ttx
import pywhatkit
import datetime

listener = sr.Recognizer()
engine = ttx.init()
voice = engine.getProperty("voices")
engine.setProperty("voice", "french")


# Fonction charger d’écouter le micro lorsqu’on parle ce qu'on dit
def speak(text):
    engine.say(text)
    engine.runAndWait()


# Fonction
def ecoute():
    try:
        with sr.Microphone() as source:
            print("Veuillez parler au micro")
            voix = listener.listen(source)
            command = listener.recognize_google(voix, language="fr-FR")

    except:
        pass

    return command


def assistant():
    message = ecoute()
    print(message)
    if 'bonjour' in message:
        speak('Bonjour. Comment allez-vous ?')
    elif 'mettez la chanson de ' in message:
        chanteur = message.replace('mettez la chanson de', '')
        print(chanteur)
        pywhatkit.playonyt(chanteur)
    elif 'heure' in message:
        heure = datetime.datetime.now().strftime("%H:%M")
        speak(f"Il est {heure}")


# Démarrage de l’assistant
while True:
    assistant()
