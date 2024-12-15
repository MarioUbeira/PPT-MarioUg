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
        
    def calculate_markov_matrix(self):
        """
        Constrúe unha matriz de transición baseada no historial do CSV.
        """
        self.markov_matrix = {action: Counter() for action in GameAction}

        with open(self.csv_file, mode="r", newline="", encoding="utf-8") as file:
            reader = csv.reader(file)
            next(reader)
            previous_move = None
            for row in reader:
                user_move = GameAction(int(row[0]))
                if previous_move is not None:
                    self.markov_matrix[previous_move][user_move] += 1
                previous_move = user_move

    def predict_next_move(self):
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
        if len(moves) < 4:
            return None

        for cycle in range(2, 4):
            if moves[-cycle:] == moves[-2 * cycle:-cycle]:
                return moves[-cycle]

        return None
        
    def get_computer_action(self):
        """
        Predí o seguinte movemento do usuario rexistrado baseado en diferentes estratexias a
        partires do seu historial.
        1º- Se o Axente no conta con suficiente información actuará de forma aleatoria.
        2º- Se o Axente detecta algún patrón, como ciclos (2>1>0>2>...) ou repeticións (1>1>1>...),
        busca contraatacar o seguinte movemento do patrón.
        2.1º- Se o Axente conta con suficiente información pero non atopa ningún patrón baseará o seu
        seguinte movemento na cadéa de Markov e nos porcentaxes de cada movemento do usuario.
        Compara o movemento esperado segundo Markov co movemento con maior porcentaxe de uso, se coinciden
        contraataca a ese movemento, e se non compara co segundo máis empregado.
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

        cyclic_move = self.detect_cyclic_pattern(last_moves)
        if cyclic_move is not None:
            return random.choice(Defeats[cyclic_move])

        if len(set(last_moves[-3:])) == 1:
            return random.choice(Defeats[last_moves[-1]])

        user_percentages = self.calculate_user_percentages()
        most_used_move = GameAction[ max(user_percentages, key=user_percentages.get) ]
        second_most_used_move = GameAction[ sorted(user_percentages, key=user_percentages.get, reverse=True)[1] ]

        predicted_user_move = self.predict_next_move()

        counter_most_used = random.choice(Victories[most_used_move])
        counter_predicted = random.choice(Victories[predicted_user_move])

        if counter_most_used == counter_predicted:
            return counter_most_used
        elif second_most_used_move == counter_predicted:
            return second_most_used_move
        else: 
            return counter_most_used




