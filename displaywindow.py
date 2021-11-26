import sys,pygame

#dimensions of display window, background grid
window_size = window_width, window_height = 1000,1000
#colors for various elements
window_color = (50,50,50)
grid_color = (20,20,20)
cell_color = (230,230,230)

from cell_logic import *

def game():
    global window,window_copy

    pygame.init() 
    
    window = pygame.display.set_mode(window_size)
    window.fill(window_color)
    window_rect = window.get_rect() #getting rect(x,y,w,h) cords of the display surface

    window_copy = window.copy()
    window_copy.set_colorkey((0,0,0))
   
    add_cells = "y"

    while True:
        #checks for various events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    pygame.draw.rect(window,cell_color,rect)

        drawGrid() #draws a grid of squares of side 20

        pygame.display.flip() #updates the display
        
def drawGrid():
    global boxsize
    boxsize = 40
    for x in range(window_width//boxsize):
        for y in range(window_height//boxsize):
            rect = pygame.Rect(x*boxsize,y*boxsize,boxsize,boxsize)
            pygame.draw.rect(window,grid_color,rect,3)


    
    



      




