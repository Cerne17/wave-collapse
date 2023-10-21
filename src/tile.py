class Tile:
    '''This class is used to manage every tile in the image, set it\'s properties and rules for joining them to their neighbors. Therefore, it\'s vital to update this if the tileset ever changes.
    This class stores the states of the up/right/bottom/left parts of the individual tiles, this information is used when "collapsing" the waves functions'''
    def __init__(self, image):
        self.image = image
        self.index = -1
        self.edges = []
        self.up    = []
        self.right = []
        self.down  = []
        self.left  = []

    def drawTile(self, window, xpos, ypos):
        '''Responsible for drawing the tiles on the screen'''
        window.blit(self.image, (xpos, ypos))

    def setRules(self, tiles):
        '''Receives a list of tiles and inspects whether the borders of any tiles matches the current tile\'s borders'''
        for tile in tiles:

            # Upper Edge:
            if self.edges[0] == tile.edges[2]:
                self.up.append(tile)

            # Right Edge:
            if self.edges[1] == tile.edges[3]:
                self.right.append(tile)

            # Bottom Edge:
            if self.edges[2] == tile.edges[0]:
                self.down.append(tile)

            # Left Edge:
            if self.edges[3] == tile.edges[1]:
                self.left.append(tile)
