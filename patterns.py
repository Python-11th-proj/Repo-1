import pygame
import csv
from displaywindow import *

with open("pattern.csv","r") as f:
    data = list(csv.reader(f))


def pattern1(boxsize,window,cell_color,cells_added):
    glidergun = data[0]

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
    pulsar = data[1]

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
    flyingmachine = data[2]

    x=900
    y=450
    for i in range(len(flyingmachine[0])):
        x += flyingmachine[0][i]*boxsize
        y += flyingmachine[1][i]*boxsize 
        rect = pygame.Rect(x,y,boxsize,boxsize)
        pygame.draw.rect(window,cell_color,rect)
        pygame.draw.rect(window,grid_color,rect,1)
        cells_added.append(rect)   
