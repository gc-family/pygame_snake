from pprint import pprint

# color settings
COLOR = [[i * 255, j * 255, k * 255] for i in range(2) for j in range(2) for k in range(2)]
# display settings
WIDTH = 640
win_WIDTH = 700
LEFTY = int((win_WIDTH-WIDTH)//2)
HALF_WIDTH = WIDTH // 2
HEIGHT = 480

win_HEIGHT = 560
LEFTX = int((win_HEIGHT - HEIGHT)//2)
HALF_HEIGHT = HEIGHT // 2

# fruit settings
fruit_pos = [HALF_WIDTH, HALF_HEIGHT]
fruit_color = COLOR[1]
fruit_radius = 20

# snake settings
snake_max = 500
total = 5*fruit_radius
initial_snake_length = [[HALF_WIDTH - difference, HALF_HEIGHT] for difference in range(total, -fruit_radius, - fruit_radius)]
print(initial_snake_length)
# initial_snake_length = [[HALF_WIDTH - difference, HALF_HEIGHT] for difference in range(100, -10, -10)]


snake_direction = 'east'
# score settings
score = 0

