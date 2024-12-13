from rules import GameAction, assess_game
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
            user_action = get_user_action()

            if user_action is None:
                print(Fore.YELLOW + f"Partida rematada, grazas por xogar.")
                break

            computer_action = predictin.predict()
            result = assess_game(user_action, computer_action)
            predictin.last_matches(user_action, computer_action, result)
            # print(predictin.calculate_user_percentages())
        except ValueError:
            range_str = f"[0, {len(GameAction) - 1}]"
            print(Fore.RED + f"Elección invalida. Escolle unha opción no rango {range_str}!")
            continue

if __name__ == "__main__":
    main()
