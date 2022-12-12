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

        self.amount = 3

        self.haswon = False

    def main_GamePlay(self,screen):
        for i in range(4):
            if self.cat[i].column == 10 and self.cat[i].row == 10:
                self.haswon = True
        #draw
        screen.blit(self.bg_size, (0,0))
        move(self.cat,self.amount,screen)
        pygame.display.update()