from CQs.cq09.point import Point

"""Checking whether the point class works"""
___author___: str = "730766272"

new_point: Point = Point(5.2, 4.5)
new_point.scale_by(2)
print(new_point.x)
print(new_point.y)
new_point2 = new_point.scale(2)
print(new_point.x)
print(new_point.y)
print(new_point2.x)
print(new_point2.y)
