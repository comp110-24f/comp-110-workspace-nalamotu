from __future__ import annotations

"""Practice with Classes"""

___author___: str = "730766272"


class Point:
    x: float
    y: float

    def __init__(self, x_init: float, y_init: float):
        self.x = x_init
        self.y = y_init

    def scale_by(self, factor: int) -> None:
        self.x *= factor
        self.y *= factor

    def scale(self, factor: int) -> Point:
        new_point: Point = Point(self.x * factor, self.y * factor)
        return new_point


class Line:
    start: Point
    end: Point

    def __init__(self, start: Point, end: Point):
        self.start = start
        self.end = end

    def get_length(self) -> float:
        length: float = (
            (self.end.x - self.start.x) ** 2 + (self.end.y - self.start.y) ** 2
        ) ** 0.5
        return length
