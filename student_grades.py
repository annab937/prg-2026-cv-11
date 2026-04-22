from sorting import random_numbers


class StudentsGrades:
    def __init__(self, scores):
        self.scores = scores

    def get_by_index(self, index):
        return self.scores[index]

    def count(self):
        return len(self.scores)

    def get_grades(self, index):
        score = self.get_by_index(index)
        if score < 50:
            return "F"
        elif 50 <= score <= 60:
            return "E"
        elif 60 <= score <= 70:
            return "D"
        elif 70 <= score <= 80:
            return "C"
        elif 80 <= score <= 90:
            return "B"
        else:
            return "A"


    def find(self, score):
        idx = 0
        positions = []
        searched_data = self.scores
        while idx < len(searched_data):
            if searched_data[idx] == score:
                positions.append(idx)
            idx += 1
        return positions

    def get_sorted(self):
            sequence = self.scores[:]
            n = len(sequence)

            for i in range(n - 1):
                for j in range(n - 1 - i):
                    if sequence[j] > sequence[j + 1]:
                        sequence[j], sequence[j + 1] = sequence[j + 1], sequence[j]
            return sequence



def main():
    results = StudentsGrades([85, 42, 91, 67, 50, 73, 100, 38, 58])
    print(f"Pocet studentu: {results.count()}")
    for student_id in range(results.count()):
        print(f"Student {student_id}: {results.get_by_index(student_id)} points – {results.get_grades(student_id)}")
    print(f"Plny pocet bodu meli studenti: {results.find(100)}")
    print(f"Serazene vysledky: {results.get_sorted()}")

    from sorting import random_numbers

    random_results = StudentsGrades(random_numbers(30, 0, 100))
    print(random_results.count())
    print(random_results.get_sorted())


if __name__ == "__main__":
    main()