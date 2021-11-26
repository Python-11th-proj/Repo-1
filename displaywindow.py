import sys,pygame

#dimensions of display window, background grid
window_size = window_width, window_height = 1000,1000
grid_size = grid_width, grid_height = 3000,3000
#colors for various elements
window_color = (50,50,50)
grid_color = (20,20,20)
cell_color = (230,230,230)

cells_added = [] #list to track rect value of all added cells

from cell_logic import *

def game():
    global grid,window,yes

    pygame.init() 
    
    window = pygame.display.set_mode(window_size,pygame.SRCALPHA) #making the display surface and making it transparent
    window_rect = window.get_rect() #getting rect(x,y,w,h) cords of the display surface
    grid = pygame.Surface(grid_size) #making grid surface
    grid.fill(window_color)

    drawGrid() #draws a grid of squares of side 20
    zoom_X,zoom_Y,zoom_W,zoom_H = 750,750,500,500 #starting rect value of zoom surface

    add_cells = "y"
    

    while True:
        #checks for various events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if zoom_H >= 1400 or zoom_W >= 1400:
                    zoom_H = 1400
                    zoom_W = 1400
                    print(zoom_X,zoom_Y,zoom_H,zoom_W)
                if event.button == 4:
                    zoom_H -= 12
                    zoom_W -=12
                    print(zoom_X,zoom_Y,zoom_H,zoom_W)
                if event.button == 5:
                    zoom_W += 12
                    zoom_H += 12
                    print(zoom_X,zoom_Y,zoom_H,zoom_W)

            if event.type == pygame.KEYDOWN:
                #bounding limits
                if zoom_Y == 18:
                    zoom_Y = 30
                if zoom_Y == 1554:
                    zoom_Y = 1542
                if zoom_X == 18:
                    zoom_X = 30
                if zoom_X == 1554:
                    zoom_X = 1542
                #movement
                if event.key == pygame.K_w:
                    zoom_Y -= 12
                    print(zoom_X,zoom_Y,zoom_H,zoom_W)
                if event.key == pygame.K_s:
                    zoom_Y += 12
                    print(zoom_X,zoom_Y,zoom_H,zoom_W)
                if event.key == pygame.K_a:
                    zoom_X -= 12
                    print(zoom_X,zoom_Y,zoom_H,zoom_W)
                if event.key == pygame.K_d:
                    zoom_X += 12
                    print(zoom_X,zoom_Y,zoom_H,zoom_W)

        zoom(zoom_X,zoom_Y,zoom_W,zoom_H) #creates zoom subsurface on grid surface
        window.blit(pygame.transform.scale(zoom_grid,window_rect.size),(0,0)) #scales zoom subsurface to window size
        pygame.display.flip() #updates the display
        
        if add_cells == "y":
            drawCells_manual()
            x = input("do you want to continue? y/n:\n")
            if x == "n":
                add_cells = "n"
            else:continue

def zoom(zoom_X,zoom_Y,zoom_W,zoom_H):
    global zoom_grid, zoom_rect
    zoom_rect = pygame.Rect(zoom_X,zoom_Y,zoom_W,zoom_H)
    zoom_grid = pygame.Surface.subsurface(grid,zoom_rect)
    zoom_grid.set_colorkey((0,0,0))
    
def drawGrid():
    global boxsize
    boxsize = 20
    for x in range(grid_width//boxsize):
        for y in range(grid_height//boxsize):
            rect = pygame.Rect(x*boxsize,y*boxsize,boxsize,boxsize)
            pygame.draw.rect(grid,grid_color,rect,1)

def drawCells_manual():
    print("Starting co-ords are 1000,1000")
    cords = input("Enter co-ords x,y(multiples of 20):\n")
    cord_split = cords.split(",")
    cord_x = int(cord_split[0])
    cord_y = int(cord_split[1])
    if cord_x%20!=0 or cord_y%20!=0:
        print("Input co-ords that are multiples of 20 eg 980,1000")
        cord_x=-10
        cord_y=-10
    cell_rect = pygame.Rect((cord_x,cord_y),(20,20))
    pygame.draw.rect(grid,cell_color,cell_rect)
    pygame.draw.rect(grid,grid_color,cell_rect,1)
    cells_added.append(cell_rect)
    print(cells_added)
