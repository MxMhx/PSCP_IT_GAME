import pygame
from state.state import State
from object.cat import Cat

bg_image = pygame.image.load('fern_game/assets/ladders.png')
bg_size = pygame.transform.scale(bg_image, (700, 700))

class GamePlay():
    def __init__(self):
        self.cat = []
        self.cat.append(Cat())
        self.cat.append(Cat())
    def main_game(self,screen):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        self.cat[0].move()
        self.cat[1].move()

        #Draw
        screen.fill(255,255,255)
        screen.blit(bg_size, (0, 0))
        self.cat[0].draw(screen)
        self.cat[1].draw(screen)
        pygame.display.update()