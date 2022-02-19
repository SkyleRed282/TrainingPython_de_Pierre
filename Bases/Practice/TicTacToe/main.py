from Bases.Practice.TicTacToe.AI import AI
from Bases.Practice.TicTacToe.Game import Game
from Bases.Practice.TicTacToe.Human import Human

if __name__ == '__main__':

    answer1 = input('AI battle? A or Human vs AI? H ')

    if answer1 == 'A':
        player1 = AI()
    else:
        player1 = Human()
    player2 = AI()

    game = Game(player1=player1, player2=player2)
    print(game.grid)

