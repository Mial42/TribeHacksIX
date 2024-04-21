from screen import Screen
import pygame

class GameOverScreen(Screen):
    def __init__(self, screen: pygame.display, bg_path: str, screen_switch_event_val:int):#, final_score: int):
        super().__init__(screen, bg_path, screen_switch_event_val)
        self.final_score = 0
        self.font = pygame.font.Font(None, 36)  # Use Pygame's default font
        self.setup_button()

    def set_final_score(self, score):
        self.final_score = score

    def setup_button(self):
        self.button_color = (0, 128, 0)  # Green button
        self.button_rect = pygame.Rect(300, 300, 200, 50)  # Button dimensions and position

    def draw_text(self, text, position, color=(255, 255, 200)):
        text_surface = self.font.render(text, True, color)
        super().get_screen().blit(text_surface, position)

    def draw_button(self, text):
        pygame.draw.rect(super().get_screen(), self.button_color, self.button_rect)  # Draw the button
        text_surface = self.font.render(text, True, (255, 255, 200))
        text_rect = text_surface.get_rect(center=self.button_rect.center)
        super().get_screen().blit(text_surface, text_rect)

    def draw(self):
        screen_hold = super().get_screen()
        screen_hold.fill((0, 0, 0))  # Clear the screen with black

        self.draw_text(f'Final Score: {self.final_score}', (300, 200))
        self.draw_button('Back to Start')

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

