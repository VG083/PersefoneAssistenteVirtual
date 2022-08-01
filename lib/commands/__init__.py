import glob
import os

import pyautogui as ag
ag.PAUSE = 2
from time import sleep
import pyperclip as clip

import pywhatkit as wk

def filterSearchContent(command):
    '''
    """
    -> Essa função filtra as palavras chaves de um comando para melhorar sua execução
    :param command: Recebe o comando para ser filtrado
    '''
    classifierWords = ('abrir', 'iniciar'
                        'buscar', 'pesquisar', 'procurar',
                        'tocar', 'música')
    for word in range(0, len(classifierWords)):
        if classifierWords[word] in command:
            newCommand = command.replace(classifierWords[word], '')
            return newCommand
            

def openProgram(command):
    '''
    """
    -> Essa função abre programas
    :param command: Recebe o comando para ser executado
    '''
    if 'navegador' in command:
        return os.system('start Brave.exe')
    if 'editor' in command:
        return os.startfile(r'C:\Users\jnone\AppData\Local\Programs\Microsoft VS Code\Code.exe')
    if 'jogos' in command:
        return os.startfile(r'C:\Program Files (x86)\Steam\steam.exe')
    if 'notas' in command:
        ag.press('win')
        sleep(2)
        ag.write('notepads')
        ag.hotkey('enter')
        return 'bloco de notas aberto'
    else:
        ag.press('win')
        contentSearch = filterSearchContent(command)
        clip.copy(contentSearch)
        ag.hotkey("ctrl", "v")
        ag.hotkey('enter')
        return print('')
        

def openSearch(command):
    '''
    """
    -> Essa função faz pesquisas no google
    :param command: Recebe o comando para ser executado
    '''
    ag.hotkey('win')
    ag.write('Brave')
    #sleep(3)
    ag.hotkey('enter')
    ag.write('google.com')
    ag.hotkey('enter')
    contentSearch = filterSearchContent(command)
    clip.copy(contentSearch)
    ag.hotkey("ctrl", "v")
    ag.hotkey('enter')


def openSong(command):
    '''
    """
    -> Essa função abre músicas diretamente no youtube
    :param command: Recebe o comando para ser executado
    '''
    contentSearch = str(filterSearchContent(command))
    wk.playonyt(contentSearch)