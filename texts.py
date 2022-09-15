import pygame.font

class Scoreboard():
    def __init__(self, sgame) -> None:
        self.screen = sgame.screen
        self.screen_rect = self.screen.get_rect()
        self.ds= sgame.ds
        self.settings = sgame.settings
        self.text_color = (255,255,0)
        self.font = pygame.font.SysFont(None, 48)
        self.preparate_score()

    def preparate_score(self):
        self.score_image = self.font.render(str(self.ds.score), True, self.text_color, self.settings.bg_color)
        self.score_rect = self.score_image.get_rect()
        self.score_rect.topright = self.screen_rect.topright 

    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)


class Text():
    def __init__(self, sgame, text, y, font_size) :
        self.text = text.upper()
        self.screen = sgame.screen
        self.screen_rect = self.screen.get_rect()
        self.ds= sgame.ds
        self.settings = sgame.settings

        self.text_color = (255,255,0)
        self.font = pygame.font.SysFont(None, font_size)
        self.text_image = self.font.render(self.text, True, self.text_color, self.settings.bg_color)
        self.text_rect = self.text_image.get_rect()
        self.text_rect.center = self.screen_rect.center
        self.text_rect.y = y

    def print_text(self):
        self.screen.blit(self.text_image, self.text_rect)

            
