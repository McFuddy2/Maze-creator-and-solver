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



win= Window(800, 600)
win.wait_for_close()
 


    