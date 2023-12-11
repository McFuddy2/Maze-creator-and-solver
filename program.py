from tkinter import Tk, BOTH, Canvas
import time

class Window:
    def __init__(self, width, height):
        self.root = Tk()
        self.root.title("Maze solver")
        self.canvas = Canvas(self.root, width=width, height=height)
        self.canvas.pack()
        self.running = True
        self.root.protocol("WM_DELETE_WINDOW", self.close)
        self.width = width
        self.height = height


    def redraw(self):
        self.root.update_idletasks() 
        self.root.update()


    def wait_for_close(self):
        while self.running:
            self.redraw()


    def close(self):
        self.running = False
        self.root.destroy()

    def draw_line(self, line, fill_color):
        line.draw(self.canvas, fill_color)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def draw(self, canvas, fill_color):
        x1, y1 = self.point1.x, self.point1.y
        x2, y2 = self.point2.x, self.point2.y
        canvas.create_line(x1, y1, x2, y2, fill=fill_color, width=2)
        canvas.pack()

class Cell:
    def __init__(self, x1, y1, x2, y2, win=None):
        self.left_wall = True
        self.right_wall = True
        self.top_wall = True
        self.bottom_wall = True
        self.lw = Line(Point(x1,y1), Point(x1,y2))
        self.rw = Line(Point(x2,y1), Point(x2,y2))
        self.tw = Line(Point(x1,y1), Point(x2,y1))
        self.bw = Line(Point(x1,y2), Point(x2,y2))
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        self._win = win

    def draw(self):
        
        x1, y1, x2, y2 = self._x1, self._x2, self._y1, self._y2
        if self.left_wall is True:
            self._win.draw_line(self.lw, "black")
        else:
            self._win.draw_line(self.lw, "white")
        if self.right_wall is True:       
            self._win.draw_line(self.rw, "green")
        else:
            self._win.draw_line(self.rw, "blue")
        if self.top_wall is True:
            self._win.draw_line(self.tw, "pink")
        else:
            self._win.draw_line(self.tw, "purple")
        if self.bottom_wall is True:
            self._win.draw_line(self.bw, "orange")
        else:
            self._win.draw_line(self.bw, "yellow")



    def draw_move(self, to_cell, undo=False):
        line = "green"
        if undo == True:
            line = "red"

        mid_x = (self._x1 + self._x2) /2
        mid_y = (self._y1 + self._y2) /2
        from_point = Point(mid_x, mid_y)
        mid_x2 = (to_cell._x1 + to_cell._x2) /2
        mid_y2 = (to_cell._y1 + to_cell._y2) /2
        to_point = Point(mid_x2, mid_y2)
        path = Line(from_point, to_point)
        self._win.draw_line(path, "black")



class Maze:
    def __init__(self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win=None
    ):
        self._x1, = x1,
        self._y1, = y1,
        self.num_rows, = num_rows,
        self.num_cols, = num_cols,
        self.cell_size_x, = cell_size_x,
        self.cell_size_y, = cell_size_y,
        self.win, = win,
        self._cells = []
        self._create_cells()
        print(f"top wall before break {self._cells[0][0].top_wall}")
        self._break_entrance_and_exit()
        print(f"top wall after break {self._cells[0][0].top_wall}")

    def _break_entrance_and_exit(self):
        self._cells[0][0].top_wall = False
        self._cells[self.num_cols - 1][self.num_rows - 1].bottom_wall = False

        self._draw_cell(0,0)
        self._draw_cell(self.num_cols - 1, self.num_rows - 1)
        self._animate()
       


    def _create_cells(self):
        for i in range(self.num_cols):
            col = []
            for j in range(self.num_rows):
                cell_x1 = self._x1 + i * self.cell_size_x
                cell_y1 = self._y1 + j * self.cell_size_y
                cell_x2 = cell_x1 + self.cell_size_x
                cell_y2 = cell_y1 + self.cell_size_y

                cell = Cell(cell_x1, cell_y1, cell_x2, cell_y2, self.win)
                col.append(cell)

                self._draw_cell(i, j)
            self._cells.append(col)



    def _draw_cell(self, i, j):
        cell_x1 = self._x1 + i * self.cell_size_x
        cell_y1 = self._y1 + j * self.cell_size_y
        cell_x2 = self._x1 + (i + 1) * self.cell_size_x
        cell_y2 = self._y1 + (j + 1) * self.cell_size_y

        cell = Cell(cell_x1, cell_y1, cell_x2, cell_y2, self.win)
        cell.draw()
        self._animate()

    def _animate(self):
        self.win.redraw()
        time.sleep(0.05)











# width, height
win = Window(800,600)

#10,10,row,col,size, size, window)
# row 600 - 10 // 50 = 11
# col 800 - 10 // = 15 

first_maze = Maze(10,10,11,15,50,50,win)





win.wait_for_close()
