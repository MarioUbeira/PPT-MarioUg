import csv
import os
import random
from collections import Counter
from rules import GameAction, GameResult, Victories, Defeats

class PredictAgent:
    def __init__(self):
        if not os.path.exists("data"):
            os.makedirs("data")
        self.csv_file = None
        
    def create_csv(self, player):
        """
        Crea dinámicamente un arquivo CSV para cada xogador.
        """
        self.csv_file = f"data/{player}.csv"
        if not os.path.exists(self.csv_file):
            with open(self.csv_file, mode="w", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)
                writer.writerow(["user_move","agent_move", "result"])

    def last_matches(self, user_move, computer_action, result):
        """
        Rexistra o historial de partidas.
        """
        with open(self.csv_file, mode="a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow([user_move, computer_action, result])
            
    def calculate_user_percentages(self):
        """
        Calcula as porcentaxes de uso de cada acción por parte do usuario rexistrado.
        """
        user_moves_counter = Counter()

        with open(self.csv_file, mode="r", newline="", encoding="utf-8") as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                user_move = GameAction(int(row[0]))
                user_moves_counter[user_move] += 1

        total_moves = sum(user_moves_counter.values())
        if total_moves == 0:
            return {action.name: 0.0 for action in GameAction}

        return {
            action.name: (user_moves_counter[action] / total_moves) * 100
            for action in GameAction
        }  
        
    def predict(self):
        """
        Predí o seguinte movemento do usuario rexistrado baseado no seu historial de partidas persoal. 
        """
        if not os.path.exists(self.csv_file):
            return random.choice(list(GameAction))
        
        user_percentages = self.calculate_user_percentages()
        if all(percentage == 0.0 for percentage in user_percentages.values()):
            return random.choice(list(GameAction))
        
        predicted_user_move = max(user_percentages, key=lambda x: user_percentages[x])
        predicted_user_move = GameAction[predicted_user_move]
        
        if predicted_user_move in Victories:
            agent_move = random.choice(Defeats[predicted_user_move])
        else:
              agent_move = random.choice(list(GameAction)) 
        
        return agent_move