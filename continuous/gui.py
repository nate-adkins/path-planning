import tkinter as tk
from continuous.map import Map, Obstacle
from continuous.map_helpers import *

root = tk.Tk()
root.geometry("700x700")
root.title("Planning Algorithms Testing")



mouse_x = None
mouse_y = None

def on_canvas_click(event) -> None:
    mouse_x = event.x
    mouse_y = event.y
    print(f"{mouse_x},{mouse_y}")

canvas = tk.Canvas(root, width=SIZE_X, height=SIZE_Y, border=None, background='white',)
canvas.bind("<Button-1>", on_canvas_click)
canvas.pack()

map = Map(SIZE_X,SIZE_Y)
map.obstacles.append(Obstacle([[100,100],[100,300],[200,250]]))
map.obstacles.append(Obstacle([[450,400],[300,400],[100,450]]))

def draw_obstacle(obstacle: Obstacle) -> None:
    length = len(obstacle.vertices)
    for i in range(length):
        last_index = 0 if i == length-1 else i+1
        x1, y1 = obstacle.vertices[i][0], obstacle.vertices[i][1]
        x2, y2 = obstacle.vertices[last_index][0],obstacle.vertices[last_index][1]
    canvas.create_line(x1,y1,x2,y2)


def update_obstacles(map: Map = map) -> None:
    for obstacle in map.obstacles:
        draw_obstacle(obstacle)
    
update_obstacles()
root.mainloop() 
