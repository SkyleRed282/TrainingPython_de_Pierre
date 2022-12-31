from student_exercices.Joël.MineSweeper.Mine import Mine, FieldPosition


class MineField:

    def __init__(self, field_width=10, field_height=12):
        self.mine_field = self.init_field_bombs(field_width, field_height)
        self.field_width = field_width
        self.field_height = field_height

    def init_field_bombs(self, field_width, field_height):


        field = []

        # für jede linie
        for _ in range(field_width):
            # neue liste erfassen
            new_line = []
            # für jede "mine"
            for _ in range(field_height):
                # neue empty "mine" in linie liste einfugen
                new_line.append(FieldPosition(Mine.LEER))

            # linie liste in field einfugen
            field.append(new_line)

        return field

    # TODO: init bombes based on difficulty
    # add X bombes in random position from the field

    def __str__(self):

        #    1  2  3
        # 1  ?  ?  ?
        # 2  ?  ?  ?
        # 3  ?  ?  ?

        field_str = '   '

        # column headers
        for zahl in range(1, self.field_width+1):
            field_str += str(zahl) + ' '


        # for each line
        for line_nbr, line_lst in enumerate(self.mine_field):

            field_str += f'\n {line_nbr+1} '

            # for each element
            for field_position in line_lst:
                field_str += f'{field_position} '


        return field_str
