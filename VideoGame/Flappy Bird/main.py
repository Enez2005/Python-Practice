import pygame
import os
import random


WIDTH, HEIGHT = 800, 450

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Not Flappy Bird but almost it")



WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)

FPS = 144
HEIGHT_METER = HEIGHT // 18
WIDTH_METER = WIDTH // 32



TEST = pygame.Rect(WIDTH // 2 - WIDTH_METER // 2, HEIGHT // 2 - HEIGHT_METER // 2, WIDTH_METER, HEIGHT_METER)

floor = pygame.Rect(0, HEIGHT - (2 * HEIGHT_METER), WIDTH, 2 * HEIGHT_METER)
BIRD_WIDHT , BIRD_HEIGHT = WIDTH_METER * 2 , HEIGHT_METER
BIRD_SCALE = pygame.Rect(WIDTH // 2 - WIDTH_METER // 2, HEIGHT // 2 - HEIGHT_METER // 2, BIRD_WIDHT, BIRD_HEIGHT)


increment_interval = 1
last_increment_time = pygame.time.get_ticks()


def gravity(VEL, bird):
    if bird.y + VEL + bird.height <= floor.y and VEL < 0.125 *HEIGHT_METER:
        VEL += 0.0027 * HEIGHT_METER
 
        return VEL
    

    return VEL

def handle_bird(bird, VEL):
    
    if bird.y + bird.height <= floor.y:
        bird.y += VEL

def draw_window(bird):
    WIN.fill(WHITE)
    pygame.draw.rect(WIN, BLACK, bird)

    pygame.draw.rect(WIN, GREEN, floor)
    
    pygame.display.update()
  

def main():

    last_increment_time = pygame.time.get_ticks()

    VEL = 0

    bird = pygame.Rect(WIDTH_METER, (HEIGHT - (2 * WIDTH_METER)) // 2, BIRD_WIDHT, BIRD_HEIGHT)

    clock = pygame.time.Clock()
    run = True


    while run:

        clock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and bird.y + bird.height > 0:
                    VEL = -(0.13 * HEIGHT_METER)

        current_time = pygame.time.get_ticks()

        if current_time - last_increment_time >= increment_interval * 1: # Sirve para poder mantener una cuenta del tiempo en cada instancia
            

            VEL = gravity(VEL, bird)

            last_increment_time = current_time
        


        handle_bird(bird, VEL)
        draw_window(bird)
        
        


    pygame.quit

if __name__ == "__main__":
    main()

