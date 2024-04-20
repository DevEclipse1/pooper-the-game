import pygame
from pygame.locals import *
import math
import random
import time
import os

title = "Pooper"

def tileBackground(screen: pygame.display, image: pygame.Surface) -> None:
    screenWidth, screenHeight = screen.get_size()
    imageWidth, imageHeight = image.get_size()
    
    tilesX = math.ceil(screenWidth / imageWidth)
    tilesY = math.ceil(screenHeight / imageHeight)
    
    for x in range(tilesX):
        for y in range(tilesY):
            screen.blit(image, (x * imageWidth, y * imageHeight))

def main():
    global title

    pygame.init()

    screen = pygame.display.set_mode((600,600))
    pygame.display.set_caption(title)

    clock = pygame.time.Clock()

    background = pygame.image.load("sky.png")
    basket = pygame.image.load("basket.png")
    shit = pygame.image.load("shit.png")

    score = 0

    font = pygame.font.Font("arial.ttf",20)
    text = font.render(str(score), True, (255, 255, 255), (0, 0, 0, 0))

    basketX = 200

    shits = []

    lastSpawnTime = 0

    lastSpawnTime = time.time()

    spawnDelay = 2
    gravity = 5

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    if basketX <= 500:
                        basketX += 50
                if event.key == pygame.K_a:
                    if basketX >= 50:
                        basketX -= 50
            
        tileBackground(screen,background)
        pygame.draw.rect(screen, "forestgreen", pygame.Rect(0, 500, 600, 100))

        screen.blit(basket, (basketX, 468))

        for shit_rect in shits[:]:
            if shit_rect.colliderect(pygame.Rect(basketX, 468, 64, 32)):
                shits.remove(shit_rect)
                score += 1
            else:
                shit_rect.y += gravity
                screen.blit(shit, shit_rect)

        text = font.render(str(score), True, (255, 255, 255), (0, 0, 0, 0))

        if time.time() - lastSpawnTime > spawnDelay:
            new_shit_rect = shit.get_rect(x=random.randint(0, 468), y=0)
            shits.append(new_shit_rect)
            lastSpawnTime = time.time()

        for shit_rect in shits[:]:
            if shit_rect.y > 500:
                os.system(f'msg "%username%" your final score was {score}')
                exit()
        
        for shit_rect in shits:
            shit_rect.y += gravity
            screen.blit(shit, shit_rect)

        screen.blit(text, (10, 10))

        pygame.display.update()
        clock.tick(60)

if __name__ == "__main__":
    main()
