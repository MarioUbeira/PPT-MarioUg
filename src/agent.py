from rules import GameAction, GameResult, Victories, Defeats
from patterns import PATTERNS
import random

class PredictAgent:
    def __init__(self):
        self.user_moves = []
        self.patterns = PATTERNS
        self._last_match = None
        
    @property
    def last_match(self):
        """
        Getter para o último resultado.
        """
        return self._last_match

    @last_match.setter
    def last_match(self, result):
        """
        Setter para actualizar o último resultado.
        """
        self._last_match = result

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
        if len(self.user_moves) == 0:
            return random.choice(list(GameAction))
        
        ted_kaczynski = self.pattern_detecter() # Ted Kaczynski e o meu patrón
        
        if ted_kaczynski:
            print("Patrón detectado")
        elif self.last_match == GameResult.Victory:
            last_move = self.user_moves[-1]
            next_move = Victories[last_move][0]
        elif self.last_match == GameResult.Defeat:
            last_move = self.user_moves[-1]
            if last_move == GameAction.Rock:
                next_move = GameAction.Scissors
            elif last_move == GameAction.Paper:
                next_move = GameAction.Rock
            else:
                next_move = GameAction.Paper 
        else:
            next_move = random.choice(list(GameAction))
        return next_move
            