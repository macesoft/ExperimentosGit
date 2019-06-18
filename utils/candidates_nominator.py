from pathlib import Path
from fileinput import FileInput
import random


class CandidatesNominator:
    candidates_playing_list = []

    def __init__(self, file_pathname):
        try:
            candidates_path = Path(file_pathname)
            file_descriptor = FileInput(candidates_path)

            candidate = file_descriptor.readline()
            while len(str(candidate)) > 0:
                self.candidates_playing_list.append(str(candidate).strip('\n'))
                candidate = file_descriptor.readline()
            file_descriptor.close()
        except FileNotFoundError:
            print("Unable to process the file")
            exit(1)

    def choose_candidate(self):
        candidate_chosen = random.choice(self.candidates_playing_list)
        self.candidates_playing_list.remove(candidate_chosen)
        return candidate_chosen

    def show_results(self, number_of_winners):
        for winner_pos in range(1, int(number_of_winners) + 1):
            winner_name = self.choose_candidate()
            print(f"Winner #{winner_pos}: {winner_name}")

        print(f"\nRemaining losers: {self.candidates_playing_list}")


# -----------------------------------------------------------------------------
