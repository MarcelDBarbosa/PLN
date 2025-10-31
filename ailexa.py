import speech_recognition as sr
from gtts import gTTS
import os
import webbrowser
import wikipedia
import subprocess

file = "voice.mp3"

def del_file(arq):
    try:
        os.remove(arq)
    except OSError:
        pass

def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        #r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
        said = ""
        try:
            said = r.recognize_google(audio, language="pt-BR")
            print(said)
        except Exception as e:
            said = ""
    return said

def speak(text):
    tts = gTTS(text=text, lang= 'pt-br')
    del_file(file)
    tts.save(file)
    os.system(f"afplay {file}")

def tarefas():
    condicao = True
    while condicao:
        print("\nEstou ouvindo...")
        speak("Como posso ajudar?")
        text = get_audio().lower()
        if 'youtube' in text:
            speak("Abrindo o site Youtube")
            url = f"https://www.youtube.com"
            webbrowser.get().open(url)
        elif 'wikipédia' in text:
            speak("Procurando Wikipedia")
            query=""
            if "procure" in text:
                query = text.replace("procure", "")
            if query != "":
                query = query.replace("na wikipédia", "")
            else:
                query = text.replace("na wikipédia", "")
            print(query)
            wikipedia.set_lang('pt')
            if query != "":
                result = wikipedia.summary(query, sentences=3)
                speak("De acordo com a wikipedia")
                print(result)
                speak(result)
            else: 
                speak("Pergunte novamente, por favor!")
        elif 'uol' in text:
            speak("Abrindo o site do uol")
            url = f"https://www.uol.com.br"
            webbrowser.get().open(url)
        elif 'música' in text:
            speak("Abrindo o VLC")
            caminho = "/Users/SEUUSUARIO/Music"
            subprocess.run(["open", "-a", "VLC", caminho])
        elif ('dormir' in text or 'aguardar' in text):
            speak("ok")
            condicao = False
        else:
            speak("Desculpe me, não entendi")

while True:
    print("\nAguardando...")
    text = get_audio().lower()
    if ('lexa' in text) or ('aste' in text):
        tarefas()
    elif 'sair' in text:
        speak("Até a próxima")
        del_file(file)
        exit()