import pygame
from displaywindow import *


def pattern1(boxsize,window,cell_color,cells_added):
    glidergun = [[-75,1,0,-1,10,0,1,1,1,1,1,1,0,1,-1,-1,-2,-1,-1,-1,14,0,-2,-1,-1,0,1,0,-1,2,2,0,10,1,0,-1],
                 [-40,0,1,0,0,-1,-1,-1,0,3,-2,1,1,0,1,1,1,0,-1,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,2,0,1,0]]

    x=900
    y=450
    for i in range(len(glidergun[0])):
        x += glidergun[0][i]*boxsize
        y += glidergun[1][i]*boxsize 
        rect = pygame.Rect(x,y,boxsize,boxsize)
        pygame.draw.rect(window,cell_color,rect)
        pygame.draw.rect(window,grid_color,rect,1)
        cells_added.append(rect)

def pattern2(boxsize,window,cell_color,cells_added):
    pulsar = [[0,1,1,4,1,1,2,0,0,0,0,0,-2,-1,-1,-4,-1,-1,-2,0,0,0,0,0,5,2,0,-2,0,2,0,-2,0,2,0,-2,-3,1,1,4,1,1,0,-1,-1,-4,-1,-1],[0,0,0,0,0,0,2,1,1,4,1,1,2,0,0,0,0,0,-2,-1,-1,-4,-1,-1,0,0,1,0,1,0,4,0,1,0,1,0,-5,0,0,0,0,0,2,0,0,0,0,0]]

    x=900
    y=450
    for i in range(len(pulsar[0])):
        x += pulsar[0][i]*boxsize
        y += pulsar[1][i]*boxsize 
        rect = pygame.Rect(x,y,boxsize,boxsize)
        pygame.draw.rect(window,cell_color,rect)
        pygame.draw.rect(window,grid_color,rect,1)
        cells_added.append(rect)

def pattern3(boxsize,window,cell_color,cells_added):
    flyingmachine = [[-75,-1,2,0,1,-3,0,4,0,3,-7,1,1,1,3,2,-2,3,-9,1,1,1,3,2,-4,3,-7,4,-4,2,1,-3,2,-1],[0,1,0,1,0,1,1,0,1,0,1,0,0,0,0,0,1,0,1,0,0,0,0,0,1,0,1,0,1,1,0,1,0,1]]

    x=900
    y=450
    for i in range(len(flyingmachine[0])):
        x += flyingmachine[0][i]*boxsize
        y += flyingmachine[1][i]*boxsize 
        rect = pygame.Rect(x,y,boxsize,boxsize)
        pygame.draw.rect(window,cell_color,rect)
        pygame.draw.rect(window,grid_color,rect,1)
        cells_added.append(rect)   
