from typing import Optional
import math


class Point(object):
    def __init__(self, x: Optional[float | int], y: Optional[float | int]):
        self.x = x
        self.y = y

    def distance_from_origin(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

    def __eq__(self, other):
        return (self.x == other.x) and (self.y == other.y)



if __name__ == '__main__':
    point = Point(3, 4)
    assert point.distance_from_origin() == 5
    assert str(point) == '(3, 4)'
    assert repr(point) == 'Point(3, 4)'

    point = Point(0, 0)
    assert point.distance_from_origin() == 0
    assert str(point) == '(0, 0)'
    assert repr(point) == 'Point(0, 0)'

    point = Point(-3, -4)
    assert point.distance_from_origin() == 5
    assert str(point) == '(-3, -4)'
    assert repr(point) == 'Point(-3, -4)'

    point1 = Point(3, 4)
    point2 = Point(3, 4)
    point3 = Point(6, 7)

    assert point1 == point2
    assert not (point1 == point3)