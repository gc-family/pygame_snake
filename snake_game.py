from snake_queue import Queue
import pygame
from pygame.locals import *
from snake_settings import *
import time

pygame.init()

times = pygame.time.Clock()


class Graphics(object):
    def __init__(self):
        self.sc = pygame.display.set_mode((win_WIDTH, win_HEIGHT))

    def drawborder(self):
        rectangele = pygame.draw.rect(self.sc, (255, 255, 255), [LEFTX,LEFTY, WIDTH, HEIGHT],5)

    def close_apps(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                False
                exit()

    def draw_snake(self, iterable):
        """this will receive coordinate iterable ..."""
        for point in iterable:
            # pygame.draw.circle(self.sc, COLOR[2], point, fruit_radius)
            pygame.draw.rect(self.sc, COLOR[2], [point[0], point[1], fruit_radius, fruit_radius], 2)


class Snake(Queue):
    def __init__(self):
        super(Snake, self).__init__()
        self.snake = self.queue
        self.change = fruit_radius - 1
        self.direction = 'east'
        self.speed = [self.change, 0]
        self.score = 0
        # initialize the snake
        self.initialize()

    def initialize(self):
        self.add_multiple(initial_snake_length)

    def change_direction(self):
        keys = pygame.key.get_pressed()
        if keys[K_UP]:
            if self.direction != 'south':
                self.speed = [0, -self.change]
                self.direction = 'north'
        if keys[K_DOWN]:
            if self.direction != 'north':
                self.speed = [0, self.change]
                self.direction = 'south'
        if keys[K_LEFT]:
            if self.direction != 'east':
                self.speed = [-self.change, 0]
                self.direction = 'west'
        if keys[K_RIGHT]:
            if self.direction != 'west':
                self.speed = [self.change, 0]
                self.direction = 'east'

    def move(self):
        self.enqueue(self.summation(self.speed))
        self.dequeue()

    def eat(self):
        self.add_tail(self.summation_end(self.speed))


class Fruit(object):
    def __init__(self):
        self.pos = [WIDTH // 2, HEIGHT // 3]
        self.radius = 5

    def move(self):
        pass


if __name__ == "__main__":
    graph = Graphics()
    snake_animal = Snake()
    fruit = Fruit()
    while True:
        graph.close_apps()
        graph.sc.fill(COLOR[0])
        graph.drawborder()
        # creation of new snake
        if snake_animal.get_heading()[0] >= WIDTH+LEFTX and snake_animal.direction == 'east':
            snake_animal.eat()
            snake_animal.get_heading()[0] = 0
            print(snake_animal.direction)

        if snake_animal.get_heading()[0] <= -5 and snake_animal.direction == 'west':
            snake_animal.eat()
            snake_animal.get_heading()[0] = WIDTH
            print(snake_animal.direction)

        if snake_animal.get_heading()[1] >= HEIGHT and snake_animal.direction == 'south':
            snake_animal.eat()
            snake_animal.get_heading()[1] = 0
            print(snake_animal.direction)

        if snake_animal.get_heading()[1] <= -5 and snake_animal.direction == 'north':
            snake_animal.eat()
            snake_animal.get_heading()[1] = HEIGHT
            print(snake_animal.direction)

        snake_animal.change_direction()
        snake_animal.move()
        graph.draw_snake(snake_animal.snake)
        times.tick(15)
        pygame.display.update()
