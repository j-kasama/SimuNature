import tkinter as tk
import random
import time

window_size = 20
rain_rate = 0.1
drop_increase = 5
reset_size = 50

window = tk.Tk()
canvas = tk.Canvas(master=window, width=1000, height=1000)

for i in range(window_size):
    canvas.create_line(0, reset_size*i, 1000, reset_size*i)
    canvas.create_line(reset_size*i, 0, reset_size*i, 1000)

canvas.pack()

drop_size = []
obj_ids = []
for i in range(window_size):
    drop_size.append([])
    obj_ids.append([])
    for j in range(window_size):
        drop_size[i].append(0)
        obj_ids[i].append(0)

def draw_drop(size):
    for i in range(window_size):
        for j in range(window_size):
            obj_ids[i][j] = canvas.create_oval(reset_size*i - size[i][j], reset_size*j - size[i][j], reset_size*i + size[i][j], reset_size*j + size[i][j])


while 1:
    for i in range(window_size):
        for j in range(window_size):
            canvas.delete(obj_ids[i][j])
            if(random.random() <= rain_rate):
                drop_size[i][j] += drop_increase
            if(drop_size[i][j] > reset_size):
                s = 0
                while(s + j < window_size):
                    drop_size[i][s + j] = 2
                    s += 1
    draw_drop(drop_size)
    window.update()
    time.sleep(0.5)
