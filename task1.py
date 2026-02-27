import numpy as np
import matplotlib.pyplot as plt

#1
a = [3.1, 1, -0.5, -3.2, 6]
b= [1, 3, 2.2, 5.1, 1]
mult_ab = np.dot(a,b)


#2
matriz = np.array([[2, -1, -3],
          [4, 1.5, -4.5],
          [7.3, -0.9, 0.2]])
matriz_T = matriz.T


#3
unos = np.ones((2, 3)) #ones
redondeada = np.round(matriz) #round
red_arriba = np.ceil(matriz) #ceil
red_abajo = np.floor(matriz) #floor


#4
valor_02 = matriz[0][2]
print(valor_02)

valor_1 = matriz[1]
print(valor_1)

print(np.shape(matriz))

#5
n = np.arange(0, 101)
yn = np.sin(np.pi*0.12*n)
y2n = np.cos(2*np.pi*0.03*n)

fig, axs = plt.subplots(1, 2, figsize=(10, 4))
axs[0].plot(n, yn, 'b-')
axs[0].set_title('Yn')
axs[0].set_xlabel('n')
axs[0].set_ylabel('func')

axs[1].plot(n, y2n, "r-")
axs[1].set_title('Y2n')
axs[1].set_xlabel('n')
axs[1].set_ylabel('func')

plt.tight_layout()
plt.show()


#5
sn = yn + y2n
tn = yn*y2n

fig, axs = plt.subplots(1, 2, figsize=(10, 4))
axs[0].plot(n, sn, 'b-')
axs[0].set_title('Sn')
axs[0].set_xlabel('n')
axs[0].set_ylabel('func')

axs[1].plot(n, tn, "r-")
axs[1].set_title('tn')
axs[1].set_xlabel('n')
axs[1].set_ylabel('func')

plt.tight_layout()
plt.show()

#6
fig, axs = plt.subplots(1, 1, figsize=(5, 4))
axs.plot(n, yn, 'b-', label="Yn")
axs.plot(n, y2n, 'r-', label="Y2n")
axs.set_title('Señales Yn y Y2n')
axs.set_xlabel('n')
axs.set_ylabel('func')
axs.legend()

plt.tight_layout()
plt.show()

#7
fig, axs = plt.subplots(1, 1, figsize=(5, 4))
axs.plot(n, sn, 'b-', label="Sn")
axs.plot(n, tn, 'r-', label="tn")
axs.set_title('Señales Sn y tn')
axs.set_xlabel('n')
axs.set_ylabel('func')
axs.legend()

plt.tight_layout()
plt.show()