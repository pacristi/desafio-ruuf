from dataclasses import dataclass


@dataclass
class Rectangle:
    height: int
    width: int

    def __post_init__(self):
        if self.height <= 0 or self.width <= 0:
            raise ValueError("Sides must be positive")

    def area(self):
        return self.height * self.width

    def has_longer_sides_than(self, rectangle: 'Rectangle'):
        return self.height > rectangle.height and self.width > rectangle.height or self.height > rectangle.width and self.width > rectangle.width

    def can_fit_from_position_vertically(self, position: int,  rectangle: 'Rectangle'):
        return self.height + position <= rectangle.height

    def can_fit_from_position_horizontally(self, position: int,  rectangle: 'Rectangle'):
        return self.width + position <= rectangle.width
