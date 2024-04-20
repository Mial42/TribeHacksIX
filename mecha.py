import pygame
class Mecha():
    
    def __init__(self, head, chest, arms, legs, x, y):
        self.head = head
        self.chest = chest
        self.arms = arms
        self.legs = legs
        self.can_move = True
    
    def move(self, dy, dx):
        if self.can_move:
            self.x += self.legs.speed * dx
            self.y += self.legs.speed * dy
        else:
            return
        
    def draw(self, surface):
        # Assuming each part's sprite is centered on the same coordinates
        surface.blit(self.legs.sprite, (self.x, self.y))
        surface.blit(self.chest.sprite, (self.x, self.y+self.legs.height))
        surface.blit(self.arms.sprite, (self.x+self.chest.width, self.y+self.legs.height))
        surface.blit(self.head.sprite, (self.x, self.y+self.legs.height+self.chest.height))




    def update(self):

    def attack(self,target):




class Head():
    def __init__(self, spritepath, health, height):
        #TODO initialize spritepath
        self.sprite = pygame.image.load(spritepath)
        self.health = health
        self.height = height

class Chest():
    def __init__(self, spritepath, health, height, width):
        #TODO initialize spritepath
        self.sprite = pygame.image.load(spritepath)
        self.health = health
        self.height = height
        self.width = width

class Arms():
    def __init__(self, spritepath, health, attack, height):
        #TODO initialize spritepath
        self.sprite = pygame.image.load(spritepath)
        self.health = health
        self.height = height

class Legs():
    def __init__(self, spritepath, health, speed, height):
        #TODO initialize spritepath
        self.sprite = pygame.image.load(spritepath)
        self.health = health
        self.speed = speed
        self.height = height


