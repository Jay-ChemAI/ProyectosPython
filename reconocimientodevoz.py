import speech_recognition as sr
import os
import webbrowser

# Crear un objeto reconocedor de voz
r = sr.Recognizer()

# Iniciar la grabación de audio
with sr.Microphone() as source:
    print("¿En qué puedo ayudarte?")
    audio = r.listen(source)

# Utilizar el reconocedor de voz de Google para transcribir el audio
try:
    comando = r.recognize_google(audio, language="es-ES")
    print("Comando: " + comando)
    
    if comando == "abrir navegador":
        webbrowser.open("https://www.google.com")
    elif comando == "abrir explorador":
        os.system("explorer")
    elif comando == "cerrar explorador":
        os.system("taskkill /f /im explorer.exe")
    elif comando == "apagar PC":
        os.system("shutdown /s /t 1")
    else:
        print("Comando no reconocido")
    
except sr.UnknownValueError:
    print("No se pudo entender lo que dijiste.")
except sr.RequestError as e:
    print("No se pudo obtener la transcripción de Google Speech Recognition; {0}".format(e))


