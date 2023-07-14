import pygame
import sys

def main():
    pygame.init()
    clock = pygame.time.Clock()
    width, height = 400, 600
    screen = pygame.display.set_mode((width, height))
    bird = pygame.Rect(50, 250, 50, 50)
    background = pygame.image.load("background.png")
    bird_image = pygame.image.load("bird.png")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.blit(background, (0, 0))
        screen.blit(bird_image, bird)
        bird.y += 1

        pygame.display.update()
        clock.tick(60)

if __name__ == "__main__":
    main()
