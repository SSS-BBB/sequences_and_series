def sequence(k: int):
    return 1/k

def series(seq: callable, start: int, end: int):
    s = 0
    for i in range(start, end + 1):
        s += seq(i)

    return s

print(series(sequence, 1, 4))