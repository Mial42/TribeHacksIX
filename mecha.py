class Mecha():
    
    def __init__(self, head, chest, arms, legs):
        self.head = head
        self.chest = chest
        self.arms = arms
        self.legs = legs


class Head():
    def __init__(self, spritepath, health):
        #TODO initialize spritepath
        self.health = health

class Chest():
    def __init__(self, spritepath, health):
        #TODO initialize spritepath
        self.health = health

class Arms():
    def __init__(self, spritepath, health, attack):
        #TODO initialize spritepath
        self.health = health

class Legs():
    def __init__(self, spritepath, health, speed):
        #TODO initialize spritepath
        self.health = health
        self.speed = speed


