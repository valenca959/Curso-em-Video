import pygame
print('Prazer em te conhecer')
print('Ouça com atenção')
pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('mp3.mp3')
pygame.mixer.music.play(loops=0, start=0.0)
pygame.event.wait()
