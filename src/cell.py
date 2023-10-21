# ----- Imports -----
import pygame
from random import choice

pygame.init()
font = pygame.font.SysFont('Arial', 20)
# -------------------
class Cell:
    '''Represets every single "pixel" in the final image'''
    def __init__(self, xpos, ypos, resolution, options):
        self.xpos        = xpos
        self.ypos        = ypos
        self.resolution  = resolution
        self.options     = options
        self.collapsed   = False

    def drawCell(self, window):
        if len(self.options) == 1:
            self.options[0].drawTile(
                window, 
                self.ypos * self.resolution, 
                self.xpos * self.resolution
           )

    def getCellEntropy(self):
        '''Counts how many possible options there are for this cell'''
        return len(self.options)

    def updateCell(self):
        '''Essentially, used to update the cell's collapsed property'''
        self.collapsed = bool(len(self.options) == 1)

    def observeCell(self):
        '''Used to select any of the possible states of the cell (Mandatory for the WFC algo)'''
        try:
            self.options = [choice(self.options)]
            self.collapsed = True
        except:
            return


