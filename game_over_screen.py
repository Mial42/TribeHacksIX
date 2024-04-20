from screen import Screen
import pygame
from screen import Screen

class GameOverScreen(Screen):
    def __init__(self, screen: pygame.display, bg_path: str, screen_switch_event_val:int, final_score: int):
        super().__init__(screen, bg_path, screen_switch_event_val)
        self.final_score = final_score
        self.font = pygame.font.Font(None, 36)  # Use Pygame's default font
        self.setup_button()

    def setup_button(self):
        self.button_color = (0, 128, 0)  # Green button
        self.button_rect = pygame.Rect(300, 300, 200, 50)  # Button dimensions and position

    def draw_text(self, text, position, color=(255, 255, 255)):
        text_surface = self.font.render(text, True, color)
        self.screen.blit(text_surface, position)

    def draw_button(self, text):
        pygame.draw.rect(self.screen, self.button_color, self.button_rect)  # Draw the button
        text_surface = self.font.render(text, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=self.button_rect.center)
        self.screen.blit(text_surface, text_rect)

    def display(self):
        self.screen.fill((0, 0, 0))  # Clear the screen with black
        if self.bg:
            self.screen.blit(self.bg, (0, 0))  # Draw the background if it exists

        self.draw_text(f'Final Score: {self.final_score}', (300, 200))
        self.draw_button('Back to Start')
        pygame.display.flip()  # Update the display

    def handle_event(self, event):
        #if event.type == pygame.MOUSEBUTTONDOWN:
            if self.button_rect.collidepoint(event.pos):
                # return 'start_screen'  #Need to switch to start
                super().switch_screen(1)
    

# # Usage example within a game loop or controller:
# screen = pygame.display.set_mode((800, 600))  # Main game screen
# bg_path = 'path_to_background_image.jpg'
# final_score = 123

# game_over_screen = GameOverScreen(screen, bg_path, final_score)

# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#         elif event.type == pygame.MOUSEBUTTONDOWN:
#             action = game_over_screen.handle_event(event)
#             if action == 'start_screen':
#                 # Switch to start screen logic
#                 print("Go to start screen")

#     game_over_screen.display()

