import math


class Circle:
    r: float

    def __init__(self, r: float):
        self.r = r

    def area(self) -> float:
        circ_area: float = math.pi * self.r**2
        return circ_area


class Rectangle:
    w: float
    h: float

    def __init__(self, w: float, h: float):
        self.w = w
        self.h = h

    def area(self) -> float:
        rect_area: float = self.w * self.h
        return rect_area
