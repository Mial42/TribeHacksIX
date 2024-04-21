from screen import Screen
import pygame
import random
import os
from platform import system

path_separator = {"Windows":["/",r"\\","\\"], "Darwin":[r"\\", "/", "/"], "Linux":[r"\\", "/", "/"]}

class FightingScreen(Screen):
    def __init__(self, screen:pygame.display, bg_path:str, screen_switch_event_val:int, score_event:int, design:int):
        super().__init__(screen, bg_path, screen_switch_event_val)
        self.__SCORE_EVENT = score_event
        self.__final_score = 0
        
        #design is a 3 digit value whose digits correspond to a part
        #e.g. 3 - 1 - 2 is a robot with Klaudius (head) - Body 1 - Legs 2
        self.__player_mech = Player(design // 100, (design // 10) % 10, design % 10)
    
    def spawn_enemies(self):
        num_enemies = [Enemy(random.randint(1, 30), random.randint(1, 30), random.randint(1, 30), random.randint(1, 30), random.randint(1, 30), os.path.join("./assets/imgs/enemy/hammer.png").replace(path_separator[system()][0], path_separator[system()][1]))] * random.randint(0,11)
        
        return

    def update_score(self):
        self.__final_score += 1
    
    def draw(self):
        super().draw_bg()
        

    #TODO set up game for real
    def end_state(self):
        pygame.event.post(pygame.event.Event(self.__SCORE_EVENT, value=self.__final_score))
        super().switch_screen()

class Player:
    def __init__(self, head:int, core:int, legs:int) -> None:
        pass

class Enemy:
    def __init__(self, posX:int, posY:int, sizeX:int, sizeY:int, speed:int, imgpath:str) -> None:
        self.__posX = posX
        self.__posY = posY
        self.__sizeX = sizeX
        self.__sizeY = sizeY
        self.__imgpath = imgpath
        #limit speed by however large the enemy is
        self.__speed = (lambda s: s if s < self.__sizeX else self.__sizeX - 10)(speed)

        img_scaled = pygame.transform.scale(pygame.image.load(os.path.join(self.__imgpath).replace(path_separator[system()][0], path_separator[system()][1]).convert_alpha(), self.__sizeX, self.__sizeY))
        super().get_screen.blit(img_scaled, (self.__sizeX, self.__sizeY))

    def update_pos(self):
        self.__posX -= self.__speed
        img_scaled = pygame.transform.scale(pygame.image.load(os.path.join(self.__imgpath).replace(path_separator[system()][0], path_separator[system()][1]).convert_alpha(), self.__sizeX, self.__sizeY))
        super().get_screen.blit(img_scaled, (self.__posX, self.__posY))

        if 