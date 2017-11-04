from tkinter import *
from classes.grid import Grid
from random import randint

if __name__ == "__main__":
    root = Tk()

    WIDTH, HEIGHT = 1024, 768
    canvas = Canvas(root, bg='white', width=WIDTH, height=HEIGHT)

    rows = randint(5, 15)
    cols = randint(5, 15)
    grid = Grid(canvas, rows, cols)
    grid.draw()

    canvas.pack()

    root.mainloop()
