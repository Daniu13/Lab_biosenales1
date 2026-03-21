from scipy.stats import mannwhitneyu
#from statsmodels.tsa.stattools import adfuller
import scipy.io as sio
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def rms(signal):
    n = np.shape(signal)[0]
    rms = np.sqrt(1 / n * np.sum(signal ** 2))
    return rms

def graficar(t, signal, signal2):
    fig, axs = plt.subplots(1, 1, figsize=(20, 10))
    axs.plot(t, signal)
    axs.plot(t, signal2, '-r')
    axs.set_title('Señal')
    axs.set_xlabel('t')
    axs.set_ylabel('Amplitud')
    axs.grid()
    axs.legend()

    plt.tight_layout()
    plt.show()
    return None

fs = 1024 #Hz
signals = sio.loadmat(r'prac3\signals.mat') # cambiar para colab
print(signals.keys())
# 'ECG_asRecording'
# 'EMG_asRecording1'
# 'EMG_asRecording2'

ecg = signals['ECG_asRecording']
ecg_filtrada = signals['ECG_filtered']

emg = signals['EMG_asRecording1']

vec_tiempo = np.arange(0, len(ecg[0]))
print(len(ecg[0]))
print(vec_tiempo)

graficar(vec_tiempo, ecg[0], ecg_filtrada[0])
#graficar(vec_tiempo, ecg_filtrada[0])
