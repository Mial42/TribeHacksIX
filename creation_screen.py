from screen import Screen
import pygame

class CreationScreen(Screen):
    def __init__(self, screen, bg_path:str, screen_switch_event_val:int) -> None:
        super().__init__(screen=screen, bg_path=bg_path, screen_switch_event_val=screen_switch_event_val)
        self.setup_mech_button()
        self.setup_start_button()
        self.headlist = ["head1.png", "head2.png","clawdius.png"]
        self.bodylist = ["body1.png", "body2.png"]
        self.legslist = ["legs1.png", "legs2.png"]
        self.currenthead = self.headlist[0]
        self.currentbody = self.bodylist[0]
        self.currentlegs = self.legslist[0]
    def setup_mech_button(self):
        self.button_color = (0, 0, 128)  # Blue button
        self.button_mech = pygame.Rect(300, 300, 200, 50)  # Button dimensions and position
    def handle_mech_button_event(self, event):
        if self.button_rect.collidepoint(event.pos):

    def setup_start_button(self):
        self.button_color = (0, 128, 0)  # Green button
        self.button_start = pygame.Rect(300, 300, 200, 50)  # Button dimensions and position
    def draw_button(self, text):
        pygame.draw.rect(super().__screen, self.button_color, self.button_rect)  # Draw the button
        text_surface = self.font.render(text, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=self.button_rect.center)
        super().get_screen().blit(text_surface, text_rect)
        