from rules import GameAction
from colorama import Fore

TRANSLATIONS = {
    "Rock": "Pedra",
    "Paper": "Papel",
    "Scissors": "Tesoiras",
    "Exit": "Saír"
}

def get_user():
    while True:
        player = input(Fore.MAGENTA + f"Introduce o teu nome (Máx 15 caracteres): {Fore.RESET}").strip()
        if not player:
            print(Fore.RED + "O nome non pode quedar baleiro. Ténteo de novo.")
            continue
        player = player.lower().replace(" ", "_")
        if len(player) > 15:
            print(Fore.RED + "O nome non pode ter máis de 15 caracteres. Ténteo de novo.")
            continue
        return player
    
def get_user_action():
    
    colors = {
        "Rock": Fore.MAGENTA,
        "Paper": Fore.CYAN,
        "Scissors": Fore.MAGENTA,
    }
    # Scalable to more options (beyond rock, paper and scissors...)
    game_choices = [f"{colors.get(game_action.name, Fore.WHITE)}{TRANSLATIONS.get(game_action.name, game_action.name)}[{game_action.value}{Fore.RESET}]" for game_action in GameAction]
    game_choices_str = Fore.WHITE + ", ".join(game_choices)
    while True:
            try:
                user_selection = int(input(f"\nEscolle ({game_choices_str}, {Fore.YELLOW}Saír[3]{Fore.RESET}): "))
                if user_selection >= 0 and user_selection <= 2:
                    user_action = GameAction(user_selection)
                    return user_action
                elif user_selection == 3:
                    return None
                else:
                    print(Fore.RED + "Introduce un número entre 1 e 3, pailán." + Fore.RESET)
            except ValueError:
                print(Fore.RED + "Introduce un número entre 1 e 3, pailán." + Fore.RESET)