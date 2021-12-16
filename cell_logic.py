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
    else:
        if cell_check_left in dead_cells:
           pass
        else:
           if iterations == 0:
                dead_cells.append(cell_check_left)
           
    if cell_check_right in cells_added:
       cells_around += 1
    else:
        if cell_check_right in dead_cells:
           pass
        else:
            if iterations == 0:
                dead_cells.append(cell_check_right)

    if cell_check_top in cells_added:
       cells_around += 1
    else:
        if cell_check_top in dead_cells:
           pass
        else:
            if iterations == 0:
                dead_cells.append(cell_check_top)
           
    if cell_check_bottom in cells_added:
       cells_around += 1
    else:
        if cell_check_bottom in dead_cells:
           pass
        else:
            if iterations == 0:
                dead_cells.append(cell_check_bottom)

    if cell_check_topLeft in cells_added:
       cells_around += 1
    else:
        if cell_check_topLeft in dead_cells:
           pass
        else:
            if iterations == 0:
                dead_cells.append(cell_check_topLeft)

    if cell_check_topRight in cells_added:
       cells_around += 1
    else:
        if cell_check_topRight in dead_cells:
           pass
        else:
            if iterations == 0:
                dead_cells.append(cell_check_topRight)
           
    if cell_check_bottomLeft in cells_added:
       cells_around += 1
    else: 
        if cell_check_bottomLeft in dead_cells:
           pass
        else:
            if iterations == 0:
                dead_cells.append(cell_check_bottomLeft) 
           
    if cell_check_bottomRight in cells_added:
       cells_around += 1
    else:
        if cell_check_bottomRight in dead_cells:
           pass
        else:
            if iterations == 0:
                dead_cells.append(cell_check_bottomRight) 


def cell_sim(cells_added,boxsize):
    global cell_state,dead_cells,iterations
    iterations = 0
    dead_cells = []
    cell_state = [] #list to track state of cells dead,alive,born (0,1,2)
    birthed_cells = []
    for elem in range(len(cells_added)):
        border_check(cells_added,cells_added,boxsize,elem)
        if cells_around <= 1: #less than or equal to 1 cell = cell dead (0)
            cell_state.append(0)
        elif cells_around >= 4: #more than or equal to 4 cells = cell dead (0)
            cell_state.append(0)
        elif cells_around == 2: #2 cells around = cell alive (2)
            cell_state.append(1) 
        elif cells_around == 3:
            cell_state.append(2)
    
    for elem in range(len(dead_cells)):
        iterations = 1
        border_check(dead_cells,cells_added,boxsize,elem)
        if cells_around <= 1: #less than or equal to 1 cell = cell dead (0)
            cell_state.append(0)
            birthed_cells.append(cell_check)
        elif cells_around >= 4: #more than or equal to 4 cells = cell dead (0)
            cell_state.append(0)
            birthed_cells.append(cell_check)
        elif cells_around == 3:
            cell_state.append(2)
            birthed_cells.append(cell_check)

    cells_added.extend(birthed_cells)


def cell_changes(cells_added,boxsize,window_copy,cell_color,window_color,window):
    removed_cells = [] #list to track all removed cells
    cell_sim(cells_added,boxsize)
    for elem in range(len(cells_added)):
        if cell_state[elem] == 2: #draws a cell if cell_state = 2
            pygame.draw.rect(window_copy,cell_color,cells_added[elem]) 
            pygame.draw.rect(window_copy,(20,20,20),cells_added[elem],1)
        elif cell_state[elem] == 0: #removes a cell if cell_state = 0
            pygame.draw.rect(window_copy,window_color,cells_added[elem])
            pygame.draw.rect(window_copy,(20,20,20),cells_added[elem],1)
            pygame.draw.rect(window,window_color,cells_added[elem])
            pygame.draw.rect(window,(20,20,20),cells_added[elem],1)
            removed_cells.append(cells_added[elem])

    for elem in removed_cells:
        cells_added.remove(elem)








        


       
        
