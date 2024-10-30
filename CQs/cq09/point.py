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
