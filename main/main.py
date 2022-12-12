import pygame
from state.game_play import GamePlay

WIDTH, HEIGHT =  700, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Cats and Ladders")
FPS = 60

game = GamePlay()
def draw():
    screen.fill(((255, 255, 255)))
    game.main_GamePlay(screen)
    pygame.display.update()

def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        draw()
    pygame.quit()

if __name__ == "__main__":
    main()
