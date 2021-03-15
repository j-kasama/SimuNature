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
    canvas.create_line(0, 50*i, 1000, 50*i)
    canvas.create_line(50*i, 0, 50*i, 1000)

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
            obj_ids[i][j] = canvas.create_oval(50*i - size[i][j], 50*j - size[i][j], 50*i + size[i][j], 50*j + size[i][j])


while 1:
    for i in range(window_size):
        for j in range(window_size):
            canvas.delete(obj_ids[i][j])
            if(random.random() <= rain_rate):
                drop_size[i][j] += drop_increase
            if(drop_size[i][j] > 50):
                s = 0
                while(s + j < 20):
                    drop_size[i][s + j] = 2
                    s += 1
    draw_drop(drop_size)
    window.update()
    time.sleep(0.5)
