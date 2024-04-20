from screen import Screen
import pygame

class StartScreen(Screen):
    def __init__(self, screen:pygame.display, bg_path:str) -> None:
        super().__init__(screen, bg_path)
    
