from screen import Screen
import pygame
import os
from platform import system

path_separator = {"Windows":["/",r"\\","\\"], "Darwin":[r"\\", "/", "/"], "Linux":[r"\\", "/", "/"]}

class CreationScreen(Screen):
    def __init__(self, screen, bg_path:str, screen_switch_event_val:int) -> None:
        super().__init__(screen=screen, bg_path=bg_path, screen_switch_event_val=screen_switch_event_val)
        #rectangle
        self.font = pygame.font.Font(None, 36)  # Use Pygame's default font
        

        self.headlist = ["./assets/imgs/parts/head1.png", "./assets/imgs/parts/head2.png","assets/imgs/parts/clawdius.png"]
        self.bodylist = ["./assets/imgs/parts/body1.png", "./assets/imgs/parts/body2.png"]
        self.legslist = ["./assets/imgs/parts/legs1.png", "./assets/imgs/parts/legs2.png"]
        self.currenthead = 1
        self.currentbody = 1
        self.currentlegs = 1
       
    def handle_event(self, event):
        if self.start_button.collidepoint(event.pos):
            num = self.currenthead*100 + self.currentbody*10 + self.currentlegs
            super().switch_screen(num)
        elif self.head_prev_button.collidepoint(event.pos):
            if(self.currenthead != 1):
                self.currenthead -= 1
                self.draw_image(1)
        elif self.head_next_button.collidepoint(event.pos):
            if(self.currenthead != 3):
                self.currenthead += 1
                self.draw_image(1)
        elif self.body_prev_button.collidepoint(event.pos):
            if(self.currentbody != 1):
                self.currentbody -= 1
                self.draw_image(2)
        elif self.body_next_button.collidepoint(event.pos):
            if(self.currentbody != 2):
                self.currentbody += 1
                self.draw_image(2)
        elif self.legs_prev_button.collidepoint(event.pos):
            if(self.currentlegs != 1):
                self.currentlegs -= 1
                self.draw_image(3)
        elif self.legs_next_button.collidepoint(event.pos):
            if(self.currentlegs != 2):
                self.currentlegs += 1
                self.draw_image(3)

    def draw_image(self, part):
        if(part == 1):
            img_scaled = pygame.transform.scale(pygame.image.load(os.path.join(self.legslist[self.currentlegs-1]).replace(path_separator[system()][0], path_separator[system()][1])).convert_alpha(), (100, 200))
            img_scaled.set_colorkey((255,255,255)) #force white to be transparent
            super().get_screen().blit(img_scaled, (150, 450))
        elif(part ==2):
            img_scaled = pygame.transform.scale(pygame.image.load(os.path.join(self.bodylist[self.currentbody-1]).replace(path_separator[system()][0], path_separator[system()][1])).convert_alpha(), (100, 200))
            img_scaled.set_colorkey((255,255,255)) #force white to be transparent
            super().get_screen().blit(img_scaled, (150, 250))
        else:
            img_scaled = pygame.transform.scale(pygame.image.load(os.path.join(self.headlist[self.currenthead-1]).replace(path_separator[system()][0], path_separator[system()][1])).convert_alpha(), (100, 200))
            img_scaled.set_colorkey((255,255,255)) #force white to be transparent
            super().get_screen().blit(img_scaled, (150, 50))

    def draw(self):
        super().draw_bg()

        self.draw_image(1)
        self.draw_image(2)
        self.draw_image(3)

        self.screen_hold = super().get_screen()
        self.head_prev_button = pygame.Rect(50, 100, 50, 100) #pygame.Rect(50, 500, 50, 100)
        pygame.draw.rect(super().get_screen(), [128,128,0], self.head_prev_button)
        self.head_next_button = pygame.Rect(550, 100, 50, 100) #pygame.Rect(550, 500, 50, 100)
        pygame.draw.rect(super().get_screen(), [128,128,0], self.head_next_button)
        self.body_prev_button = pygame.Rect(50, 300, 50, 100)
        pygame.draw.rect(super().get_screen(), [128,128,0], self.body_prev_button)
        self.body_next_button = pygame.Rect(550, 300, 50, 100)
        pygame.draw.rect(super().get_screen(), [128,128,0], self.body_next_button)
        self.legs_prev_button = pygame.Rect(50, 500, 50, 100) #pygame.Rect(50, 100, 50, 100)
        pygame.draw.rect(super().get_screen(), [128,128,0], self.legs_prev_button)
        self.legs_next_button = pygame.Rect(550, 500, 50, 100) #pygame.Rect(550, 100, 50, 100)
        pygame.draw.rect(super().get_screen(), [128,128,0], self.legs_next_button)
        self.start_button = pygame.Rect(300, 25, 50, 100)
        pygame.draw.rect(super().get_screen(), [0,128,0], self.start_button)

        #text setup
        start_text = self.font.render("Start", True, (255, 255, 255))  # White text
        self.screen_hold.blit(start_text, (self.start_button.x + 20, self.start_button.y + 10))
        start_text = self.font.render("<---", True, (255, 255, 255))  # White text
        self.screen_hold.blit(start_text, (self.head_prev_button.x + 20, self.head_prev_button.y + 10))
        start_text = self.font.render("--->", True, (255, 255, 255))  # White text
        self.screen_hold.blit(start_text, (self.head_next_button.x + 20, self.head_next_button.y + 10))
        start_text = self.font.render("<---", True, (255, 255, 255))  # White text
        self.screen_hold.blit(start_text, (self.body_prev_button.x + 20, self.body_prev_button.y + 10))
        start_text = self.font.render("--->", True, (255, 255, 255))  # White text
        self.screen_hold.blit(start_text, (self.body_next_button.x + 20, self.body_next_button.y + 10))
        start_text = self.font.render("<---", True, (255, 255, 255))  # White text
        self.screen_hold.blit(start_text, (self.legs_prev_button.x + 20, self.legs_prev_button.y + 10))
        start_text = self.font.render("--->", True, (255, 255, 255))  # White text
        self.screen_hold.blit(start_text, (self.legs_next_button.x + 20, self.legs_next_button.y + 10))