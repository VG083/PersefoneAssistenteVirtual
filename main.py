import speech_recognition as sr
import os
from time import sleep
from lib.interface import *
from lib.commands import *

listener = sr.Recognizer()

while True:
    os.system('cls')
    cabecalho()
    
    try:
        with sr.Microphone() as source:
            listener.adjust_for_ambient_noise(source)
            voice = listener.listen(source, phrase_time_limit=10)
            command = listener.recognize_google(voice, language='pt-BR')
            command = command.lower()
            falaUsuario(command)

            # Assistant Commands
            if 'fechar' in command:
                break
            if 'fecha' in command:
                break
            if 'desligar' in command:
                break
            if 'desliga' in command:
                break
            
            # Classificadores de Comandos
            openingPrograms = ('abrir', 'iniciar')
            openingSearches = ('buscar', 'pesquisar', 'procurar')
            openingSongs = ('tocar', 'música')
            
            # Comandos para abrir programas
            for palavra in range(0, len(openingPrograms)):
                if openingPrograms[palavra] in command:
                    openProgram(command)
            # Comandos para pesquisar no google
            for word in range(0, len(openingSearches)):
                if openingSearches[word] in command:
                    openSearch(command)
            # Comandos para ouvir música no youtube
            for word in range(0, len(openingSongs)):
                if openingSongs[word] in command:
                    openSong(command)
            sleep(5)
            
    except:
        falaPersefone('Desculpe, não entendi')
        sleep(2)

falaPersefone('Fechando')
