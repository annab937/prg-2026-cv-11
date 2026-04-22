import random

def random_numbers(count, low=0, high=100):
    return [random.randint(low, high) for _ in range(count)]


def selection_sort(sequence):
    sequence = sequence[:]

    n = len(sequence)
    for i in range(n):
        min_index = i

        for j in range(i + 1, n):
            if sequence[j] < sequence[min_index]:
                min_index = j
        sequence[i], sequence[min_index] = sequence[min_index], sequence[i]

    return sequence


def main():
    sequence = random_numbers(20, low=0, high=100)
    sorted_sequence = selection_sort(sequence)
    print(sequence)
    print(sorted_sequence)




if __name__ == "__main__":
    main()



