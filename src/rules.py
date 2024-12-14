from enum import IntEnum

class GameAction(IntEnum):

    Rock = 0
    Paper = 1
    Scissors = 2


class GameResult(IntEnum):
    Victory = 0
    Defeat = 1
    Tie = 2

Victories = {
    GameAction.Rock: [GameAction.Scissors],
    GameAction.Paper: [GameAction.Rock],
    GameAction.Scissors: [GameAction.Paper]
}

Defeats = {
    GameAction.Rock: [GameAction.Paper],
    GameAction.Paper: [GameAction.Scissors],
    GameAction.Scissors: [GameAction.Rock]
}