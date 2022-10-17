#simple class
class Square(object):
    def __init__(self, length_of_side):
        self._length_of_side = length_of_side
    
    def getLength(self):
        return self._length_of_side

    def setLenght(self, new_lenght):
        if new_lenght > 0:
            self._length_of_side = new_lenght
        else:
            print("Error")

    def getArea(self):
        return self._length_of_side ** 2
    
    def getPerimeter(self):
        return self._length_of_side * 4

    def __str__(self):
        return ("Square object with lenght = %d" %(self._length_of_side))

    length_of_side = property(getLength, setLenght)
    area = property(getArea)
    perimeter = property(getPerimeter)


#inherit from square
class ColouredSquare(Square):
    def __init__(self, length, colour):
        super().__init__(length)
        self._colour = colour

    def getColor(self):
        return self._colour

    def setColor(self, new_colour):
        self._colour = new_colour

    colour = property(getColor, setColor)

    def __str__(self):
        return ("%s, and colour %s" %(super().__str__(), self._colour))

#operator overloading
    def __eq__(self, square2):
        if self.length_of_side == square2.length_of_side and self.colour == square2.colour:
            return True
        else:
            return False

    


#main
if __name__ == "__main__":
    sqr1 = Square(10)

    col_sqr = ColouredSquare(10, "red")

    print(col_sqr.length_of_side)

    col_sqr2 = ColouredSquare(10, "red")

    print(col_sqr == col_sqr2)