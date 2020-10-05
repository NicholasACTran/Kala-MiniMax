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

    def __string__(self):
        #TODO: Figure out how to display objects
        return f'Cup {number}: {value} seeds'

class KalahGame:
    def __init__(self):
        self.state = {
            "board": self.GenerateInitialBoardState(),
            "possibleMoves": [1, 2, 3, 4],
            "score": [0, 0]
        }

    def GenerateInitialBoardState(self):
        cups = []
        type = 0
        for i in range(1,11):
            if i == 5 or i == 10:
                type = 1
            cups.append(Cup(type=type,
                            value=4,
                            number=i,
                            nextCup=(i+1)%10,
                            captureCup=10-i))
        return cups

    def MakeMove(self, move):
        #TODO: Capturing
        #TODO: Consecutive moves
        #TODO: Generate Possible Moves
        if move in self.state["possibleMoves"]:
            seeds = self.state["board"][move-1].value
            nextCup = self.state["board"][move-1].nextCup
            self.state["board"][move-1].Harvest()

            while seeds > 0:
                if move < 5 and nextCup == 10:
                    nextCup = 1
                elif move > 5 and nextCup == 5:
                    nextCup = 6
                else:
                    self.state["board"][nextCup - 1].Sow()
                    nextCup = self.state["board"][nextCup - 1].nextCup
                    seeds = seeds - 1

#Testing
cup = KalahGame()
print(str(cup.state["board"][0]))
