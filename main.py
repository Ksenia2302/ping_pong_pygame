import pygame
import random
import time

pygame.init()
width = 800
height = 600
cell_size = 20
white = (255, 255, 255)
#         r    g    b
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)


screen =pygame.display.set_mode((width, height))
font = pygame.font.SysFont('Verdana', 35)
clock = pygame.time.Clock()


def message(msg, color, x, y):
    text = font.render(msg, True, color)
    screen.blit(text, [x, y])

def game_loop():
    snake_pos = [100, 50]
    snake_body = [[100, 50], [90, 50], [80, 50]]
    direction = 'RIGHT'
    change_to = direction
    speed = 10

    food_pos = [random.randint(1, (width//cell_size)) * cell_size, random.randint(1, (height//cell_size)) * cell_size]
    food_spawn = True

    score = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                #break
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direction != 'DOWN':
                    change_to = 'UP'
                if event.key == pygame.K_DOWN and direction != 'UP':
                    change_to = 'DOWN'
                if event.key == pygame.K_LEFT and direction != 'RIGHT':
                    change_to = 'LEFT'
                if event.key == pygame.K_RIGHT and direction != 'LEFT':
                    change_to = 'RIGHT'

        direction = change_to
        if direction == 'UP':
            snake_pos[1] -= cell_size
        if direction == 'DOWN':
            snake_pos[1] += cell_size
        if direction == 'RIGHT':
            snake_pos[0] += cell_size
        if direction == 'LEFT':
            snake_pos[0] -= cell_size

        snake_body.insert(0, list(snake_pos))

        if abs(snake_pos[0] - food_pos[0]) < 50 and abs(snake_pos[1]  - food_pos[1]) < 50:
            food_spawn = False
            score += 10
        else:
            snake_body.pop()

        if not  food_spawn:
            food_pos = [random.randint(1, (width // cell_size)) * cell_size,
                        random.randint(1, (height // cell_size)) * cell_size]

        food_spawn = True
        if snake_pos[0] >= width or snake_pos[0] < 0 or snake_pos[1] >= height or snake_pos[1] < 0:
            message('Игра окончена', red, width // 4, height // 3)
            pygame.display.update()
            time.sleep(2)
            game_loop()

        for block in snake_body[1:]:
            if snake_pos[0] == block[0] and snake_pos[1] == block[1]:
                message('Игра окончена', red, width // 4, height // 3)
                pygame.display.update()
                time.sleep(2)
                game_loop()

        screen.fill(black)
        for pos in snake_body:
            pygame.draw.rect(screen, green, pygame.Rect(pos[0], pos[1], cell_size, cell_size))
        pygame.draw.rect(screen, red, pygame.Rect(food_pos[0], food_pos[1], cell_size, cell_size))

        message(f'Счет {score}', green, 10, 10)

        pygame.display.update()
        clock.tick(speed)

game_loop()

#пинг-понг

