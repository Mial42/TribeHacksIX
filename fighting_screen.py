from screen import Screen
import pygame

class FightingScreen(Screen):
    def __init__(self, screen:pygame.display, bg_path:str, screen_switch_event_val:int, score_event):
        super().__init__(screen, bg_path, screen_switch_event_val)
        self.__SCORE_EVENT = score_event
        self.__final_score = 0
    
    #TODO set up game for real
    def end_state(self):
        pygame.event.post(pygame.event.Event(self.__SCORE_EVENT, value=self.__final_score))
        super().switch_screen()
        