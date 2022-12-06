import pygame

WIDTH, HEIGHT =  700, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("cats and Ladders")

WHITE = ((255, 255, 255))
FPS = 60
def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
    pygame.quit()

if __name__ == "__main__":
    main()