from rules import GameAction
from rules_rpsls import GameAction
from colorama import Fore

TRANSLATIONS = {
    "Rock": "Pedra",
    "Paper": "Papel",
    "Scissors": "Tesoiras",
    "Lizard": "Lagarto",
    "Spock": "Spock",
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
    
def get_game_choice():
    while True:
        try:
            game_choice = int(input(Fore.MAGENTA + f"Escolle o modo de xogo: RPS[0], RPSLS[1], Axuda[8], Saír[9]: {Fore.RESET}"))
            if game_choice == 0 or game_choice == 1:
                return game_choice
            elif game_choice == 8:
                print(f"""
                {Fore.YELLOW}ESCOLLE O MODO DE XOGO:{Fore.RESET}
                
                - {Fore.CYAN}RPS{Fore.RESET} (clásico): Inclúe só Pedra, Papel e Tesoiras.
                - {Fore.MAGENTA}RPSLS{Fore.RESET} (ampliación): Engade Lagarto e Spock ás opcións.
                
                {Fore.YELLOW}REGRAS BÁSICAS DE RPS E RPSLS:{Fore.RESET}

                - {Fore.CYAN}RPS{Fore.RESET} (Pedra, Papel, Tesoiras):
                1. {Fore.GREEN}Pedra{Fore.RESET} vence a {Fore.RED}Tesoiras{Fore.RESET}.
                2. {Fore.GREEN}Papel{Fore.RESET} vence a {Fore.RED}Pedra{Fore.RESET}.
                3. {Fore.GREEN}Tesoiras{Fore.RESET} vence a {Fore.RED}Papel{Fore.RESET}.

                - {Fore.MAGENTA}RPSLS{Fore.RESET} (Pedra, Papel, Tesoiras, Lagarto, Spock):
                1. {Fore.GREEN}Pedra{Fore.RESET} vence a {Fore.RED}Tesoiras{Fore.RESET} e {Fore.RED}Lagarto{Fore.RESET}.
                2. {Fore.GREEN}Papel{Fore.RESET} vence a {Fore.RED}Pedra{Fore.RESET} e {Fore.RED}Spock{Fore.RESET}.
                3. {Fore.GREEN}Tesoiras{Fore.RESET} vence a {Fore.RED}Papel{Fore.RESET} e {Fore.RED}Lagarto{Fore.RESET}.
                4. {Fore.GREEN}Lagarto{Fore.RESET} vence a {Fore.RED}Spock{Fore.RESET} e {Fore.RED}Papel{Fore.RESET}.
                5. {Fore.GREEN}Spock{Fore.RESET} vence a {Fore.RED}Tesoiras{Fore.RESET} e {Fore.RED}Pedra{Fore.RESET}.
                """)       
            elif game_choice == 9:
                return None
            else:
                print(Fore.RED + "Introduce 0 para RPS ou 1 para RPSLS.")
        except ValueError:
            print(Fore.RED + "Introduce 0 para RPS ou 1 para RPSLS." + Fore.RESET)
            
def get_user_action(game_choice):
    colors = {
        "Rock": Fore.MAGENTA,
        "Paper": Fore.CYAN,
        "Scissors": Fore.MAGENTA,
        "Lizard": Fore.CYAN,
        "Spock": Fore.MAGENTA,
    }

    if game_choice == 0:
        game_choices = [f"{colors.get(game_action.name, Fore.WHITE)}{TRANSLATIONS.get(game_action.name, game_action.name)}[{game_action.value}]{Fore.RESET}" 
                        for game_action in GameAction]
    elif game_choice == 1:
        game_choices = [f"{colors.get(game_action.name, Fore.WHITE)}{TRANSLATIONS.get(game_action.name, game_action.name)}[{game_action.value}]{Fore.RESET}" 
                        for game_action in GameAction]
    
    game_choices_str = Fore.WHITE + ", ".join(game_choices)
    
    while True:
        try:
            user_selection = int(input(f"\nEscolle ({game_choices_str}, {Fore.YELLOW}Saír[9]{Fore.RESET}): "))
            if 0 <= user_selection <= len(game_choices) - 1:
                if game_choice == 0:
                    user_action = GameAction(user_selection)
                else:
                    user_action = GameAction(user_selection)
                return user_action
            elif user_selection == 9:
                return None
            else:
                print(Fore.RED + "Introduce un número válido, pailán." + Fore.RESET)
        except ValueError:
            print(Fore.RED + "Introduce un número válido, pailán." + Fore.RESET)