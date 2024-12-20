import csv
import os
import random
from collections import Counter
from rules import GameAction, Victories, Defeats

class PredictAgent:
    def __init__(self):
        if not os.path.exists("data"):
            os.makedirs("data")
        self.csv_file = None
        self.markov_matrix = {action: Counter() for action in GameAction}
        
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
            
    def counter_move_percentages(self):
        """
        Calcula as porcentaxes de uso de cada acción por parte do usuario rexistrado e
        devolve a máis empregada.
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
            return random.choice(list(GameAction))

        most_used_action = max(user_moves_counter, key=user_moves_counter.get)

        if most_used_action == GameAction.Rock:
            return GameAction.Paper
        elif most_used_action == GameAction.Paper:
            return GameAction.Scissors
        elif most_used_action == GameAction.Scissors:
            return GameAction.Rock

        return random.choice(list(GameAction))
        
    def calculate_markov_matrix(self):
        """
        Constrúe unha matriz de transición baseada no historial do CSV.
        """
        with open(self.csv_file, mode="r", newline="", encoding="utf-8") as file:
            reader = csv.reader(file)
            next(reader)
            previous_move = None
            for row in reader:
                user_move = GameAction(int(row[0]))
                if previous_move is not None:
                    self.markov_matrix[previous_move][user_move] += 1
                previous_move = user_move

    def predict_next_move_markov(self):
        """
        Devolve o máis probable seguinte movemento do usuario baseado na cadéa de Markov.
        https://es.wikipedia.org/wiki/Cadena_de_Márkov
        """
        self.calculate_markov_matrix()
        
        total_transitions = sum(sum(counter.values()) for counter in self.markov_matrix.values())
        if total_transitions == 0:
            return random.choice(list(GameAction))
        
        with open(self.csv_file, mode="r", newline="", encoding="utf-8") as file:
            reader = csv.reader(file)
            next(reader)
            last_move = None
            for row in reader:
                last_move = GameAction(int(row[0]))

        if last_move is None or not self.markov_matrix[last_move]:
            return random.choice(list(GameAction))

        predicted_move = max(self.markov_matrix[last_move], key=self.markov_matrix[last_move].get)
        return predicted_move

    def detect_cyclic_pattern(self, moves):
        """
        Detecta patróns cíclicos nos movementos do usuario.
        Devolve o próximo movemento esperado se se detecta un patrón.
        """
        with open(self.csv_file, mode="r", newline="", encoding="utf-8") as file:
            reader = csv.reader(file)
            next(reader)
            moves = [GameAction(int(row[0])) for row in list(reader)[-10:]]

        if len(moves) < 4:
            return None

        for cycle in range(2, 4):
            if moves[-cycle:] == moves[-2 * cycle:-cycle]:
                return moves[-cycle]

        return None
        
    def get_computer_action(self):
        """
        Asigna a cada posible estratexia un peso e selecciona unha delas
        pseudoaleatoriamente en base a iso.
        """
        if not os.path.exists(self.csv_file):
            return random.choice(list(GameAction))

        with open(self.csv_file, mode="r", newline="", encoding="utf-8") as file:
            reader = csv.reader(file)
            next(reader)
            last_moves = []
            for row in reader:
                last_moves.append(GameAction(int(row[0])))
                if len(last_moves) > 5:
                    last_moves.pop(0)

        strategies = [
            lambda: self.predict_next_move_markov(),
            lambda: self.detect_cyclic_pattern(last_moves) or random.choice(list(GameAction)),
            lambda: self.counter_move_percentages(),
        ]
        selected_strategy = random.choices(strategies, weights=[0.375, 0.375, 0.25])[0]
        return selected_strategy()




