import numpy as np
grid = np.zeros((3,3), dtype=str)
def avalible_space(grid, x, y):
    try:
        if not grid[x,y] == '':
            return False
        else:
            return True
    except:
        return False


def winner(grid): # dosent work :c
    xc,oc=0,0
    for i in range(3):
        for o in range(3):
            if grid[o,i] == 'x':
                xc +=1
            if grid[o,i] == 'o':
                oc +=1

    if xc == 3:
        return "x"
    elif oc == 3:
        return "o"
                

grid[0,0] = 'o'
grid[0,1] = 'o'
grid[0,2] = 'o'
print(grid) 
print(f"{winner(grid)} won")
