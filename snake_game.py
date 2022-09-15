import sys, time, pygame
from settings import DynamicSettings, Settings
from objects import Snake, SnakeHead, Food
from texts import Scoreboard, Text

class Snake_game():
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.screen_rect = self.screen.get_rect()
        pygame.display.set_caption('Snake_game')

        self.snake = []
        self.ds = DynamicSettings(self)
        self.scoreboard = Scoreboard(self) 
        self.msgs = [Text(self, text='press space to start', y=self.screen_rect.bottom-100, font_size=48 ),
         Text(self, text='higscore: '+ str(self.ds.highscore), y=30, font_size=80)]
        self.food = None

    def run_game(self):        
        while True:
            #Oczekiwanie na działanie gracza
            self.check_events()
            pygame.display.flip()
            if self.settings.game_active:           
                self.update_screen()
                self.calculate_tail_positions()
                self.check_collisions()  
                time.sleep(0.5 / self.ds.snake_speed)
                self.increase_speed()
            else:
                for msg in self.msgs:
                    msg.print_text()
                
                                  
    def check_events(self):
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    self._check_keydown_events(event)
   
    def calculate_tail_positions(self):
        for snake_part in self.snake[::-1]:
            index = self.snake.index(snake_part)
            if index > 0:
                snake_part.rect.center = self.snake[index-1].rect.center
            else:
                snake_part.update_head_position()
            
    def update_screen(self):
            self.screen.fill(self.settings.bg_color)            
            self.food.draw()
            for snake_part in self.snake:
                snake_part.draw()
            self.scoreboard.show_score()            
            
    def check_collisions(self):

        def check_border_collision():
            if self.snake[0].rect.x < self.screen_rect.left or self.snake[0].rect.x >= self.screen_rect.right or \
                self.snake[0].rect.y < self.screen_rect.top or self.snake[0].rect.y >= self.screen_rect.bottom:
                self.lose_game()

        def check_tail_collision():
            for snake_part in self.snake[1:]:
                if pygame.Rect.colliderect(self.snake[0].rect, snake_part.rect):
                    self.lose_game()

        def check_food_collison():
            if pygame.Rect.colliderect(self.snake[0].rect, self.food.rect):
                self.food = Food(self)
                #add snake_part
                self.snake.append(Snake(self))
                self.ds.score +=self.ds.food_points
                self.scoreboard.preparate_score()
                if self.ds.highscore < self.ds.score:
                    self.ds.highscore = self.ds.score
                self.increse_food_points()

        check_border_collision()
        check_tail_collision()
        check_food_collison()

    def check_elapsed_time(self):
        self.elapsed_time = time.time() - self.starting_time

    def increase_speed(self):
        self.elapsed_time = time.time() - self.starting_time
        if self.elapsed_time >30:
            self.starting_time = time.time()
            self.ds.snake_speed += 1   
    
    def increse_food_points(self):
        if len(self.snake)%5 ==0:
            self.ds.food_points *= self.ds.snake_speed/5 * 1.1
            self.ds.food_points = int(self.ds.food_points)
    
    def prepare_new_game(self):
        self.snake = [SnakeHead(self)]
        self.food = Food(self)
        self.ds.score = 0
        self.ds.snake_speed = self.settings.snake_speed
        self.ds.food_points = self.settings.food_points
        self.scoreboard = Scoreboard(self)
        self.settings.game_active = True
        self.snake[0].roll_starting_direction()
        self.starting_time = time.time()
    
    def lose_game(self):
        self.settings.game_active = False
        self.msgs[1] = Text(self, text='higscore: '+ str(self.ds.highscore), y=30, font_size=80 )

    def _check_keydown_events(self, event):
        if event.key == pygame.K_SPACE and self.settings.game_active ==False:
            self.prepare_new_game()
        elif event.key == pygame.K_RIGHT and self.snake[0].moving_y:
            self.snake[0].moving_x = 1
            self.snake[0].moving_y = 0
        elif event.key == pygame.K_LEFT and self.snake[0].moving_y:
            self.snake[0].moving_x = -1
            self.snake[0].moving_y = 0
        elif event.key == pygame.K_UP and self.snake[0].moving_x:
            self.snake[0].moving_x = 0
            self.snake[0].moving_y = -1
        elif event.key == pygame.K_DOWN and self.snake[0].moving_x:
            self.snake[0].moving_x = 0
            self.snake[0].moving_y = 1


if __name__=='__main__':
    sg = Snake_game()
    sg.run_game()