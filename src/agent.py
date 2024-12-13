import csv
import os
from rules import GameAction, GameResult, Victories, Defeats
import random

class PredictAgent:
    def __init__(self):
        self.user_moves = None
        self._last_match = None
        
    def create_csv(self, player):
        """
        Crea dinámicamente un arquivo CSV para cada xogador.
        """
        self.csv_file = f"data/{player}.csv"
        if not os.path.exists(self.csv_file):
            with open(self.csv_file, mode="w", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)
                writer.writerow(["user_move","agent_move", "result"])
        
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

    def predict(self):
        """
        Predí o seguinte movemento do usuario baseado no historial de partidas (last_matches), cando
        non atopa este patrón actúa en función do resultado da última partida. 
        """
        if len(self.user_moves) == 0:
            return random.choice(list(GameAction))  
        last_move = self.user_moves[-1]   
        print(last_move)
        if self.last_match == GameResult.Tie:
            next_move = random.choice(list(GameAction))
        elif self.last_match == GameResult.Victory:
            next_move = Defeats[Defeats[last_move][0]][0]
        else:
            next_move = Victories[Victories[last_move][0]][0]

        return next_move