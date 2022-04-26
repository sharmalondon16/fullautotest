from abc import ABC, abstractmethod


class Shape(ABC):

    @abstractmethod
    def area(self):
        NotImplementedError





class Polygon(Shape):


    def __init__(self,sides,length):
        self.side_length = length
        self.sides = sides

    def perimeter(self):
        return self.side_length*self.sides


class Square(Polygon):

    sides = 4
    def __init__(self,length):
        super().__init__(Square.sides, length)

    def area(self):
        return Square.sides*self.side_length

    def __str__(self):
        return f'I am a {Square.sides} sided polygon with area {Square.sides*self.side_length}'




if __name__ == '__main__':
    s = Square(5)
    print(s)


