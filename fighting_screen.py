from screen import Screen
import pygame
import random
import os
from platform import system
import time

path_separator = {"Windows":["/",r"\\","\\"], "Darwin":[r"\\", "/", "/"], "Linux":[r"\\", "/", "/"]}

class FightingScreen(Screen):
    def __init__(self, screen:pygame.display, bg_path:str, screen_switch_event_val:int, score_event:int):#, design:int):
        super().__init__(screen, bg_path, screen_switch_event_val)
        self.__SCORE_EVENT = score_event
        self.__final_score = 0
        
        #design is a 3 digit value whose digits correspond to a part
        #e.g. 3 - 1 - 2 is a robot with Klaudius (head) - Body 1 - Legs 2
        self.__player_mech = None

        self.__spawn_rate = 5
        self.__last_spawn = 0
        self.__curtime = 0
        self.__spawning = False
        self.__spawnlist = []
        self.__starttime = time.time()

    def set_design(self, design:int):
        self.__player_mech = Player(design // 100, (design // 10) % 10, design % 10)
        
    def make_enemy_list(self):
        #TODO make sure spawns are staggered
        self.__spawnlist = [Enemy(pygame.display.get_window_size()[0], random.randint(0,pygame.display.get_window_size()[1]), random.randint(1, 30), random.randint(1, 30), random.randint(1, 30), os.path.join("./assets/imgs/enemy/hammer.png").replace(path_separator[system()][0], path_separator[system()][1]))] * random.randint(1,11)
        #return num_enemies
    
    def update_enemies(self):
        rmv = []
        for i in range(len(self.__spawnlist)):
            if self.__spawnlist[i].img_scaled is not None:
                check = self.__spawnlist[i].update_pos()
                if check == 1:
                    rmv.append(i)
        
        for i in range(len(rmv) - 1, -1, -1):
            self.__final_score += self.__spawnlist[rmv[i]].get_spd()
            self.__spawnlist.remove(rmv[i])
            
    def draw(self):
        super().draw_bg()

        #timer so that player isn't overwhelmed by enemies
        if not self.__spawning and len(self.__spawnlist) == 0:
            print(f"Setting up spawn list {self.__spawning} {self.__spawnlist}")
            self.make_enemy_list()
            self.__spawning = True
            print(f"************************** {self.__spawning} {self.__spawnlist}")
        elif self.__spawning and (self.__curtime - self.__last_spawn) > 0.5:
            print(f"looking for next spawnable enemy {self.__spawning} {self.__spawnlist}")
            for ele in self.__spawnlist:
                if ele.img_scaled is None:
                    ele.spawn()
                    super().get_screen().blit(ele.img_scaled, (ele.get_pos()[:2]))
                    self.__last_spawn = time.time() - self.__curtime
                    break
            self.__spawning = False
        elif not self.__spawning and self.__spawnlist:
            self.end_state()
            #self.__last_spawn = time.time() - self.__starttime
        #print(f"{self.__spawning} {self.__spawnlist} {self.__curtime} {self.__last_spawn}")
        
        self.update_enemies()
        self.__curtime = time.time() - self.__starttime
            

    #TODO set up game for real
    def end_state(self):
        pygame.event.post(pygame.event.Event(self.__SCORE_EVENT, value=self.__final_score))
        super().switch_screen(1)

class Player:
    def __init__(self, head:int, core:int, legs:int) -> None:
        self.headlist = ["./assets/imgs/head1.png", "./assets/imgs/head2.png","assets/imgs/clawdius.png"]
        self.bodylist = ["./assets/imgs/body1.png", "./assets/imgs/body2.png"]
        self.legslist = ["./assets/imgs/legs1.png", "./assets/imgs/legs2.png"]

        self.__head = self.headlist[head-1]
        self.__body = self.bodylist[core-1]
        self.__legs = self.legslist[legs-1]

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
        self.img_scaled = pygame.transform.scale(pygame.image.load(os.path.join(self.__imgpath).replace(path_separator[system()][0], path_separator[system()][1])).convert_alpha(), (self.__sizeX, self.__sizeY))
        self.img_scaled.set_colorkey((255,255,255)) #force white to be transparent

    def update_pos(self):
        self.__posX -= self.__speed
        self.img_scaled = pygame.transform.scale(pygame.image.load(os.path.join(self.__imgpath).replace(path_separator[system()][0], path_separator[system()][1])).convert_alpha(), (self.__sizeX, self.__sizeY))

        if self.__posX + self.__sizeX <= 0:
            return 1
        
        return 0
    
    def get_pos(self):
        return (self.__posX, self.__posY, self.__sizeX, self.__sizeY)
    
    def get_spd(self):
        return self.__speed