from screen import Screen
import pygame

class CreationScreen(Screen):
    def __init__(self, screen, bg_path:str, screen_switch_event_val:int, int currenthead, int currentbody, int currentlegs) -> None:
        super().__init__(screen=screen, bg_path=bg_path, screen_switch_event_val=screen_switch_event_val)
        self.setup_mech_button()
        self.setup_mech_button()
        self.setup_mech_button()
        self.setup_mech_button()
        self.setup_mech_button()
        self.setup_mech_button()
        self.setup_mech_button()
        self.setup_start_button()
        self.headlist = ["head1.png", "head2.png","clawdius.png"]
        self.bodylist = ["body1.png", "body2.png"]
        self.legslist = ["legs1.png", "legs2.png"]
        self.currenthead = 1
        self.currentbody = 1
        self.currentlegs = 1
    def setup_mech_button(self, x, y):
        self.button_color = (0, 0, 128)  # Blue button
        self.button_mech = pygame.Rect(x, y, 200, 50)  # Button dimensions and position
       
    def handle_start_button_event(self, event):
        if self.button_rect.collidepoint(event.pos):
            # return 'start_screen'  #Need to switch to start
            str num = currenthead + currentbody + currentlegs
            super().switch_screen()
    def setup_start_button(self):
        self.button_color = (0, 128, 0)  # Green button
        self.button_start = pygame.Rect(300, 300, 200, 50)  # Button dimensions and position
    def draw_button(self, text):
        pygame.draw.rect(super().__screen, self.button_color, self.button_rect)  # Draw the button
        text_surface = self.font.render(text, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=self.button_rect.center)
        img_scaled = pygame.transform.scale(pygame.image.load(imgpath).convert_alpha(), sizeX, sizeY))
        super().get_screen.blit(img_scaled, (posX, posY))
        img_scaled = pygame.transform.scale(pygame.image.load(imgpath).convert_alpha(), sizeX, sizeY))
        super().get_screen.blit(img_scaled, (posX, posY))
        img_scaled = pygame.transform.scale(pygame.image.load(imgpath).convert_alpha(), sizeX, sizeY))
        super().get_screen.blit(img_scaled, (posX, posY))
        super().get_screen().blit(text_surface, text_rect)
