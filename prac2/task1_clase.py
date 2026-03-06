import numpy as np
import matplotlib.pyplot as plt

def graficar(x, n):
    fig, axs = plt.subplots(1, 1, figsize=(5, 4))
    axs.stem(n, x, 'b-', label="Sn")
    axs.set_title('Señales Sn y tn')
    axs.set_xlabel('n')
    axs.set_ylabel('func')
    axs.legend()

    plt.tight_layout()
    plt.show()
    return None

#FUNCIONES QUE NOS PIDIERON

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

def exponencial(n0, n1, n2, sigma, omega_null):
    n = np.arange(n1, n2 + 1)
    x = np.exp((sigma + 1j * omega_null) * n)
    return x, n

def sinusoidal(n0, n1, n2, omega_null, theta_null):
    n = np.arange(n1, n2 + 1)
    x = np.sin(omega_null * n + theta_null)
    return x, n


#5
#A
impulsos = [(3, -1), (5, -3), (3, -2), (3, 0), (1, 0)] #Tuplas con amplitud y desfases
x1 = sum(amp * impulso(n0, -20, 20)[0] for amp, n0 in impulsos)
graficar(x1, impulso(0, -20, 20)[1])

#B
funciones = [
    (2, -3, rampa),
    (-1, 2, rampa),
    (-5, 3, escalon)
]
x4 = sum(amp * func(n0, -10, 10)[0] for amp, n0, func in funciones)

graficar(x4, impulso(0, -10, 10)[1])