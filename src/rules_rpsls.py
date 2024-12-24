from enum import IntEnum

class GameAction(IntEnum):

    Rock = 0
    Paper = 1
    Scissors = 2
    Lizard = 3
    Spock = 4
    
class GameResult(IntEnum):
    Victory = 0
    Defeat = 1
    Tie = 2

Victories = {
    GameAction.Rock: [GameAction.Scissors, GameAction.Lizard],
    GameAction.Paper: [GameAction.Rock, GameAction.Spock],
    GameAction.Scissors: [GameAction.Paper, GameAction.Lizard],
    GameAction.Lizard: [GameAction.Spock, GameAction.Paper],
    GameAction.Spock: [GameAction.Scissors, GameAction.Rock]
}

Defeats = {
    GameAction.Rock: [GameAction.Paper, GameAction.Spock],
    GameAction.Paper: [GameAction.Scissors, GameAction.Lizard],
    GameAction.Scissors: [GameAction.Rock, GameAction.Spock],
    GameAction.Lizard: [GameAction.Rock, GameAction.Scissors],
    GameAction.Spock: [GameAction.Paper, GameAction.Lizard]
}