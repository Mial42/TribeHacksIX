import pygame
from pygame import mixer
#import sys
import os

#Screens
import start_screen
import creation_screen
import fighting_screen
import game_over_screen

def run():
    return 0

def main():
    mixer.init()
    pygame.init()

    screen_width = 1080
    screen_height = 600

    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Mecha Fighter!")
    # Run until the user asks to quit

    running = True

    while running:


        # Did the user click the window close button?

        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                running = False


        # Fill the background with white

        screen.fill((255, 255, 255))


        # Draw a solid blue circle in the center

        pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)


        # Flip the display

        pygame.display.flip()


    # Done! Time to quit.

    pygame.quit()
    
    

if __name__ == "__main__":
    main()