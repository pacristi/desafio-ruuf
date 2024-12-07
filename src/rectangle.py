from dataclasses import dataclass


@dataclass
class Rectangle:
    side_1: int
    side_2: int

    def area(self):
        return self.side_1 * self.side_2

    def has_longer_sides_than(self, rectangle: 'Rectangle'):
        return self.side_1 > rectangle.side_1 and self.side_2 > rectangle.side_1 or self.side_1 > rectangle.side_2 and self.side_2 > rectangle.side_2
