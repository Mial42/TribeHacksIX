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
        self.__spawnlist = []
    
    def make_enemy_list(self):
        #TODO make sure spawns are staggered
        self.__spawnlist = [Enemy(pygame.display.get_window_size()[0], random.randint(0,pygame.display.get_window_size()[1]), random.randint(1, 30), random.randint(1, 30), random.randint(1, 30), os.path.join("./assets/imgs/enemy/hammer.png").replace(path_separator[system()][0], path_separator[system()][1]))] * random.randint(1,11)
        #return num_enemies
    
    def update_enemies(self):
        rmv = []
        for i in range(len(self.__spawnlist)):
            if self.__spawnlist[i].img_scaled is not None:
                check = self.__spawnlist[i].update_pos()
                if check:
                    rmv.append(i)
        
        for i in range(len(rmv) - 1, -1, -1):
            self.__final_score += self.__spawnlist[rmv[i]].get_spd()
            self.__spawnlist.remove(rmv[i])
        
        print(len(self.__spawnlist))

    
    def draw(self):
        super().draw_bg()

        #timer so that player isn't overwhelmed by enemies
        if (self.__curtime - self.__last_spawn) > self.__spawn_rate and not self.__spawning and not self.__spawnlist:
            print(f"Setting up spawn list {self.__spawning} {self.__spawnlist}")
            self.make_enemy_list()
            self.__spawning = True
        elif self.__spawnlist and not self.__spawning:
            print(f"stopping spawn {self.__spawning} {self.__spawnlist}")
            self.__last_spawn = time.time()
        elif self.__spawning and (self.__curtime - self.__last_spawn) > (self.__spawn_rate // len(self.__spawnlist) + .5):
            print(f"looking for next spawnable enemy {self.__spawning} {self.__spawnlist}")
            for ele in self.__spawnlist:
                if ele.img_scaled is None:
                    ele.spawn()
                    super().get_screen().blit(ele.img_scaled, (self.__posX, self.__posY))
                    self.__last_spawn = time.time()
                    break
            self.__spawning = False
        print(f"{self.__spawning} {self.__spawnlist}")
        self.update_enemies()
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
        self.img_scaled = None


    def spawn(self):
        self.img_scaled = pygame.transform.scale(pygame.image.load(os.path.join(self.__imgpath).replace(path_separator[system()][0], path_separator[system()][1]).convert_alpha(), self.__sizeX, self.__sizeY))
        self.img_scaled.set_colorkey((255,255,255)) #force white to be transparent

    def update_pos(self):
        self.__posX -= self.__speed
        self.img_scaled = pygame.transform.scale(pygame.image.load(os.path.join(self.__imgpath).replace(path_separator[system()][0], path_separator[system()][1]).convert_alpha(), self.__sizeX, self.__sizeY))

        if self.__posX + self.__sizeX <= 0:
            self.img_scaled = None
            return 1
        
        return 0
    
    def get_pos(self):
        return (self.__posX, self.__posY, self.__sizeX, self.__sizeY)
    
    def get_spd(self):
        return self.__speed