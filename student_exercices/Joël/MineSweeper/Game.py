from student_exercices.Joël.MineSweeper.FieldPosition import Mine
from student_exercices.Joël.MineSweeper.MineField import MineField
from string import ascii_uppercase as alphabet

class Game:
    def __init__(self):
        # Dictionary with difficult
        difficult_bombs = {
            "light": 5,
            "middle": 7,
            "hard": 10,
            "heavy": 12
        }

        # Ask for difficulty
        chosen_difficulty = None
        while chosen_difficulty not in difficult_bombs.keys():
            # chosen_difficulty = input('Prompt the difficulty of the Game. "light", "middle", "hard" and "heavy"!')
            chosen_difficulty = 'heavy' # TODO: change

        self.field = MineField(9, 9, difficult_bombs[chosen_difficulty])
        self.play()

    def play(self):

        # Until the game is not finished (win or lose)
        while self.field.remaining_empty_hidden_position() > 0:
            index_x, index_y = self.ask_next_position()
            field_position = self.field.mine_field[index_x][index_y]
            # If the position has a bomb
            if field_position.mine == Mine.BOMBE:
                print('You loose!\n', self.field.display_field(reveal_all=True))
                break
            # We reaveal the position and neighbours
            self.field.reveal_position(index_x, index_y)


    def ask_next_position(self):
        print(self.field)

        position_valid = False
        while not position_valid:
            choose_field = input('Wähle ein Feldposition? Bsp. A3 ')

            if len(choose_field) != 2 or not choose_field[0].upper() in alphabet or not choose_field[1].isdigit():
                continue

            # Line Letter position is < as field height
            if alphabet.index(choose_field[0]) > self.field.field_height-1:
                continue

            # Column is < field width
            if 0 < int(choose_field[1]) > self.field.field_width:
                continue

            return alphabet.index(choose_field[0]), int(choose_field[1]) - 1
