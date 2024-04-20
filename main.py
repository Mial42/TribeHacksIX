import pygame
from pygame import mixer
import os
import platform

#Screens
import start_screen as ss
import creation_screen as cs
import fighting_screen as fs
import game_over_screen as gos

#setup path separators just to deal with mixed slashing
#yes, it's awful
path_separator = {"Windows":["/",r"\\","\\"], "Darwin":[r"\\", "/", "/"], "Linux":[r"\\", "/", "/"]}

#run the game
# screen - pygame.display var that was set in main()
def run(screen:pygame.display):
    opsys = platform.system()
    switch_val = pygame.event.custom_type()
    #TODO add background paths to folder and plug those in here
    #TODO replace testbg.png with a real background
    screens = [
        ss.StartScreen(screen=screen, bg_path=os.path.join(r"./assets/imgs/bgs/testbg.png").replace(path_separator[opsys][0], path_separator[opsys][1]), screen_switch_event_val=switch_val),
        cs.CreationScreen(screen=screen, bg_path=os.path.join(r"./assets/imgs/bgs/testbg.png").replace(path_separator[opsys][0], path_separator[opsys][1]), screen_switch_event_val=switch_val),
        fs.FightingScreen(screen=screen, bg_path=os.path.join(r"./assets/imgs/bgs/testbg.png").replace(path_separator[opsys][0], path_separator[opsys][1]), screen_switch_event_val=switch_val),
        gos.GameOverScreen(screen=screen, bg_path=os.path.join(r"./assets/imgs/bgs/testbg.png").replace(path_separator[opsys][0], path_separator[opsys][1]), screen_switch_event_val=switch_val),
      ]
    
    running = True
    cur_scr = 0

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break
            if event.type == pygame.event.custom_type():
                cur_scr += 1
        screens[cur_scr % 4].draw_bg()

        pygame.display.flip()

    pygame.quit()

    return 0

def main():
    mixer.init()
    pygame.init()

    #TODO add way to change resolution
    screen_width = 1080
    screen_height = 600

    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Mecha Fighter!")

    run(screen)

    return 0

if __name__ == "__main__":
    main()