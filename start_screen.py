from screen import Screen
import pygame

class StartScreen(Screen):
    def __init__(self, screen:pygame.display, bg_path:str, screen_switch_event_val:int) -> None:
        super().__init__(screen, bg_path, screen_switch_event_val)
    
        self.start_rct = pygame.Rect(pygame.display.get_window_size()[0] / 2 - 50, pygame.display.get_window_size()[1] / 2 - 50, 100, 100)
    
        self.quit_rct = pygame.Rect(pygame.display.get_window_size()[0] / 2 - 50, pygame.display.get_window_size()[1] / 2 + 100, 100, 100)

    def handle_event(self, event):
        if self.start_rct.collidepoint(event.pos):
            super().switch_screen(1)
        elif self.quit_rct.collidepoint(event.pos):
            pygame.event.post(pygame.QUIT)
        

    