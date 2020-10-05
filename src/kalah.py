class Cup:
    def __init__(self, type, value, number, nextCup, captureCup):
        self.type = type
        self.value = value
        self.nextCup = nextCup
        self.captureCup = captureCup
        self.number = number

    def Sow(self):
        self.value = self.value + 1

    def Harvest(self):
        self.value = 0

    def Capture(self, num):
        self.value = self.value + num

    def __str__(self):
        return f'Cup {self.number}: {self.value} seeds'

class KalahGame:
    #TODO: Make overloaded constructor to make copy of game given a game state
    def __init__(self):
        self.state = {
            'board': self.GenerateInitialBoardState(),
            'possibleMoves': [1, 2, 3, 4],
            'score': (0, 0)
        }
        self.end = False

    def GenerateInitialBoardState(self):
        cups = []
        type = 1
        for i in range(1,11):
            if i % 5 == 0:
                type = 0
            cups.append(Cup(type=type,
                            value=4*type,
                            number=i,
                            nextCup=(i+1)%10,
                            captureCup=10-i))
            type = 1
        return cups

    def MakeMove(self, move):
        # If the move is currently a possible move
        if move in self.state['possibleMoves']:
            seeds = self.state['board'][move-1].value
            currentCup = move
            nextCup = self.state['board'][move-1].nextCup
            self.state['board'][move-1].Harvest()
            repeat = False

            # While there are still seeds to drop
            while seeds > 0:
                # If next cup to drop in would be the opponents scoring cup, skip
                if move < 5 and nextCup == 10:
                    nextCup = 1
                elif move > 5 and nextCup == 5:
                    nextCup = 6
                else:
                    # Else, drop a seed into the next cup
                    # Set current cup to the cup that was just dropped in
                    # Get the next cup
                    self.state['board'][nextCup - 1].Sow()
                    currentCup = nextCup
                    nextCup = self.state['board'][nextCup - 1].nextCup
                    seeds = seeds - 1

            # If the last cup dropped was a scoring cup, get an additional move
            if currentCup % 5 == 0:
                repeat = True
            elif self.state['board'][currentCup-1].value == 1:
                # Else if the last cup dropped was empty before dropping
                # Capture that cup and the opposite cup
                total = 1 + self.state['board'][10 - currentCup-1].value
                self.state['board'][currentCup-1].Harvest()
                self.state['board'][10-currentCup-1].Harvest()
                if move < 5:
                    self.state['board'][4].Capture(total)
                else:
                    self.state['board'][9].Capture(total)

            # Setting the score
            self.state['score'] = (self.state['board'][4].value, self.state['board'][9].value)

            # Determining possible moves
            possibleMoves = []
            if repeat:
                # If gaining another consecutive move, check moves of the same parity
                if move < 5:
                    for i in range(4):
                        if self.state['board'][i].value > 0:
                            possibleMoves.append(i+1)
                else:
                    for i in range(5, 9):
                        if self.state['board'][i].value > 0:
                            possibleMoves.append(i+1)
            else:
                # Else check moves of opposite parity
                if move < 5:
                    for i in range(5, 9):
                        if self.state['board'][i].value > 0:
                            possibleMoves.append(i+1)
                else:
                    for i in range(4):
                        if self.state['board'][i].value > 0:
                            possibleMoves.append(i+1)

            self.state['possibleMoves'] = possibleMoves

            # If there are no possible moves, set the end flag
            if len(possibleMoves) == 0:
                self.end = True

    def __str__(self):
        str = 'Game Board: \n'
        for i in range(8, 4, -1):
            str = str + f'{self.state["board"][i].value} '
        str = str + '\n'
        for i in range(4):
            str = str + f'{self.state["board"][i].value} '
        str = str + '\n'
        str = str + f'Possible Moves: {self.state["possibleMoves"]}\n'
        str = str + f'Score: P1 {self.state["score"][0]} P2 {self.state["score"][1]}'
        return str

# #Testing
# cup = KalahGame()
# print(cup.state['board'][0])
