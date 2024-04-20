from screen import Screen
import pygame

class StartScreen(Screen):
    def __init__(self, screen:pygame.display, bg_path:str, screen_switch_event_val:int) -> None:
        super().__init__(screen, bg_path, screen_switch_event_val)
    
    # Define button colors
        self.start_color = (0, 255, 0)  # Green
        self.quit_color = (255, 0, 0)   # Red
        
        # Define button positions and dimensions
        window_width, window_height = pygame.display.get_window_size()
        button_width = 100
        button_height = 50
        button_spacing = 100
        button_x = (window_width - button_width) // 2
        start_button_y = (window_height - (2 * button_height + button_spacing)) // 2
        quit_button_y = start_button_y + button_height + button_spacing
        
        # Create button rectangles
        self.start_rct = pygame.Rect(button_x, start_button_y, button_width, button_height)
        self.quit_rct = pygame.Rect(button_x, quit_button_y + button_spacing, button_width, button_height)

    def handle_event(self, event):
        if self.start_rct.collidepoint(event.pos):
            super().switch_screen(1)
        elif self.quit_rct.collidepoint(event.pos):
            super().quit()
        
    def draw(self):
        # Draw background
        super().draw()

        screen_hold = super().get_screen()
        # Draw buttons
        pygame.draw.rect(super().get_screen(), self.start_color, self.start_rct)
        pygame.draw.rect(super().get_screen(), self.quit_color, self.quit_rct)
        
        # Add text to buttons
        font = pygame.font.Font(None, 36)
        start_text = font.render("Start", True, (255, 255, 255))  # White text
        quit_text = font.render("Quit", True, (255, 255, 255))    # White text
        screen_hold.blit(start_text, (self.start_rct.x + 20, self.start_rct.y + 10))
        screen_hold.blit(quit_text, (self.quit_rct.x + 30, self.quit_rct.y + 10))

    