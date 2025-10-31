from gtts import gTTS
import os
import platform

texto = "Este é um programa que gera som através de um texto"
lingua = "pt-br"
objetogtts = gTTS(text=texto, lang=lingua,slow=False)
arquivo_audio='saidagtts.wav'
objetogtts.save(arquivo_audio)

sistemaoperacional = platform.system()

if sistemaoperacional == "Darwin":
    os.system(f"afplay {arquivo_audio}")
elif sistemaoperacional == "Windows":
    os.system(f"start {arquivo_audio}")
elif sistemaoperacional == "Linux":
    os.system(f"aplay {arquivo_audio}")
else:
    print(f"Sistema operacional {sistemaoperacional} não suportado para reprodução automática")