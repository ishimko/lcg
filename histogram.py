import matplotlib.pyplot as plt

RANGES_COUNT = 20

def draw_histogram(numbers):
    weights = [1/len(numbers)]*len(numbers)
    frequency, _, _ = plt.hist(
        numbers,
        bins=RANGES_COUNT,
        weights=weights,
        edgecolor='black',
        linewidth=1
    )
    print(frequency)
    plt.show()
