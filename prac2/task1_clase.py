import numpy as np
import matplotlib.pyplot as plt

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

def graficar(x, n):
    fig, axs = plt.subplots(1, 1, figsize=(5, 4))
    axs.plot(n, x, 'b-', label="Sn")
    axs.set_title('Señales Sn y tn')
    axs.set_xlabel('n')
    axs.set_ylabel('func')
    axs.legend()

    plt.tight_layout()
    plt.show()
    return None

results = rampa(0, -10, 10)
print(results[0])
graficar(results[0], results[1])
