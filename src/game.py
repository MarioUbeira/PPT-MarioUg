from colorama import Fore
from rules import GameAction, GameResult
import csv
import matplotlib.pyplot as plt
from collections import Counter
import seaborn as sns

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

def postgame_stats(user):
    """
    Xera gráficas separadas que amosan a eficacia do axente contra o usuario rexistrado.
    """
    csv_file = f"data/{user}.csv"
    games = []
    winrate_per_game = []
    agent_win = 0
    draw = 0
    total_games = 0

    agent_moves_counter = Counter()
    result_counter = Counter()

    with open(csv_file, mode="r", newline="", encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            total_games += 1
            user_move = GameAction(int(row[0]))
            agent_move = GameAction(int(row[1]))
            result = int(row[2])

            if result == 1:
                agent_win += 1
            elif result == 2:
                draw += 1

            agent_moves_counter[agent_move] += 1
            result_counter[result] += 1

            win_or_loss_matches = total_games - draw
            winrate = (agent_win / win_or_loss_matches) * 100 if total_games > 0 else 0
            games.append(total_games)
            winrate_per_game.append(winrate)

    if not games:
        return

    sns.set_theme(style="whitegrid")
    plt.rcParams['axes.facecolor'] = '#0E4D80'
    plt.rcParams['figure.facecolor'] = '#0E4D80'

    plt.figure(figsize=(8, 5))
    plt.plot(games, winrate_per_game, marker="o", color="#F08C00", linewidth=2.5, markersize=6)
    plt.title(f"Rendemento do Axente vs {user.capitalize()}", fontsize=18, fontweight="bold", color="#C2255C", pad=20)
    plt.xlabel(f"Número de partidas xogadas ({total_games})", fontweight="bold", fontsize=14, color="#12B886", labelpad=15)
    plt.ylabel(f"Porcentaxe de victorias* ({winrate_per_game[-1]:.2f}%)", fontweight="bold", fontsize=14, color="#12B886", labelpad=15)
    plt.text(0.95, 0.95, f'Partidas - {total_games}\nVictorias - {agent_win}', fontsize=9, color="#12B886", 
         ha='right', va='top', transform=plt.gca().transAxes, fontweight='bold', 
         bbox=dict(facecolor='black', alpha=0.3, edgecolor='none', boxstyle='round,pad=0.5'))
    plt.text(-0.10, -0.20, "*Sobre o total de partidas gañadas\nou perdidas, despreciando empates.", fontsize=8, color="#E8590C", 
         ha='left', va='bottom', transform=plt.gca().transAxes)
    plt.tick_params(axis='x', colors='#E8590C')
    plt.tick_params(axis='y', colors='#E8590C')
    plt.xlim(0, max(games))
    plt.ylim(0, 100)
    plt.tight_layout()
    plt.show()

    plt.figure(figsize=(8, 5))
    result_labels = ['Victorias', 'Derrotas', 'Empates']
    result_percentages = [
        (result_counter[GameResult.Defeat] / total_games) * 100,
        (result_counter[GameResult.Victory] / total_games) * 100,
        (result_counter[GameResult.Tie] / total_games) * 100
    ]
    plt.bar(result_labels, result_percentages, color=['green', 'red', 'gray'])
    plt.title("Distribución de Resultados", fontsize=14, fontweight="bold", color="#C2255C")
    plt.ylabel("Porcentaxe", fontsize=12, color="#12B886")
    plt.tick_params(axis='x', colors='#E8590C')
    plt.tick_params(axis='y', colors='#E8590C')
    plt.tight_layout()
    plt.show()

    plt.figure(figsize=(8, 5))
    agent_move_labels = ['Pedra', 'Papel', 'Tesoiras']
    agent_move_percentages = [
        (agent_moves_counter[GameAction.Rock] / total_games) * 100,
        (agent_moves_counter[GameAction.Paper] / total_games) * 100,
        (agent_moves_counter[GameAction.Scissors] / total_games) * 100
    ]
    plt.pie(agent_move_percentages, labels=agent_move_labels, autopct='%1.1f%%', startangle=90, colors=["#F08C00", "#F0D100", "#12B886"])
    plt.title("Distribución de movementos do Axente", fontsize=14, fontweight="bold", color="#C2255C")
    plt.axis('equal')
    plt.tight_layout()
    plt.show()