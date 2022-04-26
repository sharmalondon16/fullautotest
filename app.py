from abc import ABC, abstractmethod


class Shape(ABC):

    @abstractmethod
    def area(self):
        NotImplementedError


class Square(Shape):

    sides = 4

    def __init__(self,length):
        self.side_length = length

    def perimeter(self):
        return self.side_length*4

    def area(self):
        return self.side_length**2


if __name__ == '__main__':
    s = Square(5)

