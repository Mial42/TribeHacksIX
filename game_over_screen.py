from screen import Screen
import pygame

class GameOverScreen(Screen):
    def __init__(self, screen:pygame.display, bg_path:str):
        super().__init__(screen, bg_path)
    
