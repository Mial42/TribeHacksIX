import pygame
from pygame import mixer
#import sys

def run():
    return 0

def main():
    mixer.init()
    pygame.init()

    screen_width = 1080
    screen_height = 600

    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Mecha Fighter!")
    
    

if __name__ == "__main__":
    main()