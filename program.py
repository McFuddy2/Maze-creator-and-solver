from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.root = Tk()
        self.root.title("Maze solver")
        self.canvas = Canvas(self.root, width=width, height=height)
        self.canvas.pack()
        self.running = True
        self.root.protocol("WM_DELETE_WINDOW", self.close)


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
    def __init__(self, win, x1, y1, x2, y2):
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
            self._win.draw_line(self.lw, "red")
        if self.right_wall is True:       
            self._win.draw_line(self.rw, "red")
        if self.top_wall is True:
            self._win.draw_line(self.tw, "black")
        if self.bottom_wall is True:
            self._win.draw_line(self.bw, "black")


win = Window(800,600)








point1 = Point(1, 50)
point2 = Point(74, 7)
point3 = Point(1, 1)
point4 = Point(1, 100)
point5 = Point(74, 100)
line1 = Line(point1, point2)
line2 = Line(point3, point4)
line3 = Line(point1, point5)

cell1 = Cell(win, 50, 50, 100, 100)
cell1.draw()


cell2 = Cell(win, 150, 150, 200, 200)
cell2.right_wall = False
cell2.top_wall = False
cell2.draw()


cell3 = Cell(win, 400, 600, 1, 500)
cell3.draw()









win.draw_line(line1, "black")
win.draw_line(line2, "red")
win.draw_line(line3, "black")




win.wait_for_close()

