from typing import Optional
import math
import time
import random

# Zadanie 1
class Point(object):
    def __init__(self, x: Optional[float | int], y: Optional[float | int]):
        if (isinstance(x, int) or isinstance(x, float)) and (isinstance(y, int) or isinstance(y, float)):
            self.x = x
            self.y = y
        else:
            raise TypeError('X i Y musza byc liczbami')


    def distance_from_origin(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

    def __eq__(self, other):
        return (self.x == other.x) and (self.y == other.y)


class Circle(Point):
    def __init__(self, x: Optional[float | int], y: Optional[float | int], radius: Optional[float | int]):
        super().__init__(x, y)
        if radius > 0:
            self.radius = radius
        else:
            raise ValueError('Promien nie moze byc ujemny')

    def edge_distance_from_origin(self) -> float:
        distance = self.distance_from_origin()
        if self.radius < distance:
            return distance - self.radius
        else:
            return self.radius - distance

    def area(self) -> float:
        return math.pi * self.radius ** 2

    def circumference(self) -> float:
        return 2 * math.pi * self.radius

    def is_point_in_circle(self, point: Point) -> bool:
        if math.sqrt((self.x - point.x) ** 2 + (self.y - point.y) ** 2) < self.radius:
            return True
        else:
            return False


    def __eq__(self, other):
        return super().__eq__(other) and self.radius == other.radius

    def __str__(self):
        return f"({self.x}, {self.y}, {self.radius})"

    def __repr__(self):
        return f"Circle({self.x}, {self.y}, {self.radius})"


def program():
    random.seed(time.time())

    punkty = []
    for i in range(100):
        punkty.append(Point(random.randint(-5, 5), random.randint(-5, 5)))

    kola = [
        Circle(0, 0, 4),
        Circle(2, 3, 2),
        Circle(-1, 2, 3),
    ]

    punkty_w_kolach = []
    punkty_nie_w_kolach = []
    for punkt in punkty:
        czy_jest_w_kolach = []
        for kolo in kola:
            if kolo.is_point_in_circle(punkt):
                czy_jest_w_kolach.append(True)
            else:
                czy_jest_w_kolach.append(False)
        if False not in czy_jest_w_kolach:
            punkty_w_kolach.append(punkt)
        else:
            punkty_nie_w_kolach.append(punkt)


    print(f'Punkty w kołach: \n{punkty_w_kolach}\n\nPunkty nie w kołach: {punkty_nie_w_kolach}')






# Testy
if __name__ == '__main__':
    #Zadanie 1
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

    # Zadanie 2
    circle = Circle(3, 4, 11)
    assert circle.edge_distance_from_origin() == 6

    circle = Circle(3, 4, 1)
    assert circle.edge_distance_from_origin() == 4
    assert round(circle.area(), 1) == 3.1
    assert round(circle.circumference(), 1) == 6.3

    circle1 = Circle(2, 1, 4)
    circle2 = Circle(2, 1, 4)
    circle3 = Circle(3, 4, 2)
    assert circle1 == circle2
    assert not (circle1 == circle3)

    circle4 = Circle(1, 2, 3)
    assert str(circle4) == '(1, 2, 3)'
    assert repr(circle4) == 'Circle(1, 2, 3)'

    try:
        Circle('dzien dobry', 1, 1)
    except Exception as error:
        assert isinstance(error, TypeError)

    try:
        Circle(1, 1, -20)
    except Exception as error:
        assert isinstance(error, ValueError)

    program()