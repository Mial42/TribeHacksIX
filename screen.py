import pygame

class Screen:
    # screen - pygame canvas object
    # bg_path - path to background image
    # screen_switch_event - integer value returned by the custom_event method,
    #   used to send events back to event stream
    def __init__(self, screen, bg_path:str, screen_switch_event_val:int) -> None:
        #setup event to switch screens
        self.__SCREEN_SWITCH_EVENT = screen_switch_event_val
        self.__bg_path = bg_path
        self.__screen = screen

    def draw(self):
        # SIMPLE FUNCTION, CALL WITH super()
        # ADD MORE TO IT
        self.draw_bg()

    def draw_bg(self):
        scaled = pygame.transform.scale(pygame.image.load(self.__bg_path).convert_alpha(), pygame.display.get_window_size())
        self.__screen.blit(scaled, (0,0))

        return

    def switch_screen(self, forward:int):
        pygame.event.post(pygame.event.Event(self.__SCREEN_SWITCH_EVENT, value=forward))

    def handle_event(self, event):
        # DUMMY FUNCTION
        # MUST BE OVERWRITTEN
        return

    def quit(self):
        pygame.event.post(pygame.event.Event(pygame.QUIT))

    def get_bg_path(self):
        return self.__bg_path
    
    def get_screen(self):
        return self.__screen

    #TEST METHOD, NOT TO BE CALLED
    def test_draw(self):
        # Run until the user asks to quit
        running = True

        while running:
            # Did the user click the window close button?
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # Fill the background with white
            self.__screen.fill((255, 255, 255))

            # Draw a solid blue circle in the center
            pygame.draw.circle(self.__screen, (0, 0, 255), (250, 250), 75)

            # Flip the display
            pygame.display.flip()

        # Done! Time to quit.
        pygame.quit()


