import pygame
import time
import random
pygame.init()
white = (255, 255, 255)
red = (255, 0, 0)
game_window = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Flappy Bird")

icon = pygame.image.load('icon.jpg')
pygame.display.set_icon(icon)
fps = 60
clock = pygame.time.Clock()



def screen_draw(file, height, width, pos_x, pos_y):
    a = pygame.image.load(file)
    a = pygame.transform.scale(a, (height, width))
    game_window.blit(a, (pos_x, pos_y))


def gameloop():
    game_over = True
    initial = time.time()
    game_end = True
    bird_y = 200
    speed = 0
    ground_x = 0
    accelaration = 0
    bar_list =[]
    pillar_x = 430

    while game_over:
        current_time = time.time()
        game_window.fill(white)
        screen_draw('grond.png', 500, 400, ground_x, 0)
        if ground_x < 0:
            screen_draw('grond.png', 500, 400, 500+ground_x, 0)
        if ground_x == -500:
            ground_x = 0
        screen_draw('ground 2.png', 500, 100, ground_x, 400)
        if ground_x < 0:
            screen_draw('ground 2.png', 500, 100, 500+ground_x, 400)
        if ground_x == -500:
            ground_x = 0
        screen_draw('flapy 1.png', 50, 50, 100, bird_y)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    speed = -8
                    accelaration = 0.8
        bird_y += speed
        speed += accelaration
        ground_x -= 5
        if (current_time - initial) > 3.5:
            a = random.randint(100, 200)
            #screen_draw('pilar up.png', 70, a, 430, 400-a)
            initial = time.time()
            bar_list.append([a, 430])
        else:
            r = 0
            for i, j in bar_list:
                screen_draw('pilar up.png', 70, i, j, 400-i)
                screen_draw('pillar down.png', 70, 300-i, j, 0)
                bar_list[r][1] -= 5
                if j < -70:
                    del bar_list[r]
                r += 1
        pygame.display.update()
        clock.tick(fps)
gameloop()
pygame.quit()
quit()