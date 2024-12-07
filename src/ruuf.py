from .rectangle import Rectangle


class Ruuf(Rectangle):

    def __init__(self, height: int, width: int):
        super().__init__(height, width)
        self.tiles = [[0 for _ in range(self.width)]
                      for _ in range(self.height)]

    def place_panel(self, panel: Rectangle, x: int, y: int):
        for i in range(panel.height):
            self.tiles[y + i][x:x + panel.width] = [1] * panel.width

    def can_fit_panel(self, panel: Rectangle, x: int, y: int) -> bool:
        for i in range(panel.height):
            for j in range(panel.width):
                if self.tiles[i + y][j + x] == 1:
                    return False
        return True
