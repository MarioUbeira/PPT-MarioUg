from rules import GameAction, assess_game
from agent import PredictAgent
from user import get_user_action, play_another_round

def main():
    predictin = PredictAgent()
    
    while True:
        try:
            user_action = get_user_action()
        except ValueError:
            range_str = f"[0, {len(GameAction) - 1}]"
            print(f"Invalid selection. Pick a choice in range {range_str}!")
            continue
        
        predictin.last_matches(user_action)
        computer_action = predictin.predict()
        assess_game(user_action, computer_action)

        if not play_another_round():
            break


if __name__ == "__main__":
    main()
