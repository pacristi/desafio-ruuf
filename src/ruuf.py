from .rectangle import Rectangle


class Ruuf(Rectangle):

    def __init__(self, height: int, width: int):
        super().__init__(height, width)
        self.tiles = [[0 for _ in range(self.width)]
                      for _ in range(self.height)]

    def can_fit(self, rectangle: Rectangle, x: int, y: int) -> bool:
        try:
            for i in range(rectangle.height):
                for j in range(rectangle.width):
                    if self.tiles[i + y][j + x] == 1:
                        raise IndexError()
            return True
        except IndexError:
            return False

    def place(self, rectangle: Rectangle, x: int, y: int):
        for i in range(rectangle.height):
            for j in range(rectangle.width):
                self.tiles[y + i][x + j] = 1
