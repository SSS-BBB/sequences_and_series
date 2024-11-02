import matplotlib.pyplot as plt
import numpy as np
import math

DOT_SIZE = 4

def sequence(k: int):
    return k

def hamonic_sequence(k: int):
    return 1/k

def p_sequence(k: int):
    p = 2
    return 1 / (k**p)

def cosfact_sequence(k: int):
    return math.cos(k) / math.factorial(k)

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


def plot_compare(seq_dict: dict, a: int, b: int):
    start = a
    end = b
    if a > b:
        start = b
        end = a

    # prepare info for graph
    x = np.linspace(start, end, (end - start) + 1)

    # get info from every seq in the container
    y_sequence_container = {}
    y_series_container = {}
    for seq_name, seq in seq_dict.items():
        y = getArray(seq, start, end)
        y_sequence_container[seq_name] = np.array(y[0])
        y_series_container[seq_name] = np.array(y[1])

    # plot info
    figure, axis = plt.subplots(1, 2) # 1 row 2 columns

    # plot sequence (axis[0])
    axis[0].set_title("Sequences Compare")

    # plot series (axis[1])
    axis[1].set_title("Series Compare")

    for seq_name in seq_dict.keys():
        axis[0].scatter(x, y_sequence_container[seq_name], label = seq_name + " Sequence", s = DOT_SIZE)
        axis[1].scatter(x, y_series_container[seq_name], label = seq_name + " Series", s = DOT_SIZE)

    axis[0].legend()
    axis[1].legend()
    plt.show()


plot_compare({"Hamonic": hamonic_sequence, "P": p_sequence, "CosFact": cosfact_sequence}, 1, 50)