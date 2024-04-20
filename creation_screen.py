from screen import Screen
import pygame

class CreationScreen(Screen):
    def __init__(self, screen, bg_path:str, screen_switch_event_val:int, currentlegs: str, currenthead: str, currentbody: str, headlist: list, legslist:list, bodylist: list) -> None:
        super().__init__(screen=screen, bg_path=bg_path, screen_switch_event_val=screen_switch_event_val)
        self.setup_head_next_button()
        self.setup_head_prev_button()
        self.setup_body_next_button()
        self.setup_body_prev_button()
        self.headlist = ["head1.png", "head2.png","clawdius.png"]
        self.bodylist = ["body1.png", "body2.png"]
        self.legslist = ["legs1.png", "legs2.png"]
        self.currenthead = headlist[0]
        self.currentbody = bodylist[0]
        self.currentlegs = legslist[0]
    def setup_head_next_button(self):
        self.button_color = (0, 128, 0)  # Green button
        self.button_rect = pygame.Rect(300, 300, 200, 50)  # Button dimensions and position
    def setup_head_prev_button(self):
        self.button_color = (0, 128, 0)  # Green button
        self.button_rect = pygame.Rect(300, 300, 200, 50)  # Button dimensions and position
    def setup_body_next_button(self):
        self.button_color = (0, 128, 0)  # Green button
        self.button_rect = pygame.Rect(300, 300, 200, 50)  # Button dimensions and position
    def setup_body_prev_button(self):
        self.button_color = (0, 128, 0)  # Green button
        self.button_rect = pygame.Rect(300, 300, 200, 50)  # Button dimensions and position
    def setup_legs_next_button(self):
        self.button_color = (0, 128, 0)  # Green button
        self.button_rect = pygame.Rect(300, 300, 200, 50)  # Button dimensions and position
    def setup_legs_prev_button(self):
        self.button_color = (0, 128, 0)  # Green button
        self.button_rect = pygame.Rect(300, 300, 200, 50)  # Button dimensions and position
    def setup_start_button(self):
        self.button_color = (0, 128, 0)  # Green button
        self.button_rect = pygame.Rect(300, 300, 200, 50)  # Button dimensions and position
