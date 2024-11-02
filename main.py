import matplotlib.pyplot as plt
import numpy as np

def sequence(k: int):
    return k

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

    s = 0
    seqArray = []
    seriesArray = []
    for i in range(start, end + 1):
        ai = seq(i)
        s += ai

        seriesArray.append(s)
        seqArray.append(ai)

    return (seqArray, seriesArray)

print(getArray(sequence, 1, 5))