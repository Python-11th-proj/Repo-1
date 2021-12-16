import sys,pygame,time,random

window_size = window_width, window_height = 1800,900 #dimensions of display window

#colors for various elements
window_color = (50,50,50)
grid_color = (20,20,20)
cell_color = (230,230,230)

cells_added = [] #list to track added cells

from cell_logic import *


def drawGrid(): #draws the grid and saves all the rects to grid_rect
    for x in range(window_width//boxsize):
        for y in range(window_height//boxsize):
            rect = pygame.Rect(x*boxsize,y*boxsize,boxsize,boxsize)
            pygame.draw.rect(window,window_color,rect)
            pygame.draw.rect(window,grid_color,rect,1)

  
def cursor_hover():
    global rect
    mouse_x,mouse_y = pygame.mouse.get_pos()
    #gets the co-ordinate of the top left corner of the nearest square based on mouse position
    nearest_x = (mouse_x//boxsize)*boxsize
    nearest_y = (mouse_y//boxsize)*boxsize
    rect = pygame.Rect(nearest_x,nearest_y,boxsize,boxsize)
    drawGrid()
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
    boxsize = 10 #size of the cells in the grid

    font = pygame.font.SysFont("Arial", 18) #font for the fps counter

    drawGrid() #draws the grid

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
                    #redraws the last cell after mouse hover is stopped
                    pygame.draw.rect(window,window_color,rect)
                    pygame.draw.rect(window,grid_color,rect,1)

                    #starts the simulation
                    while phase1:
                        clock.tick(150)
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                pygame.quit()
                                sys.exit()
                        cell_changes(cells_added,boxsize,window_copy,cell_color,window_color,window)
                        window.blit(window_copy,window_rect) #displays window_copy on the display window
                        window.blit(update_fps(font),(10,0)) #displays the fps
                        pygame.display.flip() #updates the display
                        #time.sleep(0.3)

                if event.key == pygame.K_BACKSLASH:
                    # defining snake default position
                    snake_position = [150, 90]
 
                    # defining first 4 blocks of snake body
                    snake_body = [  [150, 90],
                                    [120, 90],
                                    [90, 90],
                                    [60, 90]
                                   ]
                    # fruit position
                    fruit_position = [random.randrange(0, (1800//boxsize)) * 30,random.randrange(0, (800//boxsize)) * boxsize]
                    fruit_spawn = True
 
                    # setting default snake direction right
                    direction = 'RIGHT'
                    change_to = direction

                    # initial score
                    score = 0

                    def show_score(choice, color, font, size,window):
                        # creating font object score_font
                        score_font = pygame.font.SysFont(font, size)
                        # create the display surface object
                        score_surface = score_font.render('Score : ' + str(score), True, color)
                        # create a rectangular object for the score
                        score_rect = score_surface.get_rect()
                        # displaying text
                        window.blit(score_surface, score_rect)

                    def game_over(window):
                        # creating font object my_font
                        my_font = pygame.font.SysFont('times new roman', 50)
                        # creating a text surface
                        game_over_surface = my_font.render('Your Score is : ' + str(score), True, (255,0,0))
                        game_over_rect = game_over_surface.get_rect()
                        # setting position of the text
                        game_over_rect.midtop = (window_width/2, window_height/4)
                        window.blit(game_over_surface, game_over_rect)
                        pygame.display.flip()
                        time.sleep(2)
                        pygame.quit()
                        quit()

                    while phase1:
                        clock.tick(150)
                        for event in pygame.event.get():
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_UP:
                                    change_to = 'UP'
                                if event.key == pygame.K_DOWN:
                                    change_to = 'DOWN'
                                if event.key == pygame.K_LEFT:
                                    change_to = 'LEFT'
                                if event.key == pygame.K_RIGHT:
                                    change_to = 'RIGHT'
 
                                if change_to == 'UP' and direction != 'DOWN':
                                    direction = 'UP'
                                if change_to == 'DOWN' and direction != 'UP':
                                    direction = 'DOWN'
                                if change_to == 'LEFT' and direction != 'RIGHT':
                                    direction = 'LEFT'
                                if change_to == 'RIGHT' and direction != 'LEFT':
                                    direction = 'RIGHT'
 
                        # Moving the snake
                        if direction == 'UP':
                            snake_position[1] -= boxsize
                        if direction == 'DOWN':
                            snake_position[1] += boxsize
                        if direction == 'LEFT':
                            snake_position[0] -= boxsize
                        if direction == 'RIGHT':
                            snake_position[0] += boxsize
 
                        # Snake body growing mechanism
                        snake_body.insert(0, list(snake_position))
                        if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
                            score += 10
                            fruit_spawn = False
                        else:
                            snake_body.pop()
         
                        if not fruit_spawn:
                            fruit_position = [random.randrange(1, (window_width//boxsize)) * boxsize,random.randrange(1, (window_height//boxsize)) * boxsize]
         
                        fruit_spawn = True
                        window.fill(window_color)
     
                        for pos in snake_body:
                            pygame.draw.rect(window,(0,255,0), pygame.Rect(pos[0], pos[1], boxsize, boxsize))
         
                        pygame.draw.rect(window,(255,0,0), pygame.Rect(fruit_position[0], fruit_position[1], boxsize, boxsize))
 
                        # Game Over conditions
                        if snake_position[0] < 0 or snake_position[0] > window_width-boxsize:
                            game_over(window)
                        if snake_position[1] < 0 or snake_position[1] > window_height-boxsize:
                            game_over(window)
     
                        # Touching the snake body
                        for block in snake_body[1:]:
                            if snake_position[0] == block[0] and snake_position[1] == block[1]:
                                game_over(window)
     
                        # displaying score countinuously
                        show_score(1, (255,255,255), 'times new roman', 20,window)
     
                        # Refresh game screen
                        pygame.display.update()
                        time.sleep(0.1)
                    
        window.blit(window_copy,window_rect) #displays window_copy on the display window
        window.blit(update_fps(font),(10,0)) #displays the fps
        pygame.display.flip() #updates the display
     

    

    
    



      




