from screen import Screen
import pygame

class FightingScreen(Screen):
    def __init__(self, screen:pygame.display, bg_path:str, screen_switch_event_val:int):
        super().__init__(screen, bg_path, screen_switch_event_val)
    
