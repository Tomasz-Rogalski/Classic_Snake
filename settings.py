class Settings():
    def __init__(self) -> None:
        self.screen_width = 1000
        self.screen_height = 800
        self.bg_color = (0, 0, 0)

        self.snake_color = (220,220,220)
        self.snake_size = 20
        self.snake_speed = 5.0
        self.snake_step = self.snake_size

        self.food_color = (150,0,0)
        self.food_points = 100
    
        self.game_active = False


class DynamicSettings():
    def __init__(self, sgame, hs=0) -> None:
        self.score = 0
        self.highscore = 0
        self.food_points = sgame.settings.food_points
        self.snake_speed = 5.0





        