# ----- Imports -----
from cell import Cell
import copy
from random import choice
# -------------------

class Grid:
    '''This Class is responsible for holding the current state of the "wave" or, in our case: the image'''
    def __init__(self, width, height, resolution, options):
        self.width      = width
        self.height     = height
        self.w_const    = self.width  //  resolution
        self.h_const    = self.height //  resolution
        self.resolution = resolution
        self.grid       = []
        self.options    = options

    def initiateCells(self):
        '''Creates a 2D array of cells'''
        for i in range(self.w_const):
            self.grid.append([])
            for j in range(self.h_const):
                cell = Cell(i, j, self.resolution, self.options)
                self.grid[i].append(cell)

    def drawGrid(self, window):
        '''Draws every single cell in the grid'''
        for row in self.grid:
            for cell in row:
                cell.drawCell(window)

    def heuristicPick(self):
        '''Picks the cell with the lowest entropy
        This function runs in every tick of the application, chosing one cell to be collapsed.'''

        # Empty Grid
        gridCopy = [i for row in self.grid for i in row]
        gridCopy.sort(key=lambda x: x.getCellEntropy())
        
        # Grid Filtering
        filteredGrid = list(filter(lambda x: x.getCellEntropy() > 1, gridCopy))
        if filteredGrid == []:
            return None

        # Picking the least entropic cell
        leastEntropyCell = filteredGrid[0]
        filteredGrid = list(filter(lambda x:x.getCellEntropy()==leastEntropyCell.getCellEntropy(),filteredGrid))

        # Returning a Pick if filteredGrid is not empty
        pick = choice(filteredGrid)
        return pick

    def collapse(self):
        '''The collapse function - in other words - the algorithm.
        It first choses a random picked cell, then collapses based on the least entropic cell'''

        # Picking a cell
        pick = self.heuristicPick()
        if pick:
            self.grid[pick.xpos][pick.ypos].options
            self.grid[pick.xpos][pick.ypos].observeCell()
        else:
            return

        # Empty copy of the Grid:
        nextGrid = copy.copy(self.grid)

        # Update the entropy values:
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                if self.grid[i][j].collapsed:
                    nextGrid[i][j] = self.grid[i][j]
                
                else:
                    # Stores the valid options from up/right/bottom/left for each cell in the grid
                    cumulativeValidOptions = self.options

                    # Checks above cell 
                    cellAbove = self.grid[(i-1)%self.w_const][j]
                    validOptions = []
                    for option in cellAbove.options:
                        validOptions.extend(option.down)
                    cumulativeValidOptions = [option for option in cumulativeValidOptions if option in validOptions]
                    
                    # Checks right cell
                    cellRight = self.grid[i][(j+1)%self.h_const]
                    validOptions = []
                    for option in cellRight.options:
                        validOptions.extend(option.left)
                    cumulativeValidOptions = [option for option in cumulativeValidOptions if option in validOptions]

                    # Checks bottom cell
                    cellBelow = self.grid[(i+1)%self.w_const][j]
                    validOptions = []
                    for option in cellBelow.options:
                        validOptions.extend(option.up)
                    cumulativeValidOptions = [option for option in cumulativeValidOptions if option in validOptions]

                    # Checks left cell
                    cellLeft = self.grid[i][(j-1)%self.h_const]
                    validOptions = []
                    for option in cellLeft.options:
                        validOptions.extend(option.right)
                    cumulativeValidOptions = [option for option in cumulativeValidOptions if option in validOptions]

                    # Assign the cumulativeValidOptions to be the current cell's valid options
                    nextGrid[i][j].options = cumulativeValidOptions
                    nextGrid[i][j].updateCell()

        # Re-assign the grid
        self.grid = copy.copy(nextGrid)
