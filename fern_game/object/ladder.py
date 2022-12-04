import pygame

class Ladder(object):
    def __init__(self):
        self.chanel = {
            #index 0,1 is row and column where cat stand
            #index 2,3 is row and column where cat move to
            #ladders
            'ch4' : [1,4,3,5],
            'ch13' : [2,3,5,6],
            'ch33' : [4,3,5,9],
            'ch42' : [5,2,7,8],
            'ch50' : [5,10,7,9],
            'ch62' : [7,2,9,1],
            'ch74' : [8,4,10,2]
            #snake
        }
        self.row_lad = 1
        self.column_lad = 1
    
    def move(self,row,column):
        self.row_lad = row
        self.column_lad = column
        for x in self.chanel:
            if self.chanel[x][0] == row and self.chanel[x][1] == column:
                self.row_lad = self.chanel[x][2]
                self.column_lad = self.chanel[x][3]