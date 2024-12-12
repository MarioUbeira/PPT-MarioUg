from rules import GameAction
from colorama import Fore

TRANSLATIONS = {
    "Rock": "Pedra",
    "Paper": "Papel",
    "Scissors": "Tesoiras",
    "Exit": "Saír"
}

def get_user_action():
    
    colors = {
        "Rock": Fore.MAGENTA,
        "Paper": Fore.CYAN,
        "Scissors": Fore.MAGENTA,
        "Exit": Fore.YELLOW
    }
    # Scalable to more options (beyond rock, paper and scissors...)
    game_choices = [f"{colors.get(game_action.name, Fore.WHITE)}{TRANSLATIONS.get(game_action.name, game_action.name)}[{game_action.value}{Fore.RESET}]" for game_action in GameAction]
    game_choices_str = Fore.WHITE + ", ".join(game_choices)
    user_selection = int(input(f"\nEscolle ({game_choices_str}): "))
    user_action = GameAction(user_selection)

    return user_action