import pygame
import os

class Screen:

    def __init__(self, screen, bg_path:str) -> None:
        self.__bg_path = bg_path
        self.__screen = screen
        #self.__engine = pygame_game

    def draw_bg(self):
        scaled = pygame.transform.scale(pygame.image.load(self.__bg_path).convert_alpha(), pygame.display.get_window_size())
        self.__screen.blit(scaled, (0,0))

        return

    def test_draw(self):
        # Run until the user asks to quit
        running = True

        while running:
            # Did the user click the window close button?
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # Fill the background with white
            self.__screen.fill((255, 255, 255))

            # Draw a solid blue circle in the center
            pygame.draw.circle(self.__screen, (0, 0, 255), (250, 250), 75)

            # Flip the display
            pygame.display.flip()

        # Done! Time to quit.
        pygame.quit()


