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
            chosen_difficulty = input('Prompt the difficulty of the Game. "light", "middle", "hard" and "heavy"!')

        self.mine_field = MineField(9, 9, difficult_bombs[chosen_difficulty])
        self.play()

    def play(self):

        while self.mine_field.remaining_empty_hidden_position() > 0:
            print(self.ask_next_position())

    def ask_next_position(self):
        print(self.mine_field)

        position_valid = False
        while not position_valid:
            choose_field = input('Wähle ein Feldposition? Bsp. A3')

            if len(choose_field) != 2 or choose_field[0].upper() in alphabet or not choose_field[1].isdigit():
                continue

            if alphabet.index(choose_field[0]) > self.mine_field.field_height - 1:
                continue
            if int(choose_field[1]) > self.mine_field.field_width - 1:
                continue

            return alphabet.index(choose_field[0]), int(choose_field[1]) - 1
