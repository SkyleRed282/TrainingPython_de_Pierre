class Grid:

    def __init__(self):
        cells = []
        for _ in range(3):
            cells.append([' ', ' ', ' '])

        self.cells = cells

    def __str__(self):
        rep = ''
        for x in range(3):
            for y in range(3):
                rep += f'[{self.cells[x][y]}]'
            rep += '\n'
        return rep
