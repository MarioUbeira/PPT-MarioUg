from colorama import Fore
from rules import GameAction, GameResult
import csv

def assess_game(user_action, computer_action):

    game_result = None

    if user_action == computer_action:
        print(Fore.BLUE + f"Xogador e axente escolleron {user_action.name}. Partida empatada!")
        game_result = GameResult.Tie

    # You picked Rock
    elif user_action == GameAction.Rock:
        if computer_action == GameAction.Scissors:
            print(Fore.GREEN + "Pedra aplasta Tesoiras. Gañaches!")
            game_result = GameResult.Victory
        else:
            print(Fore.RED + "Papel cubre pedra. Perdiches!")
            game_result = GameResult.Defeat

    # You picked Paper
    elif user_action == GameAction.Paper:
        if computer_action == GameAction.Rock:
            print(Fore.GREEN + "Papel cubre pedra. Gañaches!")
            game_result = GameResult.Victory
        else:
            print(Fore.RED + "Tesoiras cortan papel. Perdiches!")
            game_result = GameResult.Defeat

    # You picked Scissors
    elif user_action == GameAction.Scissors:
        if computer_action == GameAction.Rock:
            print(Fore.RED + "Pedra aplasta Tesoiras. Perdiches!")
            game_result = GameResult.Defeat
        else:
            print(Fore.GREEN + "Tesoiras cortan papel. Gañaches!")
            game_result = GameResult.Victory

    return game_result

def aggregate(player_name):
    """
    Devolve a cantidade de victorias de cada participante.
    """
    player_wins = 0
    agent_wins = 0

    csv_file = f"data/{player_name}.csv"

    with open(csv_file, mode="r", newline="", encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            result = int(row[2])
            if result == 0:
                player_wins += 1
            elif result == 1:
                agent_wins += 1
                
    return player_wins, agent_wins

def draw_scoreboard(user, player_wins, agent_wins):
    """
    Debuxa o marcador.
    """
    if player_wins > agent_wins:
        user_color = Fore.GREEN
        agent_color = Fore.RED
    elif agent_wins > player_wins:
        user_color = Fore.RED
        agent_color = Fore.GREEN
    else:
        user_color = Fore.BLUE
        agent_color = Fore.BLUE
    
    print(Fore.LIGHTBLACK_EX + "*" * 50)
    print(f"{' ' * 10}{Fore.LIGHTYELLOW_EX}TÁBOA DE RESULTADOS{Fore.RESET}{' ' * 10}")
    print(f"{' ' * 5}{user_color}{user.capitalize()} → {player_wins}{Fore.RESET}  -----  {agent_color}{agent_wins} ← Axente")
    print(Fore.LIGHTBLACK_EX + "*" * 50)