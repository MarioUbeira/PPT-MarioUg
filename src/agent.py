from rules import GameAction
from patterns import PATTERNS
import random

class PredictAgent:
    def __init__(self):
        self.user_moves = []
        self.patterns = PATTERNS

    def last_matches(self, move):
        """
        Rexistra o historial de partidas.
        """
        self.user_moves.append(move)
        
    def pattern_detecter(self):
        """
        Encargarase de detectar patróns no historial de partidas en base a un diccionario de posibles patróns.
        """
        if len(self.user_moves) < 10:
            return None
        for pattern in self.patterns:
            return pattern
        return None

    def predict(self):
        """
        Predí o seguinte movemento do usuario baseado no historial de partidas (last_matches) cando
        este teña un mínimo de 10 partidas rexistradas, mentres non as teña actuará aleatoriamente. 
        """
        if len(self.user_moves) < 10:
            return random.choice(list(GameAction))
        return random.choice(list(GameAction)) #Aquí ira a "intelixencia" do axente