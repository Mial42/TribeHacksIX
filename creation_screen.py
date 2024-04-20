from screen import Screen
import pygame

class CreationScreen(Screen):
    def __init__(self, screen, bg_path:str) -> None:
        super().__init__(screen=screen, bg_path=bg_path)