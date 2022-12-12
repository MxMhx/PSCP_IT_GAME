import pygame

from object.move import move
from object.cat import Cat

class GamePlay():
    def __init__(self):
        self.bg_image = pygame.image.load('Art/Ladders_Finish.png')
        self.bg_size = pygame.transform.scale(self.bg_image, (700,700))

        self.cat = []
        self.cat.append(Cat(1))
        self.cat.append(Cat(2))
        self.cat.append(Cat(3))
        self.cat.append(Cat(4))

        self.amount = 4

    def main_GamePlay(self,screen):
        #draw
        screen.blit(self.bg_size, (0,0))
        move(self.cat,self.amount,screen)
        pygame.display.update()