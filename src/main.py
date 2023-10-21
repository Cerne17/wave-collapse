# ----- Imports -----
import pygame
from tile import Tile
from grid import Grid
# -------------------

# ------- Environment Variables -------
WIDTH              = 600
HEIGHT             = 600
RESOLUTION         = 30
TOTAL_IMAGE_NUMBER = 5
FPS                = 120

pygame.init()
font = pygame.font.SysFont('Arial', 16)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Wave Function Collapse")
clock = pygame.time.Clock()
# -------------------------------------

# ------- Image Loading Function -------
def loadImage(path, resolution, padding=0):
    image = pygame.image.load(path).convert_alpha()
    image = pygame.transform.scale(image, (resolution-padding, resolution-padding))
    return image
# --------------------------------------

# ------- Display Message Function -------
def displayMessage(message, position):
    text = font.render(str(message), True, (255, 255, 255))
    screen.blit(text, position)
# ----------------------------------------

# ------- Debbuging Function -------
def hover(mousePos, resolution, grid):
    '''
        When mouse is hovering a cell, it will display:
            [ ] cell Entropy
            [ ] cell collapsed bool
            [ ] cell options / tiles options
    '''
    mouseX, mouseY = mousePos
    xPos = mouseX // resolution
    yPos = mouseY // resolution

    cell = grid.grid[yPos][xPos]

    # Informations:
    cellEntropy = cell.getCellEntropy()
    cellCollapsed = cell.collapsed
    cellOptions = [option.edges for option in cell.options]

    # Hover Box:
    pygame.draw.rect(screen, (20, 20, 20), (mouseX, mouseY, 200, 100))

    # Hover Text/Informations:
    displayMessage(f"Entropy      : {cellEntropy}", (mouseX+10, mouseY+10))
    displayMessage(f"Collapsed    : {cellCollapsed}", (mouseX+10, mouseY+30))
    displayMessage(f"Cell Options : {cellOptions}", (mouseX+10, mouseY+50))
# ----------------------------------

def main():

    # ------- Loading Images -------
    options = []

    for i in range(TOTAL_IMAGE_NUMBER):

        # Loading Images
        image = loadImage(f".././img/{i}.png", RESOLUTION)

        options.append(Tile(image))

    # ------------------------------

    # ------- Edges Configurations -------
    
    options[0].edges = [1,1,0,0]
    options[1].edges = [1,1,1,1]
    options[2].edges = [0,0,0,0]
    options[3].edges = [0,1,0,1]
    options[4].edges = [0,1,1,1]

    # Updating tile Rules
    for i, tile in enumerate(options):
        tile.index = i
        tile.setRules(options)

    # ------------------------------------

    # ------- Grid -------

    wave = Grid(WIDTH, HEIGHT, RESOLUTION, options)
    wave.initiateCells()

    # --------------------

    # Toggles Debug Mode
    debugMode = False
    

    # ------------- Game Loop -------------
    running = True
    while running:
        # Screen Background
        screen.fill((200, 0, 240))
        
        # ------ Events Cheking ------

        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                
                if event.key == pygame.K_ESCAPE:
                    running = False
                    exit()

                if event.key == pygame.K_d:
                    debugMode = not debugMode

                if event.key == pygame.K_q:
                    running = False
                    exit()
            # ------------------------

        wave.drawGrid(screen)

        wave.collapse()

        if debugMode:
            mousePosition = pygame.mouse.get_pos()
            hover(mousePosition, RESOLUTION, wave)

        # Screen Update
        pygame.display.update()

        # MAX FPS
        clock.tick(FPS)


if __name__ == "__main__":
    main()
