from rules import GameAction, assess_game
from agent import PredictAgent
from user import get_user_action

def main():
    predictin = PredictAgent()
    
    while True:
        try:
            user_action = get_user_action()
        except ValueError:
            range_str = f"[0, {len(GameAction) - 1}]"
            print(f"Elección invalida. Escolle unha opción no rango {range_str}!")
            continue
        
        predictin.last_matches(user_action)
        computer_action = predictin.predict()
        result = assess_game(user_action, computer_action)
        predictin.last_match = result

        if user_action.value == 3:
            print(f"Partida rematada, grazas por xogar.")
            break


if __name__ == "__main__":
    main()
