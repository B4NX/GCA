import pygame, sys, random, CA

SCREEN_WIDTH  = 600
SCREEN_HEIGHT = 600

color_background = (255, 255, 255)
color_finder = (255, 0, 0)
color_trail = (192, 128, 128)
color_wall = (0, 0, 0)
color_grid = (90, 90, 90)

GRID_WIDTH = 40
GRID_HEIGHT = 40

CELL_WIDTH = int(SCREEN_WIDTH / GRID_WIDTH)
CELL_HEIGHT = int(SCREEN_HEIGHT / GRID_HEIGHT)

UP = (0, (0, -1))
LEFT = (-90, (-1, 0))
DOWN = (180, (0, 1))
RIGHT = (90, (1, 0))
nextTurn = {UP:LEFT, LEFT:DOWN, DOWN:RIGHT, RIGHT:UP}

FinderHeadPosition = (0, 0)
FinderHeadDirection = UP
FinderTrail = [FinderHeadPosition,]

finderIcon = pygame.image.load("finderarrow.png")
finderIcon = pygame.transform.scale(finderIcon, (CELL_WIDTH, CELL_HEIGHT))

controlIndex = 567 #Evolve with GA?

#returns True if success, False if failure (out of bounds or hit a wall)
def MoveFinder():
    global FinderHeadPosition
    c = zip( FinderHeadPosition, FinderHeadDirection[1]) 
    newPos = [ sum( x ) for x in c ]
    if (newPos[0] < 0 or newPos[0] > GRID_WIDTH):
        return False
    if (newPos[1] < 0 or newPos[1] > GRID_HEIGHT):
        return False
    FinderTrail.append(FinderHeadPosition)
    FinderHeadPosition = newPos
    return True

def TurnFinder():
    global FinderHeadDirection
    FinderHeadDirection = nextTurn[FinderHeadDirection]

def drawGrid():
    global mainSurface
    for x in range(GRID_WIDTH - 1):
        mainSurface.fill(color_grid, ((x + 1) * CELL_WIDTH, 0, 1, SCREEN_HEIGHT))
    for y in range(GRID_HEIGHT - 1):
        mainSurface.fill(color_grid, (0, (y + 1) * CELL_HEIGHT, SCREEN_WIDTH, 1))

def drawFinderTrail():
    global mainSurface
    lastPos = FinderTrail[-1]
    mainSurface.fill(color_trail, (lastPos[0] * CELL_WIDTH, lastPos[1] * CELL_HEIGHT, CELL_WIDTH, CELL_HEIGHT))

def drawFinder():
    global mainSurface
    #mainSurface.fill(color_finder, (FinderHeadPosition[0] * CELL_WIDTH, FinderHeadPosition[1] * CELL_HEIGHT, CELL_WIDTH, CELL_HEIGHT))
    mainSurface.blit(pygame.transform.rotate(finderIcon, FinderHeadDirection[0]), (FinderHeadPosition[0] * CELL_WIDTH, FinderHeadPosition[1] * CELL_HEIGHT))

#Replace with input from CA
def update():
    CA.update_rows()
    row = CA.getLastRow()
    if (row[controlIndex] == 0):
        MoveFinder()
    else:
        TurnFinder()

def init():
    global mainSurface
    pygame.init()
    mainSurface = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    pygame.display.set_caption("Pathfing")
    mainSurface.fill(color_background)
    drawGrid()

    CA.initCA()

def main():
    while 1:
            for event in pygame.event.get():
                    if event.type==pygame.QUIT:
                            pygame.quit()
                            sys.exit()
                    if event.type==pygame.KEYDOWN:
                            pygame.quit()
                            sys.exit()
            update()
            drawFinderTrail()
            drawFinder()
            pygame.display.flip()

init()
main()