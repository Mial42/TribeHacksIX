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
    switch_event = pygame.event.custom_type()
    score_event = pygame.event.custom_type()
    score_val = 0
    
    #TODO add background paths to folder and plug those in here
    #TODO replace testbg.png with a real background
    screens = [
        ss.StartScreen(screen=screen, bg_path=os.path.join(r"./assets/imgs/bgs/testbg.png").replace(path_separator[opsys][0], path_separator[opsys][1]), screen_switch_event_val=switch_event),
        cs.CreationScreen(screen=screen, bg_path=os.path.join(r"./assets/imgs/bgs/testbg.png").replace(path_separator[opsys][0], path_separator[opsys][1]), screen_switch_event_val=switch_event)
        #fs.FightingScreen(screen=screen, bg_path=os.path.join(r"./assets/imgs/bgs/testbg.png").replace(path_separator[opsys][0], path_separator[opsys][1]), screen_switch_event_val=switch_event),
        #gos.GameOverScreen(screen=screen, bg_path=os.path.join(r"./assets/imgs/bgs/testbg.png").replace(path_separator[opsys][0], path_separator[opsys][1]), screen_switch_event_val=switch_event),
      ]
    
    running = True
    cur_scr = 0
    cur_scr_obj = screens[0]

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break
            elif event.type == switch_event and cur_scr % 4 == 1:
                cur_scr += (lambda s: 1 if s > 0 else -1)(event.value)
            elif event.type == switch_event:
                cur_scr += event.value
            elif event.type == pygame.MOUSEBUTTONDOWN:
                cur_scr_obj.handle_event(event)

        if not running:
            break
        
        #generate FightingScreen, GameOverScreen so we don't run them in background
        if(cur_scr % 4 == 2):
            cur_scr_obj = fs.FightingScreen(screen=screen, bg_path=os.path.join(r"./assets/imgs/bgs/testbg.png").replace(path_separator[opsys][0], path_separator[opsys][1]), screen_switch_event_val=switch_event, score_event=score_event)
        elif(cur_scr % 4 == 3):
            cur_scr_obj = gos.GameOverScreen(screen=screen, bg_path=os.path.join(r"./assets/imgs/bgs/testbg.png").replace(path_separator[opsys][0], path_separator[opsys][1]), screen_switch_event_val=switch_event, final_score=score_val)
        else:
            cur_scr_obj = screens[cur_scr % 4]
        
        cur_scr_obj.draw()

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