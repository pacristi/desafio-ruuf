from dataclasses import dataclass


@dataclass
class Rectangle:
    height: int
    width: int

    def __post_init__(self):
        if self.height <= 0 or self.width <= 0:
            raise ValueError("Sides must be positive")
