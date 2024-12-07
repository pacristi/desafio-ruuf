from .rectangle import Rectangle


class PanelFitter():

    def __init__(self, panel: Rectangle, ruuf: Rectangle):
        self.panel = panel
        self.ruuf = ruuf

    def fit_count(self) -> int:
        if self.panel.height == self.panel.width:
            return self._fit_count_square_panel()
        return self._fit_count_rectangle_panel()

    def _fit_count_rectangle_panel(self) -> int:
        if self.panel.has_longer_sides_than(self.ruuf):
            return 0
        return self.ruuf.area() // self.panel.area()

    def _fit_count_square_panel(self) -> int:
        count = 0
        position_x = 0
        position_y = 0

        while self.panel.can_fit_from_position_vertically(position_y, self.ruuf):
            while self.panel.can_fit_from_position_horizontally(position_x, self.ruuf):
                count += 1
                position_x += self.panel.width

            position_x = 0
            position_y += self.panel.height

        return count
