import pygame 

def pattern(boxsize,window,cell_color,cells_added):
    glidergun = [[-75,1,0,-1,10,0,1,1,1,1,1,1,0,1,-1,-1,-2,-1,-1,-1,14,0,-2,-1,-1,0,1,0,-1,2,2,0,10,1,0,-1],[-40,0,1,0,0,-1,-1,-1,0,3,-2,1,1,0,1,1,1,0,-1,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,2,0,1,0]]
    pulsar = [[0,1,1,4,1,1,2,0,0,0,0,0,-2,-1,-1,-4,-1,-1,-2,0,0,0,0,0,5,2,0,-2,0,2,0,-2,0,2,0,-2,-3,1,1,4,1,1,0,-1,-1,-4,-1,-1],[0,0,0,0,0,0,2,1,1,4,1,1,2,0,0,0,0,0,-2,-1,-1,-4,-1,-1,0,0,1,0,1,0,4,0,1,0,1,0,-5,0,0,0,0,0,2,0,0,0,0,0]]
    flyingmachine = [[-75,-1,2,0,1,-3,0,4,0,3,-7,1,1,1,3,2,-2,3,-9,1,1,1,3,2,-4,3,-7,4,-4,2,1,-3,2,-1],[0,1,0,1,0,1,1,0,1,0,1,0,0,0,0,0,1,0,1,0,0,0,0,0,1,0,1,0,1,1,0,1,0,1]]
    pattern_list = flyingmachine

    x=900
    y=450
    for i in range(len(pattern_list[0])):
        x += pattern_list[0][i]*boxsize
        y += pattern_list[1][i]*boxsize 
        rect = pygame.Rect(x,y,boxsize,boxsize)
        pygame.draw.rect(window,cell_color,rect)
        cells_added.append(rect)

def pattern1(boxsize,window,cell_color,cells_added):
    glidergun = [[-75,1,0,-1,10,0,1,1,1,1,1,1,0,1,-1,-1,-2,-1,-1,-1,14,0,-2,-1,-1,0,1,0,-1,2,2,0,10,1,0,-1],[-40,0,1,0,0,-1,-1,-1,0,3,-2,1,1,0,1,1,1,0,-1,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,2,0,1,0]]
    pattern_list = glidergun

    x=900
    y=450
    for i in range(len(pattern_list[0])):
        x += pattern_list[0][i]*boxsize
        y += pattern_list[1][i]*boxsize 
        rect = pygame.Rect(x,y,boxsize,boxsize)
        pygame.draw.rect(window,cell_color,rect)
        cells_added.append(rect)

def pattern2(boxsize,window,cell_color,cells_added):
      pulsar = [[0,1,1,4,1,1,2,0,0,0,0,0,-2,-1,-1,-4,-1,-1,-2,0,0,0,0,0,5,2,0,-2,0,2,0,-2,0,2,0,-2,-3,1,1,4,1,1,0,-1,-1,-4,-1,-1],[0,0,0,0,0,0,2,1,1,4,1,1,2,0,0,0,0,0,-2,-1,-1,-4,-1,-1,0,0,1,0,1,0,4,0,1,0,1,0,-5,0,0,0,0,0,2,0,0,0,0,0]]
      pattern_list = pulsar

      x=900
      y=450
      for i in range(len(pattern_list[0])):
        x += pattern_list[0][i]*boxsize
        y += pattern_list[1][i]*boxsize 
        rect = pygame.Rect(x,y,boxsize,boxsize)
        pygame.draw.rect(window,cell_color,rect)
        cells_added.append(rect)

def pattern3(boxsize,window,cell_color,cells_added):
      flyingmachine = [[-75,-1,2,0,1,-3,0,4,0,3,-7,1,1,1,3,2,-2,3,-9,1,1,1,3,2,-4,3,-7,4,-4,2,1,-3,2,-1],[0,1,0,1,0,1,1,0,1,0,1,0,0,0,0,0,1,0,1,0,0,0,0,0,1,0,1,0,1,1,0,1,0,1]]
      pattern_list = flyingmachine

      x=900
      y=450
      for i in range(len(pattern_list[0])):
        x += pattern_list[0][i]*boxsize
        y += pattern_list[1][i]*boxsize 
        rect = pygame.Rect(x,y,boxsize,boxsize)
        pygame.draw.rect(window,cell_color,rect)
        cells_added.append(rect)       
