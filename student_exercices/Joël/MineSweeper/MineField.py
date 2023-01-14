from random import randint
from string import ascii_uppercase as alphabet
from student_exercices.Joël.MineSweeper.FieldPosition import Mine, FieldPosition, Status


class MineField:

    def __init__(self, field_width, field_height, amount_bombs_perc):
        self.field_width = field_width
        self.field_height = field_height
        self.mine_field = self.init_field()
        self.place_bombs(amount_bombs_perc)

    def init_field(self):

        field = []

        # für jede linie
        for _ in range(self.field_width):
            # neue liste erfassen
            new_line = []
            # für jede "mine"
            for _ in range(self.field_height):
                # neue empty "mine" in linie liste einfugen
                new_line.append(FieldPosition(Mine.LEER))

            # linie liste in field einfugen
            field.append(new_line)

        return field

    def remaining_empty_hidden_position(self):
        counter = 0
        for line in self.mine_field:
            for field_postion in line:
                if field_postion.mine == Mine.LEER and field_postion.status == Status.HIDDEN:
                    counter += 1

        return counter

    def reveal_position(self, index_x, index_y):
        print(self.get_neighbours_position(index_x, index_y))

    def get_neighbours_position(self, index_x, index_y):

        # X X X
        # X Y X
        # X X X
        field_positions = []
        for pos_x in range(index_x-1, index_x+2):
            for pos_y in range(index_y-1, index_y+2):
                # not the base position
                if pos_x != index_x or pos_y != index_y:
                    if pos_x >= 0 < self.field_width and pos_y >= 0 < self.field_height:
                        field_positions.append((pos_x, pos_y))

        return field_positions

    def place_bombs(self, amount_bombs_perc):

        # Give the number of bombs
        bombs_to_place = int(amount_bombs_perc / 100 * self.field_width * self.field_height)

        # Until we placed all the bombes
        while bombs_to_place > 0:

            # random postion für die neue Bombe
            position_x = randint(0, self.field_width - 1)
            position_y = randint(0, self.field_height - 1)

            # Ist die Zelle leer platzieren wir eine Bombe
            if self.mine_field[position_x][position_y].mine is Mine.LEER:
                self.mine_field[position_x][position_y] = FieldPosition(Mine.BOMBE)
                bombs_to_place -= 1

    def __str__(self):
        return self.display_field()

    def display_field(self, reveal_all=False):
        #    1  2  3
        # 1  ?  ?  ?
        # 2  ?  ?  ?
        # 3  ?  ?  ?

        field_str = '   '

        # column headers
        for zahl in range(1, self.field_width + 1):
            field_str += str(zahl) + ' '

        # for each line
        for line_nbr, line_lst in enumerate(self.mine_field):

            field_str += f'\n {alphabet[line_nbr]} '

            # for each element
            for field_position in line_lst:
                field_str += f'{field_position.display_position(reveal_all)} '

        return field_str
