import os
import time
from rules import GameAction
from game import assess_game, aggregate, draw_scoreboard, postgame_stats
from agent import PredictAgent
from agent_rpsls import PredictAgentRPSLS
from user import get_user, get_game_choice, get_user_action
from colorama import init, Fore

init(autoreset=True)

def main():
    predictin = PredictAgent()
    super_predictin = PredictAgentRPSLS()
    user = get_user()
    game_mode = get_game_choice()
    if game_mode is None:
        print(Fore.YELLOW + "Sesión rematada. Grazas por xogar!")
        return
    
    predictin.create_csv(user) if game_mode == 0 else super_predictin.create_csv(user)   
    result = 0
    agent = predictin if game_mode == 0 else super_predictin
    
    while True:
        try:
            os.system('cls' if os.name == 'nt' else 'clear')
            user_action = get_user_action(game_mode)
            if user_action is None:
                print(Fore.YELLOW + f"Partida rematada. Grazas por xogar!")
                postgame_stats(user, game_mode)
                break

            computer_action = agent.get_computer_action()
            result = assess_game(user_action, computer_action)
            agent.last_matches(user_action, computer_action, result)
            # Marcador
            player_wins, agent_wins = aggregate(user, game_mode)
            draw_scoreboard(user, player_wins, agent_wins)
            time.sleep(1.5)
            
        except ValueError:
            range_str = f"[0, {len(GameAction) - 1}]"
            print(Fore.RED + f"Elección invalida. Escolle unha opción no rango {range_str}!")
            continue

if __name__ == "__main__":
    main()
