import pygame, random, sys, pygame_menu

pygame.init()
screen_size = 800
screen = pygame.display.set_mode((screen_size, screen_size))
clock = pygame.time.Clock()
pygame.display.set_caption('Snake By Vladislav Taskaev')
board_coordinates = (0, 49)  # it's 49x49 field, we cannot 800x800 - it'll be so small
pixel_size = screen_size / (board_coordinates[1] + 1)  # +1 because we think in matrix - 0 also pixel
bd_image = pygame.image.load("logo.jpg")

pygame.mixer.init()
pygame.mixer.music.load('Plugly - Subway scam.mp3')
pygame.mixer.music.play(-1)

class Snake():
    def __init__(self, starting_x, starting_y, starting_length):
        self.color = (0, 255, 0)
        self.dead = False
        self.score = 0
        self.grow = 0

        self.array = [(starting_x - i, starting_y) for i in range(starting_length)]  # the snake body
        self.apple = (random.randint(*board_coordinates), random.randint(*board_coordinates))  # the coordinates of the apple
        self.dir = {"x": -1,
                    "y": 0}
        self.check_apple()
        pygame.display.set_caption(
            f'Snake By Vladislav Taskaev                                                              your score is {self.score}')

    def check_apple(self):
        if self.apple in self.array:
            self.score += 1
            self.grow += 1
            self.apple = (random.randint(*board_coordinates), random.randint(*board_coordinates))
            self.check_apple()

    def move_snake(self):
        new_point = (self.array[-1][0] + self.dir["x"], self.array[-1][1] + self.dir["y"])
        self.dead = self.point_in_body(new_point)
        self.array.append(new_point)
        self.check_apple()
        if self.grow == 0:
            self.array.pop(0)
        else:
            self.grow -= 1
            pygame.display.set_caption(f'Snake By Vladislav Taskaev                                                              your score is {self.score}')

    def am_i_dead(self):
        return self.dead

    def point_in_body(self, point):
        return point[0] < board_coordinates[0] or\
               point[0] > board_coordinates[1] or\
               point[1] < board_coordinates[0] or\
               point[1] > board_coordinates[1] or\
               point in self.array

    def return_score(self):
        return self.score


def draw(screen, snakes):
    pygame.draw.rect(screen, (32, 32, 32), (0, 0, 1000, 1000))
    for snake in snakes:
        for pixel in snake.array:
            pygame.draw.rect(screen, snake.color,
                             ((pixel[0] * pixel_size) + 1, (pixel[1] * pixel_size) + 1, pixel_size - 2, pixel_size - 2))
        pygame.draw.rect(screen, [255, 0, 0], (
        (snake.apple[0] * pixel_size) + 1, (snake.apple[1] * pixel_size) + 1, pixel_size - 2, pixel_size - 2))


def draw(screen, snakes):
    pygame.draw.rect(screen, (32, 32, 32), (0, 0, 1000, 1000))
    for snake in snakes:
        for pixel in snake.array:
            pygame.draw.rect(screen, snake.color,
                             ((pixel[0] * pixel_size) + 1, (pixel[1] * pixel_size) + 1, pixel_size - 2, pixel_size - 2))
        pygame.draw.rect(screen, [255, 0, 0], (
        (snake.apple[0] * pixel_size) + 1, (snake.apple[1] * pixel_size) + 1, pixel_size - 2, pixel_size - 2))


def start_the_game():
    snakes = [Snake(random.randint(4, 46), random.randint(4, 44), 3)]

    while True:
        draw(screen, snakes)
        snakes[0].move_snake()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    snakes[0].dir = {
                        "x": 0,
                        "y": -1
                    }
                if event.key == pygame.K_DOWN:
                    snakes[0].dir = {
                        "x": 0,
                        "y": 1
                    }
                if event.key == pygame.K_LEFT:
                    snakes[0].dir = {
                        "x": -1,
                        "y": 0
                    }
                if event.key == pygame.K_RIGHT:
                    snakes[0].dir = {
                        "x": 1,
                        "y": 0
                    }
        pygame.display.update()

        if snakes[0].am_i_dead():
            # snakes = [Snake(random.randint(4, 46), random.randint(4, 44), 3)]
            break

        clock.tick(20)


def main():
    start_the_game()



main_theme = pygame_menu.themes.THEME_DEFAULT.copy()
main_theme.set_background_color_opacity(0.4)
menu = pygame_menu.Menu('Here we go again', 500, 250, position = (50, 75),theme = main_theme)

menu.add.text_input('Name :', default='Player 1')
menu.add.button('Start the game', start_the_game)
menu.add.button('Exit', pygame_menu.events.EXIT)

menu.center_content()

while True:

    screen.blit(bd_image, (0,0))
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            exit()

    if menu.is_enabled():
        menu.update(events)
        menu.draw(screen)

    pygame.display.update()

if __name__ == "__main__":
    main()