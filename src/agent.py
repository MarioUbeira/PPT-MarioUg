import csv
import os
from rules import GameAction, GameResult, Victories, Defeats
import random

class PredictAgent:
    def __init__(self):
        self.user_moves = []
        
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

    def last_matches(self, user_move, computer_action, result):
        """
        Rexistra o historial de partidas.
        """
        if self.csv_file is None:
            self.csv_file = "data/default.csv"
            
        with open(self.csv_file, mode="a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow([user_move, computer_action, result])
            
    def predict(self, last_move):
        """
        Predí o seguinte movemento do usuario baseado no historial de partidas (last_matches), cando
        non atopa este patrón actúa en función do resultado da última partida. 
        """
        if last_move == 0:
            return random.choice(list(GameAction))  

        if last_move == GameResult.Tie:
            agent_move = random.choice(list(GameAction))
        elif last_move == GameResult.Victory:
            agent_move = random.choice(list(GameAction))
        else:
            agent_move = random.choice(list(GameAction))

        return agent_move