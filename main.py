import matplotlib.pyplot as plt
import numpy as np

DOT_SIZE = 4

def sequence(k: int):
    return k

def hamonic_sequence(k: int):
    return 1/k

def p_sequence(k: int):
    p = 2
    return 1 / (k**p)

def series(seq: callable, a: int, b: int):
    start = a
    end = b
    if a > b:
        start = b
        end = a
        
    s = 0
    for i in range(start, end + 1):
        s += seq(i)

    return s

def getArray(seq: callable, a: int, b: int):
    start = a
    end = b
    if a > b:
        start = b
        end = a

    # store data for sequence and series
    s = 0
    seqArray = []
    seriesArray = []
    for i in range(start, end + 1):
        ai = seq(i)
        s += ai

        seriesArray.append(s)
        seqArray.append(ai)

    return (seqArray, seriesArray)

def plot_one(seq: callable, a: int, b: int):
    start = a
    end = b
    if a > b:
        start = b
        end = a

    # prepare info for graph
    x = np.linspace(start, end, (end - start) + 1)

    y = getArray(seq, start, end) # tuple for both array sequence and array series
    y_sequence = np.array(y[0])
    y_series = np.array(y[1])

    # plot
    plt.scatter(x, y_sequence, color = "red", label = "Sequences", s = DOT_SIZE)
    plt.scatter(x, y_series, color = "blue", label = "Series", s = DOT_SIZE)
    plt.legend()
    plt.show()


plot_one(p_sequence, 1, 100)