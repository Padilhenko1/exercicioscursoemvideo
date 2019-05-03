#um programa de python que abra e reproduza um audio de arquivo mp3
#import pygame

#pygame.init() #iniciando o pygame
#pygame.mixer.music.load('ex21.mp3')
#pygame.mixer.music.play()
#pygame.event.wait()

from pygame import mixer
mixer.init()
mixer.music.load('ex21.mp3')
mixer.music.play()
input('Agora você escuta')

"Por incompatibilidade usar apenas o import mixer do pygame"