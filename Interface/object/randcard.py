import pygame
import random

back3_path = 'Art/Card_Back3.png'
back5_path = 'Art/Card_Back5.png'
forward3_path = 'Art/Card_Forward3.png'
forward5_path = 'Art/Card_Forward5.png'
start_path = 'Art/Card_Start.png'
stop_path = 'Art/Card_Stop.png'

class Card(object):
    def __init__(self):
        self.back3 = pygame.image.load(back3_path)
        self.back5 = pygame.image.load(back5_path)
        self.forward3 = pygame.image.load(forward5_path)
        self.forward5 = pygame.image.load(forward5_path)
        self.start = pygame.image.load(start_path)
        self.stop = pygame.image.load(stop_path)

        self.chanelcard = {
            'ch10' : [1,10],
            'ch15' : [2,5],
            'ch20' : [2,10],
            'ch29' : [3,9],
            'ch37' : [4,7],
            'ch52' : [6,2],
            'ch56' : [6,6],
            'ch61' : [7,1],
            'ch71' : [8,1],
            'ch77' : [8,7],
            'ch86' : [9,6],
            'ch93' : [10,3],
            'ch98' : [10,8]
        }

        self.row_card = 1
        self.column_card = 1

    def show(self,row,column,screen):
        self.row_card = row
        self.column_card = column
        for x in self.chanelcard:
            if self.chanelcard[x][0] == row and self.chanelcard[x][1] == column:
                print("random card")