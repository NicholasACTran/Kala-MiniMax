from kalah import KalahGame
from minimax import Minimax

Game = KalahGame()
while not Game.end:
    #TODO: Add Call to Minimax function to make the move for computer
    print(Game)
    print('Make a move')
    move = int(input())
    if move in Game.state['possibleMoves']:
        Game.MakeMove(move)
    else:
        print('Invalid Move')
