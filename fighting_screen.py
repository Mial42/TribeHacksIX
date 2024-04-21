from screen import Screen
import pygame
import random
import os
from platform import system
import time

path_separator = {"Windows":["/",r"\\","\\"], "Darwin":[r"\\", "/", "/"], "Linux":[r"\\", "/", "/"]}

class FightingScreen(Screen):
    def __init__(self, screen:pygame.display, bg_path:str, screen_switch_event_val:int, score_event:int, design:int):
        super().__init__(screen, bg_path, screen_switch_event_val)
        self.__SCORE_EVENT = score_event
        self.__final_score = 0
        
        #design is a 3 digit value whose digits correspond to a part
        #e.g. 3 - 1 - 2 is a robot with Klaudius (head) - Body 1 - Legs 2
        self.__player_mech = Player(design // 100, (design // 10) % 10, design % 10)

        self.__spawn_rate = 5
        self.__last_spawn = 0
        self.__curtime = time.time()
        self.__spawning = False
        self.__spawnlist = None
    
    def make_enemy_list(self):
        #TODO make sure spawns are staggered
        num_enemies = [Enemy(random.randint(1, 30), random.randint(1, 30), random.randint(1, 30), random.randint(1, 30), random.randint(1, 30), os.path.join("./assets/imgs/enemy/hammer.png").replace(path_separator[system()][0], path_separator[system()][1]))] * random.randint(0,11)
        return num_enemies
    
    def update_enemies(self, enemies):
        rmv = []
        for i in range(len(enemies)):
            if enemies[i].spawned == True:
                check = enemies[i].update_pos()
                if check:
                    rmv.append(i)
        
        for i in range(len(rmv) - 1, -1, -1):
            self.__final_score += enemies[rmv[i]].get_spd()
            enemies.remove(rmv[i])

    
    def draw(self):
        super().draw_bg()
        
        #timer so that player isn't overwhelmed by enemies
        if self.__curtime - self.__last_spawn > self.__spawn_rate and not self.__spawning and not self.__spawnlist:
            l = self.make_enemy_list()
            self.__spawning = True
        elif self.__spawnlist and not self.__spawning:
            self.__last_spawn = time.time()
            del(self.__spawnlist[:])
            self.__spawnlist = None
        elif self.__spawning and self.__curtime - self.__last_spawn > self.__spawn_rate // len(self.__spawnlist) + 1:
            for ele in self.__spawnlist:
                if ele.spawned == False:
                    ele.spawn()
                    break

        self.update_enemies(self.__spawnlist)
        self.__curtime = time.time()
            

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
        self.spawned = False


    def spawn(self):
        img_scaled = pygame.transform.scale(pygame.image.load(os.path.join(self.__imgpath).replace(path_separator[system()][0], path_separator[system()][1]).convert_alpha(), self.__sizeX, self.__sizeY))
        img_scaled.set_colorkey((255,255,255)) #force white to be transparent
        super().get_screen().blit(img_scaled, (self.__sizeX, self.__sizeY))
        self.spawned = True

    def update_pos(self):
        self.__posX -= self.__speed
        img_scaled = pygame.transform.scale(pygame.image.load(os.path.join(self.__imgpath).replace(path_separator[system()][0], path_separator[system()][1]).convert_alpha(), self.__sizeX, self.__sizeY))
        super().get_screen().blit(img_scaled, (self.__posX, self.__posY))

        if self.__posX + self.__sizeX <= 0:
            return 1
        
        return 0
    
    def get_pos(self):
        return (self.__posX, self.__posY, self.__sizeX, self.__sizeY)
    
    def get_spd(self):
        return self.__speed