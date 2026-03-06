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
xn_derivada = np.concatenate([[0], np.diff(xn)])
graficar([(xn, np.arange(0, len(xn))),
          (xn_derivada, np.arange(0, len(xn)))])

#B
"""En el caso continuo, implica que tamibén apliquemos la derivada a tramos, 
lo cual nos va a dar la función escalón para todo el intervalo en conjunto. Con
numpy estamos trabajando las señales como vectores discretos, y como np.diff calcula
la derivada punto por punto por la fórmula 'out[i] = a[i+1] - a[i]', los saltos entre
los puntos de corte de los intervalos, nos darán diferencias negativas.
"""

#7
x_n = np.concatenate([rampa(0, 0, 5)[0], (rampa(5, 5, 9)[0])[::-1],
                      rampa(9, 10, 14)[0] + 1, 5 * escalon(15, 15, 17)[0],
                      10 * escalon(17, 17, 20)[0]])
graficar([(x_n, np.arange(0, len(x_n)))])

def desplazar_secuencia(x_base, k, n_objetivo):
    x_desplazada = np.zeros_like(n_objetivo, dtype=float)
    for i, n in enumerate(n_objetivo):
        indice_original = n - k
        if 0 <= indice_original < len(x_base):
            x_desplazada[i] = x_base[int(indice_original)]       
    return x_desplazada
#A
x5 = (2 * desplazar_secuencia(x_n, 4, np.arange(-20, 21)) +
      desplazar_secuencia(x_n, 0, np.arange(-20, 21)))
graficar([(x5, np.arange(0, len(x5)))])

#B
n_rango = np.arange(-20, 21)
exp_val, _ = exponencial(0, -20, 20, 0.5, 0)
sin_val, _ = sinusoidal(0, -20, 20, 0.05 * np.pi, 0)
x6 = (0.001 * exp_val.real * desplazar_secuencia(x_n, 0, n_rango) +
      10 * sin_val * desplazar_secuencia(x_n, -2, n_rango))
graficar([(x6, np.arange(0, len(x6)))])