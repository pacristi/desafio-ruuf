from .rectangle import Rectangle


class Panel(Rectangle):

    def can_fit_from_position_vertically(self, position: int,  rectangle: Rectangle):
        return self.height + position <= rectangle.height

    def can_fit_from_position_horizontally(self, position: int,  rectangle: Rectangle):
        return self.width + position <= rectangle.width

    def flip(self) -> 'Panel':
        return Panel(self.width, self.height)
