from .rectangle import Rectangle


class PanelFitter():

    def __init__(self, panel: Rectangle, ruuf: Rectangle):
        self.panel = panel
        self.ruuf = ruuf

    def fit_count(self) -> int:
        if self.panel.has_longer_sides_than(self.ruuf):
            return 0
        return self.ruuf.area() // self.panel.area()
