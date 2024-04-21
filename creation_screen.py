from screen import Screen
import pygame

class CreationScreen(Screen):
    def __init__(self, screen, bg_path:str, screen_switch_event_val:int) -> None:
        super().__init__(screen=screen, bg_path=bg_path, screen_switch_event_val=screen_switch_event_val)
        #rectangle

        self.head_prev_button = pygame.Rect(50, 500, 50, 100)
        pygame.draw.rect(super().get_screen(), [128,128,0], self.head_prev_button)
        self.head_next_button = pygame.Rect(550, 500, 50, 100)
        pygame.draw.rect(super().get_screen(), [128,128,0], self.head_next_button)
        self.body_prev_button = pygame.Rect(50, 500, 50, 100)
        pygame.draw.rect(super().get_screen(), [128,128,0], self.body_prev_button)
        self.body_next_button = pygame.Rect(550, 500, 50, 100)
        pygame.draw.rect(super().get_screen(), [128,128,0], self.body_next_button)
        self.legs_prev_button = pygame.Rect(50, 500, 50, 100)
        pygame.draw.rect(super().get_screen(), [128,128,0], self.legs_prev_button)
        self.legs_next_button = pygame.Rect(550, 500, 50, 100)
        pygame.draw.rect(super().get_screen(), [128,128,0], self.legs_next_button)
        self.start_button = pygame.Rect(50, 500, 50, 100)
        pygame.draw.rect(super().get_screen(), [0,128,0], self.start_button)

        #text setup
        start_text = font.render("Start", True, (255, 255, 255))  # White text
        screen_hold.blit(start_text, (self.start_rct.x + 20, self.start_rct.y + 10))
        self.setup_start_button()
        self.headlist = ["assets/imgs/head1.png", "assets/imgs/head2.png","assets/imgs/clawdius.png"]
        self.bodylist = ["assets/imgs/body1.png", "assets/imgs/body2.png"]
        self.legslist = ["assets/imgs/legs1.png", "assets/imgs/legs2.png"]
        self.currenthead = 1
        self.currentbody = 1
        self.currentlegs = 1
       
    def handle_start_button_event(self, event):
        if self.button_rect.collidepoint(event.pos):
            # return 'start_screen'  #Need to switch to start
            num = self.currenthead*100 + self.currentbody*10 + self.currentlegs
            super().switch_screen(num)
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
