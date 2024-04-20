import pygame
class Mecha():
    
    def __init__(self, head, chest, arms, legs, x, y):
        self.head = head
        self.chest = chest
        self.arms = arms
        self.legs = legs
        self.x = x
        self.y = y

        self.can_move = True
        self.is_stunned = False
        self.jump = False
        self.attacking = False
        self.hit = False
        self.health = head.health + chest.health + arms.health + legs.health


    
    def move(self, dy, dx):
        if self.can_move:
            self.x += self.legs.speed * dx
            self.y += self.legs.speed * dy
        else:
            return
        
    def draw(self, surface):
        surface.blit(self.legs.sprite, (self.x, self.y))
        surface.blit(self.chest.sprite, (self.x, self.y+self.legs.height))
        surface.blit(self.arms.sprite, (self.x+self.chest.width, self.y+self.legs.height))
        surface.blit(self.head.sprite, (self.x, self.y+self.legs.height+self.chest.height))




    def update(self):
            #check what action the player is performing
        if self.health <= 0:
            self.health = 0
            self.alive = False
            self.update_action(6)
        elif self.jump:
            self.update_action(2)
        elif self.attacking:
            self.update_action(3)
        elif self.hit:
            self.update_action(5)



    def attack(self, target):
        # Simple attack reducing target health by a fixed amount
        damage = self.arms.damage  
        target.health -= damage  

    




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
    def __init__(self, spritepath, health, damage, height):
        #TODO initialize spritepath
        self.sprite = pygame.image.load(spritepath)
        self.health = health
        self.height = height
        self.damage = damage

class Legs():
    def __init__(self, spritepath, health, speed, height):
        #TODO initialize spritepath
        self.sprite = pygame.image.load(spritepath)
        self.health = health
        self.speed = speed
        self.height = height


