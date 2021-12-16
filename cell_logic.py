import pygame

def border_check(rect,cells_added,boxsize,elem):
    global cells_around,cell_check
    cells_around = 0 #number of cells around currently checked cell
    cell_check = rect[elem] #currently checked cell

    #rect for all surrounding areas of currently checked cell
    cell_check_left = pygame.Rect(cell_check.left-boxsize,cell_check.top,boxsize,boxsize)
    cell_check_right = pygame.Rect(cell_check.left+boxsize,cell_check.top,boxsize,boxsize)
    cell_check_top = pygame.Rect(cell_check.left,cell_check.top-boxsize,boxsize,boxsize)
    cell_check_bottom = pygame.Rect(cell_check.left,cell_check.top+boxsize,boxsize,boxsize)

    cell_check_topLeft = pygame.Rect(cell_check.left-boxsize,cell_check.top-boxsize,boxsize,boxsize)
    cell_check_bottomLeft = pygame.Rect(cell_check.left-boxsize,cell_check.top+boxsize,boxsize,boxsize)
    cell_check_topRight = pygame.Rect(cell_check.left+boxsize,cell_check.top-boxsize,boxsize,boxsize)
    cell_check_bottomRight = pygame.Rect(cell_check.left+boxsize,cell_check.top+boxsize,boxsize,boxsize)

    #if surrounding rects in cells_added increase cells_around by 1
    if cell_check_left in cells_added:
        cells_around += 1
    if cell_check_right in cells_added:
        cells_around += 1
    if cell_check_top in cells_added:
        cells_around += 1
    if cell_check_bottom in cells_added:
        cells_around += 1
    if cell_check_topLeft in cells_added:
        cells_around += 1
    if cell_check_topRight in cells_added:
        cells_around += 1
    if cell_check_bottomLeft in cells_added:
        cells_around += 1
    if cell_check_bottomRight in cells_added:
        cells_around += 1

    return cells_around

def cell_sim(rect,cells_added,boxsize):
    global cell_state
    cell_state = [] #list to track state of cells dead,alive,born (0,1,2)
    for elem in range(len(rect)):
        border_check(rect,cells_added,boxsize,elem)
        if cells_around <= 1: #less than or equal to 1 cell = cell dead (0)
            cell_state.append(0)
        elif cells_around >= 4: #more than or equal to 4 cells = cell dead (0)
            cell_state.append(0)
        elif cells_around == 2: #2 cells around = cell alive (2)
            if rect[elem] in cells_added: #checks if the currently checked cell is an alive or dead cell
                cell_state.append(1) 
            else:
                cell_state.append(0)
        elif cells_around == 3:
            if rect[elem] in cells_added:
                cell_state.append(1)
            else:
                cell_state.append(2)

def cell_changes(rect,cells_added,boxsize,window_copy,cell_color,window_color,window):
    birthed_cells = [] #list to track all born cells
    removed_cells = [] #list to track all removed cells
    cell_sim(rect,cells_added,boxsize)
    for elem in range(len(cell_state)):
        if cell_state[elem] == 2: #draws a cell if cell_state = 2
            pygame.draw.rect(window_copy,cell_color,rect[elem]) 
            pygame.draw.rect(window_copy,(20,20,20),rect[elem],1)
            birthed_cells.append(rect[elem])
        elif cell_state[elem] == 0: #removes a cell if cell_state = 0
            if rect[elem] in cells_added:
                pygame.draw.rect(window_copy,window_color,rect[elem])
                pygame.draw.rect(window_copy,(20,20,20),rect[elem],1)
                pygame.draw.rect(window,window_color,rect[elem])
                pygame.draw.rect(window,(20,20,20),rect[elem],1)
                removed_cells.append(rect[elem])
            else:
                pass

    cells_added.extend(birthed_cells)
    for elem in removed_cells:
        cells_added.remove(elem)








        


       
        
