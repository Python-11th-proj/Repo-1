import sys,pygame,time

window_size = window_width, window_height = 1800,900 #dimensions of display window

#colors for various elements
window_color = (50,50,50)
grid_color = (20,20,20)
cell_color = (230,230,230)


cells_added = []
grid_rect = []

from cell_logic import *

def drawGrid(grid_rect):
    for x in range(window_width//boxsize):
        for y in range(window_height//boxsize):
            rect = pygame.Rect(x*boxsize,y*boxsize,boxsize,boxsize)
            pygame.draw.rect(window,window_color,rect)
            pygame.draw.rect(window,grid_color,rect,1)
            if grid_no == 0:
                grid_rect.append(rect)
            else:
                pass
  
def cursor_hover():
    global rect
    mouse_x,mouse_y = pygame.mouse.get_pos()
    #gets the co-ordinate of the top left corner of the nearest square based on mouse position
    nearest_x = (mouse_x//boxsize)*boxsize
    nearest_y = (mouse_y//boxsize)*boxsize
    drawGrid(grid_rect) #draw the grid everytime to remove cursor trail
    rect = pygame.Rect(nearest_x,nearest_y,boxsize,boxsize)
    pygame.draw.rect(window,cell_color,rect)
    
def update_fps(font):
	fps = str(int(clock.get_fps()))
	fps_text = font.render(fps, 1, pygame.Color("coral"))
	return fps_text

def game():
    global window,window_copy,boxsize,clock,game_loop,grid_no

    pygame.init()
    
    clock = pygame.time.Clock() #object to call clock method
    window = pygame.display.set_mode(window_size) #makes the display window
    window.fill(window_color)
    window_rect = window.get_rect() #getting rect(x,y,w,h) cords of the display surface(display window)

    window_copy = window.copy() #makes an identical copy of the display surface 
    window_copy.fill(window_color)
    window_copy.set_colorkey(window_color) #makes the copy window transparent

    add_cells = "y"
    boxsize = 30 #size of the cells in the grid
    font = pygame.font.SysFont("Arial", 18) #font for the fps counter
    grid_no = 0
    drawGrid(grid_rect) #draws the grid
    grid_no = 1

    phase1 = True

    while phase1:
        clock.tick(150) #the fps
        #checks for various events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if add_cells == 'y' or 'yes':
                    #draws a cell on the square at the current mouse position
                    if event.button == 1: #left click
                        pygame.draw.rect(window_copy,cell_color,rect)
                        pygame.draw.rect(window_copy,grid_color,rect,1)
                        cells_added.append(rect)
                    #removes a cell on the square at the current mouse position
                    if event.button == 3: #right click
                        pygame.draw.rect(window_copy,window_color,rect)
                        pygame.draw.rect(window_copy,grid_color,rect,1)
                        cells_added.remove(rect)

            if event.type == pygame.MOUSEMOTION: #called when the mouse is moved
                if add_cells == 'y':
                    cursor_hover()
                else:
                    #redraws the last cell after mouse hover is stopped
                    pygame.draw.rect(window,window_color,rect)
                    pygame.draw.rect(window,grid_color,rect,1)

            if event.type == pygame.KEYDOWN:
                #if the space key is pressed the simulation is started 
                if event.key == pygame.K_SPACE:
                    add_cells = 'n'
                    pygame.draw.rect(window,window_color,rect)
                    pygame.draw.rect(window,grid_color,rect,1)
                    while phase1:
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                pygame.quit()
                                sys.exit()
                        cell_changes(grid_rect,cells_added,boxsize,window_copy,cell_color,window_color,window)
                        window.blit(window_copy,window_rect) #displays window_copy on the display window
                        window.blit(update_fps(font),(10,0)) #displays the fps
                        pygame.display.flip() #updates the display
                        time.sleep(0.1)
                    
        window.blit(window_copy,window_rect) #displays window_copy on the display window
        window.blit(update_fps(font), (10,0)) #displays the fps
        pygame.display.flip() #updates the display
     

    

    
    



      




