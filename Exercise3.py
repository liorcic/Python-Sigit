# Functions that receive the game and the winning combinations and returns the winners
def find_winner(game, combinations):
    for combination in combinations:
        if game[combination[0][0]][combination[0][1]] == game[combination[1][0]][combination[1][1]] and game[combination[1][0]][combination[1][1]] == game[combination[2][0]][combination[2][1]] and game[combination[2][0]][combination[2][1]] != 0:
                return game[combination[1][0]][combination[1][1]]
    return -1


game = [[1, 2, 0],
        [2, 1, 0],
        [2, 1, 0]]
combinations = [[(0, 0), (0, 1), (0, 2)],
                [(1, 0), (1, 1), (1, 2)],
                [(2, 0), (2, 1), (2, 2)],
                [(0, 0), (1, 0), (2, 0)],
                [(0, 1), (1, 1), (2, 1)],
                [(0, 2), (1, 2), (2, 2)],
                [(0, 0), (1, 1), (2, 2)],
                [(0, 2), (1, 1), (0, 2)]]

winner = find_winner(game, combinations)
if winner == 0:
    print("Game didn't end ")
elif winner == -1:
    print("It's a tie !")
else:
    print(winner)
