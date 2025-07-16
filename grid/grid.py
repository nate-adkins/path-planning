import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap, NoNorm 
import numpy as np
import random, math

SIZE = 10

class GridType:
    CLEAR = 0
    OBJECT = 1
    START = 2
    END = 3
    VISITED = 4
    PATH = 5

COLORS = [  "white",  # clear
            "black",  # object
            "blue",   # start
            "red",    # end
            "green",  # visited
            "gray",   # path
        ]

grid = np.zeros((SIZE, SIZE), dtype=int)

def make_rand_coord() -> tuple[int]:
    return random.randint(0,SIZE-1), random.randint(0,SIZE-1)

def gaussian_islands(count) -> None:
    for _ in range(count):
        curr_x, curr_y = make_rand_coord()
        grid[curr_x, curr_y] = GridType.OBJECT
        gaussian_fill(curr_x, curr_y, 0.5)

def gaussian_fill(x,y, prob) -> None:
    cutoff = 0.3
    attenuation  = 0.3
    if prob <= cutoff: return
    for op in [[-1,1],[0,1],[1,1],[-1,0],[1,0],[-1,-1],[0,-1],[-1,1]]:
        new_x, new_y = x+op[0], y+op[1]
        if (0 <= new_x < SIZE and 0 <= new_y < SIZE):
            grid[new_x,new_y] = GridType.OBJECT if random.random() <= (prob if (op[0] == 0 or op[1] == 0) else prob * math.sqrt(2)) else GridType.CLEAR      
            gaussian_fill(new_x, new_y, prob * attenuation)

def place_start_end(randomize = False) -> None:
    
    for type, coord in zip([GridType.START,GridType.END],[[0,0],[SIZE-1,SIZE-1]]):
        x, y = coord if not randomize else make_rand_coord()
        grid[x][y] = type

def ant_alg(start,end):
    
    x_diff = end[0] - start[0]
    y_diff = end[1] - start[1]

    if x_diff == 0 or y_diff == 0: return

    new_x, new_y = tuple[start]

    if x_diff < 0: # go left

        ant_alg
    elif x_diff > 0: # go right



def main():

    gaussian_islands(3)
    place_start_end()

    plt.figure(figsize=(10,10))

    cmap = ListedColormap(COLORS)
    plt.imshow(grid, cmap, norm=NoNorm(), origin='lower')

    plt.show()

if __name__ == '__main__':
    main()