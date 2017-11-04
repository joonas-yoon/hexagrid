from math import sqrt


class Cell:
    def __init__(self, x, y, rad):
        self.x, self.y, = 0, 0
        self.id = ''
        self.set_xy(x, y)
        self.r = rad
        self.adjacent_cells = []
        self.enabled = True
        self.item = None

    def set_xy(self, x, y, r=None):
        self.x, self.y = x, y
        self.id = "{}.{}".format(self.x, self.y)
        if r is not None:
            self.r = r

    def __str__(self):
        return str(self.id)

    def add_adjacent(self, other_cell):
        self.adjacent_cells.append(other_cell)

    def draw(self, canvas):
        x, y, r = self.x, self.y, self.r
        sr = sqrt(3) * r / 2
        self.item = canvas.create_polygon(
            x, y - r,
            x + sr, y - r / 2,
            x + sr, y + r / 2,
            x, y + r,
            x - sr, y + r / 2,
            x - sr, y - r / 2,
            fill='#ccc',
            outline='#000'
        )
        return self.item

    def enable(self, boolean):
        self.enabled = boolean

    def update(self, canvas):
        if self.enabled:
            canvas.itemconfig(self.item, fill="#ccc", outline="#000")
        else:
            canvas.itemconfig(self.item, fill="", outline="")
