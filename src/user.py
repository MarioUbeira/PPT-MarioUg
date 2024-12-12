from rules import GameAction

TRANSLATIONS = {
    "Rock": "Pedra",
    "Paper": "Papel",
    "Scissors": "Tesoiras",
    "Exit": "Saír"
}

def get_user_action():
    # Scalable to more options (beyond rock, paper and scissors...)
    game_choices = [f"{TRANSLATIONS.get(game_action.name, game_action.name)}[{game_action.value}]" for game_action in GameAction]
    game_choices_str = ", ".join(game_choices)
    user_selection = int(input(f"\nEscolle ({game_choices_str}): "))
    user_action = GameAction(user_selection)

    return user_action