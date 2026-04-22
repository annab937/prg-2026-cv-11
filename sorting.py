import random
import matplotlib.pyplot as plt

def random_numbers(count, low=0, high=100):
    return [random.randint(low, high) for _ in range(count)]

#Selection Sort
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

#Bubble Sort
def bubble_sort(sequence):
    plt.ion()
    plt.show()
    sequence = sequence[:]
    n = len(sequence)

    for i in range(n - 1):
        for j in range(n - 1 - i):
            if sequence[j] > sequence[j + 1]:
                index_highlight1 = j
                index_highlight2 = j + 1
                colors = ["steelblue"] * len(sequence)
                colors[index_highlight1] = "tomato"
                colors[index_highlight2] = "tomato"
                plt.clf()
                plt.bar(range(len(sequence)), sequence, color=colors)
                plt.title("Bubble Sort")
                plt.pause(0.1)
                sequence[j], sequence[j + 1] = sequence[j + 1], sequence[j]
    plt.ioff()
    plt.show()
    return sequence

#


def main():
    sequence = random_numbers(20, low=0, high=100)
    sorted_sequence = bubble_sort(sequence)
    print(sequence)
    print(sorted_sequence)




if __name__ == "__main__":
    main()



