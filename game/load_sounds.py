import sys
sys.path.append('.')
import pygame

# Load SFX
pygame.mixer.init()
artillery_sfx = pygame.mixer.Sound('assets/audio/artillery.mp3')
artillery_sfx.set_volume(0.5)

laser_sfx = pygame.mixer.Sound('assets/audio/laser.mp3')
laser_sfx.set_volume(0.5)

# Load BFX
game_music = pygame.mixer.Sound('assets/audio/game.wav')
game_music.set_volume(0.5)