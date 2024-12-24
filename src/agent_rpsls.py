import csv
import os
import random
from collections import Counter, defaultdict
from rules_rpsls import GameAction, Victories, Defeats

class PredictAgentRPSLS:
    def __init__(self):
        if not os.path.exists("data"):
            os.makedirs("data")
        self.csv_file = None
        self.markov_matrix = defaultdict(lambda: defaultdict(int))
        
    def _read_csv(self):
        """
        Lee o arquivo csv.
        """
        with open(self.csv_file, mode="r", newline="", encoding="utf-8") as file:
            reader = csv.reader(file)
            next(reader)
            return [row for row in reader]
    
    def create_csv(self, player):
        """
         Crea dinámicamente un arquivo CSV para cada xogador.
        """
        self.csv_file = f"data/{player}_rpsls.csv"
        if not os.path.exists(self.csv_file):
            with open(self.csv_file, mode="w", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)
                writer.writerow(["user_move", "agent_move", "result"])

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
        rows = self._read_csv()
        for row in rows:
            user_move = GameAction(int(row[0]))
            user_moves_counter[user_move] += 1

        total_moves = sum(user_moves_counter.values())
        if total_moves == 0:
            return random.choice(list(GameAction))

        most_used_action = max(user_moves_counter, key=user_moves_counter.get)

        if most_used_action in Victories:
            return random.choice(Defeats[most_used_action])

        return random.choice(list(GameAction))

    def calculate_markov_matrix(self):
        """
         Constrúe unha matriz de transición baseada no historial do CSV.
        """
        rows = self._read_csv()
        previous_move = None
        for row in rows:
            user_move = GameAction(int(row[0]))
            if previous_move is not None:
                self.markov_matrix[previous_move][user_move] += 1
            previous_move = user_move

    def predict_next_move_markov(self):
        """
        Devolve o máis probable seguinte movemento do usuario baseado na cadéa de Markov.
        https://es.wikipedia.org/wiki/Cadena_de_Márkov
        """
        if not self.markov_matrix:
            self.calculate_markov_matrix()

        rows = self._read_csv()
        last_move = GameAction(int(rows[-1][0])) if rows else None

        if last_move is None or not self.markov_matrix[last_move]:
            return random.choice(list(GameAction))

        predicted_move = max(self.markov_matrix[last_move], key=self.markov_matrix[last_move].get)
        return random.choice(Defeats[predicted_move])

    def detect_cyclic_pattern(self, moves):
        """
        Detecta patróns cíclicos nos movementos do usuario.
        Devolve o próximo movemento esperado se se detecta un patrón.
        """
        
        if len(moves) < 3:
            return None

        for length in range(2, len(moves) // 2 + 1):
            for i in range(len(moves) - length):
                if moves[i:i+length] == [moves[i]] * length:
                    user_move = moves[i]
                    return random.choice(Defeats[user_move])

        for cycle_len in range(2, len(moves) // 2 + 1):
            for start in range(len(moves) - cycle_len):
                cycle = moves[start:start+cycle_len]
                for offset in range(start + cycle_len, len(moves) - cycle_len + 1):
                    if moves[offset:offset + cycle_len] == cycle:
                        user_move = moves[start]
                        return random.choice(Defeats[user_move])

        return None
        
    def get_computer_action(self):
        """
        Asigna a cada posible estratexia un peso e selecciona unha delas
        pseudoaleatoriamente en base a iso.
        """
        if not os.path.exists(self.csv_file):
            return random.choice(list(GameAction))

        rows = self._read_csv()
        last_moves = [GameAction(int(row[0])) for row in rows[-3:]]

        detected_pattern = self.detect_cyclic_pattern(last_moves)
        
        if detected_pattern is not None:
            return detected_pattern 

        strategies = [
            lambda: self.predict_next_move_markov(),
            lambda: self.counter_move_percentages(),
            lambda: random.choice(list(GameAction)),
        ]

        selected_strategy = random.choices(strategies, weights=[0.45, 0.45, 0.1])[0]
        return selected_strategy()