from .ruuf import Ruuf
from .panel import Panel


class PanelFitter():

    def __init__(self, panel: Panel, ruuf: Ruuf):
        self.panel = panel
        self.ruuf = ruuf

    def fit_count(self) -> int:
        count = 0

        for y in range(self.ruuf.height):
            for x in range(self.ruuf.width):
                if self.ruuf.can_fit(self.panel, x, y):
                    self.ruuf.place(self.panel, x, y)
                    count += 1
                elif self.ruuf.can_fit(self.panel.flip(), x, y):
                    self.ruuf.place(self.panel.flip(), x, y)
                    count += 1

        return count
