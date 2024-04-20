from screen import Screen
import pygame

class StartScreen(Screen):
    def __init__(self, screen:pygame.display, bg_path:str, screen_switch_event_val:int) -> None:
        super().__init__(screen, bg_path, screen_switch_event_val)
    
    def start_button(self):
        return
    
    def quit_button(self):
        pygame.event.post(pygame.QUIT)