from rules import GameAction
import random

class PredictAgent:
    def __init__(self):
        self.user_moves = []

    def last_matches(self, move):
        """
        Rexistra o movemento do usuario.
        """
        self.user_moves.append(move)

    def predict(self):
        """
        Predí o seguinte movemento do usuario baseado no historial de partidas (last_matches) cando
        este teña un mínimo de 10 partidas rexistradas, mentres non as teña actuará aleatoriamente. 
        """
        if len(self.user_moves) < 10:
            return random.choice(list(GameAction))
        return random.choice(list(GameAction)) #Aquí ira a "intelixencia" do axente