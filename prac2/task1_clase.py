import numpy as np
import matplotlib.pyplot as plt

def graficar(senales, titulos=None):
    """
    senales: Lista de tuplas [(x1, n1), (x2, n2), ...]
    titulos: Lista de strings para cada subplot
    """
    num_graficos = len(senales)
    
    columnas = 2 if num_graficos > 1 else 1
    filas = (num_graficos + columnas - 1) // columnas
    
    fig, axs = plt.subplots(filas, columnas, figsize=(5 * columnas, 4 * filas), squeeze=False)
    axs = axs.flatten()

    for i in range(num_graficos):
        x, n = senales[i]
        axs[i].stem(n, x, 'b-', label=f"Señal {i+1}")
        
        if titulos and i < len(titulos):
            axs[i].set_title(titulos[i])
        
        axs[i].set_xlabel('n')
        axs[i].set_ylabel('Amplitud')
        axs[i].grid(True, alpha=0.3)
        axs[i].legend()

    for j in range(num_graficos, len(axs)):
        axs[j].axis('off')

    plt.tight_layout()
    plt.show()

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
graficar([(x1, impulso(0, -20, 20)[1])])

#B
funciones = [
    (2, -3, rampa),
    (-1, 2, rampa),
    (-5, 3, escalon)
]
x4 = sum(amp * func(n0, -10, 10)[0] for amp, n0, func in funciones)
graficar([(x4, impulso(0, -10, 10)[1])])


#6
#A
xn = np.concatenate([rampa(0, 0, 5)[0], rampa(5, 6, 11)[0], rampa(-10, 12, 17)[0]])
n = np.arange(0, len(xn))
xn_derivada = np.concatenate([[0], np.diff(xn)])
graficar([(xn, n), (xn_derivada, n)])

#B
"""En el caso continuo, implica que tamibén apliquemos la derivada a tramos, 
lo cual nos va a dar la función escalón para todo el intervalo en conjunto. Con
numpy estamos trabajando las señales como vectores discretos, y como np.diff calcula
la derivada punto por punto por la fórmula 'out[i] = a[i+1] - a[i]', los saltos entre
los puntos de corte de los intervalos, nos darán diferencias negativas.
"""
