import csv
import os
from rules import GameAction, GameResult, Victories, Defeats
import random

class PredictAgent:
    def __init__(self):
        self.user_moves = []
        self._last_match = None
        self.last_agent_move = None
        
    def create_csv(self, player):
        """
        Crea dinámicamente un arquivo CSV para cada xogador.
        """
        if not os.path.exists("data"):
            os.makedirs("data")
            
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

    def last_matches(self, user_move):
        """
        Rexistra o historial de partidas.
        """
        if self.csv_file is None:
            self.csv_file = "data/default.csv"
            
        with open(self.csv_file, mode="a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow([user_move, self.last_agent_move, self._last_match])
            
    def predict(self):
        """
        Predí o seguinte movemento do usuario baseado no historial de partidas (last_matches), cando
        non atopa este patrón actúa en función do resultado da última partida. 
        """
        if len(self.user_moves) == 0:
            return random.choice(list(GameAction))  
        
        last_move = self.user_moves[-1]   
        if self.last_match == GameResult.Tie:
            self.last_agent_move = random.choice(list(GameAction))
        elif self.last_match == GameResult.Victory:
            self.last_agent_move = random.choice(list(GameAction))
        else:
            self.last_agent_move = random.choice(list(GameAction))

        return self.last_agent_move