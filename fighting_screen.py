from screen import Screen
import pygame
import random
import os
from platform import system

path_separator = {"Windows":["/",r"\\","\\"], "Darwin":[r"\\", "/", "/"], "Linux":[r"\\", "/", "/"]}

class FightingScreen(Screen):
    def __init__(self, screen:pygame.display, bg_path:str, screen_switch_event_val:int, score_event):
        super().__init__(screen, bg_path, screen_switch_event_val)
        self.__SCORE_EVENT = score_event
        self.__final_score = 0
    
    def spawn_enemies(self):
        num_enemies = [Enemy(random.randint(1, 30), random.randint(1, 30), random.randint(1, 30), random.randint(1, 30), random.randint(1, 30), os.path.join("./assets/imgs/enemy/hammer.png").replace(path_separator[system()][0], path_separator[system()][1]))]random.randint(0,11)
        
        return

    #TODO set up game for real
    def end_state(self):
        pygame.event.post(pygame.event.Event(self.__SCORE_EVENT, value=self.__final_score))
        super().switch_screen()

class Enemy:
    def __init__(self, posX:int, posY:int, sizeX:int, sizeY:int, speed:int, imgpath:str):
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