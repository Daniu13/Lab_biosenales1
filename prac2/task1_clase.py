import numpy as np

def impulso(n0, n1, n2):
    n = np.arange(n1, n2 + 1)
    x = (n == n0).astype(int)
    return x, n

def escalon(n0, n1, n2):
    n = np.arange(n1, n2 + 1)
    x = (n >= n0).astype(int)
    return x, n

def rampa(n0, n1, n2):
    n = np.arange(n1, n2 + 1)
    x = (n >= n0).astype(int)
    x = np.concatenate([np.zeros(len(x[x == 0]), dtype=int, order='C'),
                       np.arange(0, len(x[x != 0]), dtype=int)])
    return x, n

results = rampa(0, -10, 10)
print(results[0])
