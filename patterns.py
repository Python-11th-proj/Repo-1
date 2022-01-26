def pattern():
    repeat = [[0, 10, 0, 10],[0, 0, 10, -10]]
    for i in len(repeat):
        rect = pygame.Rect(900+repeat[0][i],450+repeat[1][i],boxsize,boxsize)
        pygame.draw.rect(window,cell_color,rect)
