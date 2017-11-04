from math import sqrt
from classes.cell import Cell
from tkinter import CURRENT


class Grid:
    def __init__(self, canvas, rows, cols):
        self.canvas = canvas
        self.rows, self.cols = rows, cols
        self.cell_size = cell_size = 30
        self.grid = [[Cell(x, y, cell_size) for x in range(cols)] for y in range(rows)]

        self.canvas.bind("<ButtonPress-1>", lambda event: Grid.show_dfs(event, self))
        self.canvas.bind("<ButtonPress-3>", lambda event: Grid.delete_cell(event, self))

        for r in range(rows):
            for c in range(cols):
                dy = [-1, -1, 0, 0, 1, 1]
                dx = [0, 1, -1, 1, 0, 1]
                for d in range(6):
                    ny = r + dy[d]
                    nx = c + dx[d]
                    if ny < 0 or ny >= rows or nx < 0 or nx >= cols:
                        continue
                    self.grid[r][c].add_adjacent(self.grid[ny][nx])

        self.cell_by_item_tag = dict()

    def draw(self):
        cy = self.canvas.winfo_reqheight() / 2 - self.rows * self.cell_size * 1.5 / 2
        for row in range(self.rows):
            cx = self.canvas.winfo_reqwidth() / 2 - self.cols * self.cell_size * sqrt(3) / 2

            if row % 2:
                cx -= self.cell_size * sqrt(3) / 2

            for col in range(self.cols):
                cell = self.grid[row][col]
                cell.set_xy(cx, cy)
                cell.draw(self.canvas)
                cell.id = self.canvas.find_closest(cx, cy)
                self.cell_by_item_tag[cell.id] = cell
                cx += self.cell_size * sqrt(3)
            cy += self.cell_size * 1.5

    @staticmethod
    def delete_cell(event, grid):
        canvas = grid.canvas
        if canvas.find_withtag(CURRENT):
            item = canvas.find_closest(event.x, event.y)
            cell = grid.cell_by_item_tag[item]
            cell.enable(not cell.enabled)
            cell.update(canvas)

    @staticmethod
    def show_dfs(event, grid):
        canvas = grid.canvas
        if canvas.find_withtag(CURRENT):
            item = canvas.find_closest(event.x, event.y)
            cell = grid.cell_by_item_tag[item]
            if cell.enabled:
                Grid.dfs(canvas, cell, None)

    @staticmethod
    def dfs(canvas, cell, visited):
        if visited is None:
            visited = set()
        elif cell.id in visited:
            return None
        visited.add(cell.id)
        canvas.update_idletasks()
        canvas.after(25)
        canvas.itemconfig(cell.id, fill="red")
        for next_cell in cell.adjacent_cells:
            if next_cell.enabled:
                Grid.dfs(canvas, next_cell, visited)

        canvas.update_idletasks()
        canvas.after(25)
        canvas.itemconfig(cell.id, fill="#ccc")

