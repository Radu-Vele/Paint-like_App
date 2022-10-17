# @author: Radu-Augustin Vele

import tkinter as tk

#a 2D point
class Point(object):
    def __init__(self, x, y):
        self._x = x
        self._y = y
    
    def getX(self):
        return self._x

    def setX(self, new_x):
        if(new_x > 0):
            self._x = new_x

    x = property(getX, setX)

    def getY(self):
        return self._y

    def setY(self, new_y):
        if(new_y > 0):
            self._y = new_y

    y = property(getY, setY)

#interface class
class Interface(object):
    def __init__(self):

        self._corner1 = Point(0, 0)
        self._corner2 = Point(0, 0)

        self._root = tk.Tk()
        self._root.title('Paint but Cooler')
        self._root.geometry('750x500')
        
        self._l1 = tk.Label(self._root, text = "Select the background color:").grid(row = 0, column =1)
        self._l2 = tk.Label(self._root, text = "Select the shape:").grid(row = 4, column = 1)
        
        self._button1 = tk.Button(self._root, text = "Red", activebackground="#EA9C8E", bg="#E92C0A", height= 3, width=15)
        self._button1.bind('<Button-1>', self.getRed)
        self._button1.grid(row = 1, column =1)

        self._button2 = tk.Button(self._root, text = "Blue", activebackground="lightblue", bg="blue", height= 3, width=15)
        self._button2.bind('<Button-1>', self.getBlue)
        self._button2.grid(row = 2, column =1)

        self._button3 = tk.Button(self._root, text = "Yellow", activebackground="lightyellow", bg="yellow", height= 3, width=15)
        self._button3.bind('<Button-1>', self.getYellow)
        self._button3.grid(row = 3, column =1)

        
        self._l3 = tk.Label(self._root, text = "Selected color:").grid(row = 0, column =3)
        self._l4 = tk.Label(self._root, text = "Selected shape:").grid(row = 2, column =3)

        self._shape = tk.StringVar()
        self._shape.set("No_Shape_Selected")
        tk.Label(self._root, textvariable=self._shape).grid(row = 3, column = 3)

        self._color = tk.StringVar()
        self._color.set("No_Color_Selected")
        tk.Label(self._root, textvariable=self._color).grid(row = 1, column = 3)

        

        self._button4 = tk.Button(self._root, text = "Line", activebackground="lightgrey", bg="grey", height= 3, width=15)
        self._button4.bind('<Button-1>', self.getLine)
        self._button4.grid(row = 5, column =1)

        self._button5 = tk.Button(self._root, text = "Rectangle", activebackground="lightgrey", bg="grey", height= 3, width=15)
        self._button5.bind('<Button-1>', self.getRectangle)
        self._button5.grid(row = 6, column =1)

        self._button6 = tk.Button(self._root, text = "Oval", activebackground="lightgrey", bg="grey", height= 3, width=15)
        self._button6.bind('<Button-1>', self.getOval)
        self._button6.grid(row = 7, column =1)


        self._canvas = tk.Canvas(self._root, bg = "lightgrey", height = 500, width = 450)
        self._canvas.grid(row = 0, rowspan= 10, column = 2)
        self._canvas.bind('<Button-1>', self.getCoordinates)

        self._clr_button = tk.Button(self._root, text = "Clear Canvas", activebackground="lightgrey", bg = "grey", height = 3, width = 15)
        self._clr_button.grid(row = 5, column = 3)
        self._clr_button.bind('<Button-1>', self.clearCanvas)

        self._res_button = tk.Button(self._root, text = "Clear Selection", activebackground="lightgrey", bg = "grey", height = 3, width = 15)
        self._res_button.grid(row = 6, column = 3)
        self._res_button.bind('<Button-1>', self.reset)

        self._root.mainloop()
       

    def getLine(self, event):
        self._shape.set("Line")

    def getRectangle(self, event):
         self._shape.set("Rectangle")

    def getOval(self, event):
         self._shape.set("Oval")

    def getRed(self, event):
        self._color.set("red")

    def getBlue(self, event):
         self._color.set("blue")

    def getYellow(self, event):
         self._color.set("yellow")


    def draw(self, x1, y1, x2, y2):

        if(self._color.get() == "No_Color_Selected" or self._shape.get() == "No_Shape_Selected"):
            self._canvas.create_text(x1, y1, text = "Careful: Color and/or shape not selected!")
            
            
        if(self._shape.get() == "Line"):
            self._canvas.create_line(x1, y1, x2, y2, fill = self._color.get(), width="1")
        else:
            if(self._shape.get() == "Oval"):
                self._canvas.create_oval(x1, y1, x2, y2, fill = self._color.get())
            else:
                if(self._shape.get() == "Rectangle"):
                    self._canvas.create_rectangle(x1, y1, x2, y2, fill = self._color.get())

    def clearCanvas(self, event):
        self._canvas.delete("all")        

    def reset(self, event):
        self._shape.set("No_Shape_Selected")
        self._color.set("No_Color_Selected")

    def getCoordinates(self, event):
            global count_click

            if(count_click == 0): #first point
                self._corner1.x = event.x
                self._corner1.y = event.y
                count_click += 1
            else:
                self._corner2.x = event.x
                self._corner2.y = event.y
                count_click = 0
                self.draw(self._corner1.x, self._corner1.y, self._corner2.x, self._corner2.y)



if __name__ == '__main__':
    count_click = 0
    my_interface = Interface()

