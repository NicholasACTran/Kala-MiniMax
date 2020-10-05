from kalah import KalahGame

# Given the state of the game, return the best possible move found at a certain depth
# state - The current state of the game
# depth - The depth of the search tree for the minimax algorithm
def Minimax(state, depth):
    # Generate a copy of the game, using the state passed in
    # Prevents minimax algorithm from directly altering the game
    Game = KalahGame(state)
    return 5
