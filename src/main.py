import os
import time
from rules import GameAction
from game import assess_game, aggregate, draw_scoreboard, postgame_stats
from agent import PredictAgent
from user import get_user, get_user_action
from colorama import init, Fore

init(autoreset=True) #just_fix_windows_console() no me funciona

def main():
    predictin = PredictAgent()
    user = get_user()
    predictin.create_csv(user)
    result = 0
    while True:
        try:
            os.system('cls' if os.name == 'nt' else 'clear')
            user_action = get_user_action()

            if user_action is None:
                print(Fore.YELLOW + f"Partida rematada, grazas por xogar.")
                postgame_stats(user)
                break

            computer_action = predictin.get_computer_action()
            result = assess_game(user_action, computer_action)
            predictin.last_matches(user_action, computer_action, result)
            # Marcador
            player_wins, agent_wins = aggregate(user)
            draw_scoreboard(user, player_wins, agent_wins)
            time.sleep(1)
            
        except ValueError:
            range_str = f"[0, {len(GameAction) - 1}]"
            print(Fore.RED + f"Elección invalida. Escolle unha opción no rango {range_str}!")
            continue

if __name__ == "__main__":
    main()
