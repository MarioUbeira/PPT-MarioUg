from enum import IntEnum

class GameAction(IntEnum):

    Rock = 0
    Paper = 1
    Scissors = 2
    Exit = 3


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

def assess_game(user_action, computer_action):

    game_result = None

    if user_action == computer_action:
        print(f"Xogador e axente escolleron {user_action.name}. Partida empatada!")
        game_result = GameResult.Tie

    # You picked Rock
    elif user_action == GameAction.Rock:
        if computer_action == GameAction.Scissors:
            print("Pedra aplasta Tesoiras. Gañaches!")
            game_result = GameResult.Victory
        else:
            print("Papel cubre pedra. Perdiches!")
            game_result = GameResult.Defeat

    # You picked Paper
    elif user_action == GameAction.Paper:
        if computer_action == GameAction.Rock:
            print("Papel cubre pedra. Gañaches!")
            game_result = GameResult.Victory
        else:
            print("Tesoiras cortan papel. Perdiches!")
            game_result = GameResult.Defeat

    # You picked Scissors
    elif user_action == GameAction.Scissors:
        if computer_action == GameAction.Rock:
            print("Pedra aplasta Tesoiras. Gañaches!")
            game_result = GameResult.Defeat
        else:
            print("Tesoiras cortan papel. Gañaches!")
            game_result = GameResult.Victory

    return game_result